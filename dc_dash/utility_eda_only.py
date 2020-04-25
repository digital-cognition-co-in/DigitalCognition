#!/bin/bash

from .sql_queries_all import *
from .dc_bokeh_plots import *
from .dc_eda_funcs import *
from .models import *
from .forms import*
#import codecs
import subprocess
from subprocess import call
import json , time , psycopg2 , io , os , re 
import pandas as pd


# for deleting the model - importing CONNECTION
from django.db import connection, DatabaseError, IntegrityError, OperationalError
from django.db.models.fields import (BinaryField, BooleanField, CharField, IntegerField,
PositiveIntegerField, SlugField, TextField)
from django.shortcuts import redirect
from django.core.files import File

from django.conf import settings
#from settings import * ## Wont Work -- Code below has chained Imports === user = settings.DATABASES['default']['USER']
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from collections import OrderedDict
from sqlalchemy import create_engine
       


class utility_eda_only_class():
    def __init__(self):
        pass        

    import datetime
    dt_now = str(datetime.datetime.now())
    dt_all_now = datetime.datetime.now()
    minute_now = dt_all_now.minute
    #print("--------dt_all_now.minute---------",dt_all_now.minute)
    #now = datetime.datetime.now()
    #print(now.year, now.month, now.day, now.hour, now.minute, now.second)

    def test_CodeMirror(request):
        return render(request,'dc_dash/codeMirror_test1.html')


    def get_userInput_BokehBoxPlot(request):
        """
        Get userInput - Column Clicked values for == bokeh_boxplot_large_userInputs(self,col_with_CategoricalValues):
        HTML Template == /dc_dash/templates/dc_dash/eda_landing_index.html 
        """
        if request.method == 'POST':
            # print(request)
            # print(request.POST)
            col_index_clicked = request.POST.getlist('col_num')
            print("-FILE => utility_eda_only => get_userInput_BokehBoxPlot => col_index_clicked--",col_index_clicked) #
            # ['1'] ## For Column 1 of dataTable
            print("       "*90)
            col_with_CategoricalValues = str(col_index_clicked[0])
            bokeh_class_obj = bokeh_class() #
            db_table_name =  bokeh_class_obj.bokeh_boxplot_large_userInputs(col_with_CategoricalValues)
            
        return render(request,'dc_dash/dhankar_sidebar.html')
    
    
    def showCategoricalCols_view(request):
        """
        #JIRA_ROHIT_25APR -- Check if this is required - No More Modals ? 
        #JIRA_ROHIT_25APR -- All - postgresql Conn creation in methods to be deleted - all conns to be created from a central method 
        This Func passes the JSON for AJAX to Modal == modal_CategoricalCols
        """
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
        #limit_records = 1500 ## as its EDA SUMMARY - All Records required 
        
        latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        myDict_dataSetName = latest_dataSetName[0]
        for keys , values in myDict_dataSetName.items():
            if "dataset_name" in keys:
                dataset_name = str(values)

        #sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(dataset_name),str(limit_records))
        sql_command = "SELECT * FROM {}.{} ;".format(str(schema_default_public), str(dataset_name))
        df_for_cat_cols = pd.read_sql(sql_command,engine)
        #
        df_for_cat_cols.to_pickle("./df_for_cat_cols.pkl")
        #
        df_for_cat_cols = pd.read_pickle("./df_for_cat_cols.pkl")
        #
        # print("----UTILY_eda_ONLY==AFTER--====read_pickle===--df_for_cat_cols--------",df_for_cat_cols)
        # print("   "*90)

        df_with_cat_cols = showCategoricalCols(df_for_cat_cols)
        ### Can get -- All DF's here --- But how to show in JSON DICT for AJAX ??
        ## If we create - more than 1 AJAX URL's ???
        ## To Avoid hitting the DB again and AGAN --- create a PICKLE of the EDA--dataSet --- the TEMP DATASET for EDA ...
        ## Use that PICKLE file for ALL KINDS of PROCESSING ---- ?? 

        #print("----From == UTILY_eda_ONLYutility_eda_only==--df_with_cat_cols--------",df_with_cat_cols)
        #print("   "*90)
        #
        #showCategoricalCols
        data = json.loads(df_with_cat_cols.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        #print("-----UTILY_eda_ONLY-showCategoricalCols_view--dict_json----=====---",dict_json) # OK Dont 
        #
        return JsonResponse(dict_json, safe= False)


    def eda_ExtractEmailParts(self):
        """
        PARAMS from JS = colIndx saved in Django model == temp_colIndex_for_Eda() == column_index_from_dataTables_js
        
        """
        from sqlalchemy import create_engine

        #latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        colIndx_email = temp_colIndex_for_Eda.objects.all().values('column_index_from_dataTables_js').order_by('-pk')[0:1]
        # print("======colIndx_email=======",colIndx_email) ## Index Starts at ZERO 
        myDict_colIndx_email = colIndx_email[0]
        for keys , values in myDict_colIndx_email.items():
            if "column_index_from_dataTables_js" in keys:
                colIndx_email = int(values)
                print("======colIndx_email=======",colIndx_email)

        #
        latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        myDict_dataSetName = latest_dataSetName[0]
        for keys , values in myDict_dataSetName.items():
            if "dataset_name" in keys:
                dataset_name = str(values)
        
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
        limit_records = 1500 ## JIRA_ROHIT_PendingTask --- 10AUG19 --- Time without Limits for Larger dataSets 
        #
        

        #sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(dataset_name),str(limit_records))
        sql_command = "SELECT * FROM {}.{} ;".format(str(schema_default_public), str(dataset_name))
        df_emailParts = pd.read_sql(sql_command,engine)
        #df_emailParts

        #try:
        #print(type(colIndx_email))
        #print("                "*90)

        # col = param['column_name']
        #col = colIndx_email
        #location_col = df_emailParts.columns.get_loc(col) #
        # This here EXPECTS a COL NAME from which it will give COL INDEX --- see above == param['column_name']
        # OldSick was passing in COL NAMES === me DC COL INDEX 
        #print("=====location_col=========",location_col)
        #print("                    "*90)

        col_name = df_emailParts.columns[colIndx_email]
        #print("=====col_name=======",col_name)
        #print("                    "*90)


        idy = colIndx_email + 1
        
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        result = df_emailParts[col_name].apply(lambda x: extractEmail(x, EMAIL_REGEX)).apply(pd.Series) 
        #print("========RESULT=========",result) ## OK 
        #print("                    "*90)

        
        mydf = pd.DataFrame(result.values.tolist(), index= result.index)
        ls_df_cols = df_emailParts.columns.tolist() ## Get a LIST of DF COLUMNS 
        # new_name = getNewColName(str(df[col].name) + "_Email_Part_1" + "_1", ls_df_cols) 
        ## JIRA_ROHIT_PendingTask == OK Old Scik Code Not Used  
        # new_name1 = getNewColName(str(df[col].name) + "_Email_Part_2" + "_1", ls_df_cols)
        new_name = "Email_Part1_LocalName"
        new_name1 = "Email_Part2_DomainAddress"

        mydf.columns = [new_name,new_name1] # Creating Columns LABELS for the first time ?? 
        df1 = pd.concat([df_emailParts,mydf],axis=1)
        ls_df_cols.insert((idy),new_name)
        ls_df_cols.insert((idy+1),new_name1) 
        df1 = df1[ls_df_cols]
        #print("========df1========",df1) # OK 
        #print("              "*90)

        return df1

        # except Exception as e:
        #     raise e 


    def extractEmail(data, regexpression):

        '''
        This method identifies the email part from a string and the then splits the string on the basis of @ to separate id and domain from it.
        Param1: data - a string object which contains a cell value of a column
        Param2: regexpression - a string object which contains the regular expression for email. This parameter is part of code only, not from user input
        Returns: List of String
        '''
        try:
            if(re.match(regexpression, str(data)) != None):
                ls_1 = str(data).split('@')
                return ls_1
            else:
                return None    

        except Exception as e:
            print(e)
            raise e



        
        
            #

        








