#!/bin/bash

from django.core.files import File
import re , io , json , gzip
import pandas as pd
from .models import *
from .utily import*
from .forms import*
from django.shortcuts import redirect

#import codecs
import subprocess
from subprocess import call

# for deleting the model - importing CONNECTION
#
from django.db import connection, DatabaseError, IntegrityError, OperationalError
from django.db.models.fields import (BinaryField, BooleanField, CharField, IntegerField,
                                     PositiveIntegerField, SlugField, TextField)

from .dc_eda_funcs import *
from django.conf import settings
# from settings import * ## Wont Work -- Code below has chained Imports === user = settings.DATABASES['default']['USER']
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse  
from collections import OrderedDict
from sqlalchemy import create_engine
from .sql_queries_all import *
# from .dc_bokeh_plots import *
# from .dc_holoviews import *
# from .utility_eda_only import *


def eda_ceil_and_floor_outPut(self): 
    """
    https://github.com/digital-cognition-co-in/DigitalCognition/issues/17
    
    """
    from sqlalchemy import create_engine
    from .dc_eda_funcs import save_postEdaDataSet
    latest_MatchSimilarText = eda_inputs_MatchSimilarText.objects.all().values(
        'fuzziness', 'str_to_compare_with').order_by('-pk')[0:1]
        myDict = latest_MatchSimilarText[0]
        for keys, values in myDict.items():
            if "fuzziness" in keys:
                fuzziness = str(values)
            if "str_to_compare_with" in keys:
                str_to_compare_with = str(values)

        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name,
        )
        engine = create_engine(database_url, echo=False)
        schema_default_public = "public"
        limit_records = 1500  # as its EDA

        #latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        qs_counter_for_dfFromEDA = temp_dataSetName_dfFromEDA.objects.all().values('counter_for_dfFromEDA').order_by('-pk')[0:1]
        # JIRA_ROHIT_PendingTask== qs_counter_for_dfFromEDA = temp_dataSetName_dfFromEDA.objects.all().values('counter_for_dfFromEDA').order_by('-pk')[0:1]
        # JIRA_ROHIT_PendingTask== #print("------QUERY SET----qs_counter_for_dfFromEDA------------",qs_counter_for_dfFromEDA)
        # First RUN Above shall be an EMPTY QUERYSET --- as NO VALUES for COUNTER == <QuerySet []>
        if qs_counter_for_dfFromEDA.exists():
            # We are NOT in FIRST RUN ..
            myDict_counter = qs_counter_for_dfFromEDA[0]
            for keys, values in myDict_counter.items():
                if "counter_for_dfFromEDA" in keys:
                    latest_counter_for_dfFromEDA = int(values)
            # THIS will Always be TRUE HERE --- as above we Checked for NOT IN FIRST RUN ...
            if latest_counter_for_dfFromEDA > 0:
                #print("---------GOT COUNTER > 0  latest_counter_for_dfFromEDA======",latest_counter_for_dfFromEDA)
                latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
                #print("=====FOR TESTING -- 06 AUG === ",latest_dataSetName) #
                # ABOVE OK Gets CurrentEDA Chosen EDA>>GO ... Not required to be last CSV Uploaded
                # JIRA_ROHIT_ Below earlier Code Incorrect will only Work if ??? latest_dataSetName === is the DataSet created by LATEST CSV IMPORT ??
                # JIRA_ROHIT_ latest_dataSetName = temp_dataSetName_dfFromEDA.objects.all().values('temp_dataset_name').order_by('-pk')[0:1]
                myDict_dataSetName = latest_dataSetName[0]
                for keys, values in myDict_dataSetName.items():
                    if "dataset_name" in keys:  # JIRA_ROHIT_PendingTask Corrected == earlier had == temp_dataset_name
                        dataset_name = str(values)
                        #print("----FILE==UTILY.py--latest_dataSetName = temp_dataSetName_for_EDALanding--dataset_name-------------",dataset_name)
                        #print("              JIRA_ROHIT_PendingTask======")
        else:
            #print("FIRST RUN OF DATA SET __________")
            #print("     "*90)
            ##print("---------GOT COUNTER == 0  latest_counter_for_dfFromEDA======",latest_counter_for_dfFromEDA)
            latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values(
                'dataset_name').order_by('-pk')[0:1]
            myDict_dataSetName = latest_dataSetName[0]
            for keys, values in myDict_dataSetName.items():
                if "dataset_name" in keys:
                    dataset_name = str(values)
        # JIRA_ROHIT_PendingTask----This here DOES NOT Give CORRECT COL INDEX == column_index_from_dataTables_js
        # THIS == temp_colIndex_for_Eda === gets saved in DJANGO MODEL ABOVE in FUNC == eda_get_value_from_js(request):
        latest_colIndex = temp_colIndex_for_Eda.objects.all().values(
            'column_index_from_dataTables_js').order_by('-pk')[0:1]
        if latest_colIndex.exists():
            # this above Django QuerySet Exists:
            myDict_colIndex = latest_colIndex[0]
            for keys, values in myDict_colIndex.items():
                if "column_index_from_dataTables_js" in keys:
                    column_index = str(values)
                    #print("----FILE==Utily.py === def eda_MatchSimilarText_outPut(self): --GOT COL INDEX ---WHY THIS COMMENT == JIRA_ROHIT_PendingTask get query SET Exists Check here??? -----",column_index)
        else:
            #print("---FROM UTILY.py NO COL INDEX YET ---------") #
            column_index = int(3)
            # JIRA_ROHIT_PendingTask Hardcoded below == column_index = int(3)
            # If USER has Not Clicked ona  COLUMN to Pass in JS >> latest_colIndex
            # Just use default COLUMN_Index == 3
            # This needs a JavaScript_WARNING - JavaScript_ALERT on the FRONT END.

        sql_command = "SELECT * FROM {}.{} limit {};".format(
            str(schema_default_public), str(dataset_name), str(limit_records))
        df_for_eda = pd.read_sql(sql_command, engine)
        df_from_eda = matchSimilarText(df_for_eda, fuzziness, str_to_compare_with, column_index)
        data = json.loads(df_from_eda.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        # JIRA_ROHIT_PendingTask == 06AUG19 --- All this below here CHECK ...
        counter_for_dfFromEDA = 0
        temp_dataset_name = save_postEdaDataSet(
            df_from_eda, dataset_name)  # JIRA_ROHIT_PendingTask
        # func-delete_temp_dataSets(temp_dataset_name) ## Some kind of delayed Delete of temp DataSets
        #print("---FILE==UTILY.py--TBD---Send to TEMPLATE FrontEnd --- temp_dataset_name----",temp_dataset_name)
        if temp_dataset_name != None:
            counter_for_dfFromEDA += 1
        model = temp_dataSetName_dfFromEDA()
        model.counter_for_dfFromEDA = int(counter_for_dfFromEDA)
        model.temp_dataset_name = str(temp_dataset_name)
        model.save()

        return JsonResponse(dict_json, safe=False)
