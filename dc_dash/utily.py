# File "/media/dhankar/Dhankar_1/a1_19/bitbucket_up/newsdjangomain/dc_dash/utily.py", line 286, in eda_SearchAndReplace_outPut
#     myDict_colIndex = latest_colIndex[0]


#!/bin/bash

from django.core.files import File
import re  # regex
import io  # for Input OutPut File to be written
import pandas as pd
import json 
from .models import *
# from .calc_1 import*
# from .calc_2 import*
from .utily import*
from .summary_stats_1 import*
#from .predictive_1 import*
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

import gzip
# from .scraping import * #
# from .scrap_LinkedIn_ import *
from .dc_eda_funcs import *

from django.conf import settings
#from settings import * ## Wont Work -- Code below has chained Imports === user = settings.DATABASES['default']['USER']
#
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
#
from django.http import JsonResponse ### DHANK ---FEB19
from collections import OrderedDict
from sqlalchemy import create_engine
#
from .sql_queries_all import *
#from .dc_bokeh_apr19 import *
from .dc_bokeh_plots import *
from .dc_holoviews import *
from .utility_eda_only import *

#



from django.contrib.auth.decorators import login_required
@login_required(login_url='/admin_approved_accounts/login/') 
class utily_class():
    def __init__(self):
        pass        

    import datetime
    dt_now = str(datetime.datetime.now())
    dt_all_now = datetime.datetime.now()
    minute_now = dt_all_now.minute
    ##print("--------dt_all_now.minute---------",dt_all_now.minute)


    import datetime
    now = datetime.datetime.now()
    ##print(now.year, now.month, now.day, now.hour, now.minute, now.second)

    
    #model_4.objects.all.delete()  ## gave errors - own SO Answer to old post 
    #https://stackoverflow.com/questions/4532681/how-to-remove-all-of-the-data-in-a-table-using-django/47492991#47492991

    from django.shortcuts import render
    from django.http import HttpResponse, JsonResponse
    from django.template import loader
    import json
    import time 
    import psycopg2
    import io , os 

    def modalSimpleTest(request):
        return render(request,'dc_dash/includes/modalSimpleTest.html')


    def iFrame_EdaColActions_view(request):
        """
        iFrame_EdaColActions_view
        """
        
        return render(request,'dc_dash/includes/modal_EDA_Col_Actions.html') #
        # This PAGE = as iFRAME in the eda_SideBar. 
        


    def tableAu_reportsDimensions(self):  
        """
        tableAu_reportsDimensions
        """
        from sqlalchemy import create_engine
        from .dc_eda_funcs import tableAuReports_Metrics
        
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
        #
        
        latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        myDict_dataSetName = latest_dataSetName[0]
        for keys , values in myDict_dataSetName.items():
            if "dataset_name" in keys:
                dataset_name = str(values)

        # Not using Latest COLUMN Index - as we do SUMMARY STATS for Complete DF
        # latest_colIndex = temp_colIndex_for_Eda.objects.all().values('column_index_from_dataTables_js').order_by('-pk')[0:1]
        # myDict_colIndex = latest_colIndex[0]
        # for keys , values in myDict_colIndex.items():
        #     if "column_index_from_dataTables_js" in keys:
        #         column_index = str(values)
        
        #sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(dataset_name),str(limit_records))
        sql_command = "SELECT * FROM {}.{} ;".format(str(schema_default_public), str(dataset_name))
        df_for_TableAuReports = pd.read_sql(sql_command,engine)
        ls_tableAu_Metrics_ColNames , ls_ColTableAuReports_Dimensions = tableAuReports_Metrics(df_for_TableAuReports)
        # #print("==========ls_tableAu_Metrics_ColNames============",ls_tableAu_Metrics_ColNames)
        # #print("==========ls_ColTableAuReports_Dimensions============",ls_ColTableAuReports_Dimensions)
        # #
        #df_TableAuRepoMetsnDims = pd.DataFrame({'dims_json':ls_ColTableAuReports_Dimensions,'metrics_json':ls_tableAu_Metrics_ColNames},columns=['dims_json','metrics_json'])

        keys = ['dims_json','metrics_json']
        values = [ls_ColTableAuReports_Dimensions,ls_tableAu_Metrics_ColNames]

        #data = json.loads(dict(zip(keys, values)))
        data = dict(zip(keys, values))
        
    
        #data = json.loads(df_TableAuRepoMetsnDims.to_json(orient='split'))

        # dims_json = json.dumps(ls_ColTableAuReports_Dimensions)
        # metrics_json = json.dumps(ls_tableAu_Metrics_ColNames)

        dict_json = {}
        dict_json['data_json'] = data
        
        #print("-----UTILY--tableAu_reportsDimensions---dict_json-------AAAAAAAAAAAAA-----",dict_json) # OK Dont 
        return JsonResponse(dict_json, safe= False)
    



    def nonModal_TableAuReports(request):
        
        return render(request,'dc_dash/includes/nonModal_TableAuReports.html')



    def modal_psql_CentOS(request):
        #conn_cursor = query_psql_CentOS7_Droplet() // JIRA_ROHIT_PendingTask HERE -- this Uncomment this is OK 
        # JIRA_ROHIT_PendingTask below here - need to get 

        # data = json.loads(df_for_pg_stat_activity.to_json(orient='split'))
        # dict_json = {}
        # dict_json['data_json'] = data
        # return JsonResponse(dict_json, safe= False)
        return render(request,'dc_dash/eda_sidebar.html')


    def holoviews_bar_small_view(request):
        """
        holoviews_bar_small_view
        """
        holoviews_class_obj = holoviews_class() #
        js_holo_bar,div_holo_bar,cdn_js_holo_bar,cdn_css_holo_bar = holoviews_class_obj.holoviews_bar_small()
        context = {"graphname": "categorical_bar_plot",
                "div_bokeh": div_holo_bar,
                "js_bokeh": js_holo_bar,
                "cdn_js": cdn_js_holo_bar,
                "cdn_css": cdn_css_holo_bar,
                    }                           
                #
                # 2nd PLOT on same page ..
                #    "div1": div1,
                #    "js1": js1,
                #    "cdn_js1": cdn_js1,
                #    "cdn_css1": cdn_css1,
                #
        #return JsonResponse(context, safe= False)
        return render(request,'dc_dash/includes/Charts_and_Plots/dc_bokeh_charts_apr19.html',context) #
        # This PAGE = as iFRAME in the eda_SideBar MODAL . 
        # 



    def dc_bokeh_scatterPlot_view(request):
        """
        bokeh_scatter_iris
        """
        bokeh_class_obj = bokeh_class() #
        js_bokeh,div_bokeh,cdn_js,cdn_css = bokeh_class_obj.bokeh_scatter_iris()#
        ##print("========FROM UTILY_js_bokeh=============",js_bokeh)
        #
        context = {"graphname": "tukey_boxPlot",
                "div_bokeh": div_bokeh,
                "js_bokeh": js_bokeh,
                "cdn_js": cdn_js,
                "cdn_css": cdn_css,
                    }
                #
                # 2nd PLOT on same page ..
                #    "div1": div1,
                #    "js1": js1,
                #    "cdn_js1": cdn_js1,
                #    "cdn_css1": cdn_css1,
                #
        #return JsonResponse(context, safe= False)
        return render(request,'dc_dash/includes/Charts_and_Plots/dc_bokeh_scatterPlot_apr19.html',context) #
        # This PAGE = as iFRAME in the eda_SideBar MODAL . 


    def bokeh_boxplot_clicks_from_js(request):
        """
        bokeh_boxplot_clicks_from_js
        """
        if request.method == 'POST':
            clicked_box_outlier = request.POST.get('clicked_box_outlier')
            print("----UTILY.py == bokeh_boxplot_clicks_from_js== ----clicked_box_outlier-----------",clicked_box_outlier)
            if clicked_box_outlier != None:
                #Input to Bokeh Func for BoxPlot Design 
                print("------Bokeh Func for BoxPlot Design --")
                # model = temp_colIndex_for_Eda()
                # model.column_index_from_dataTables_js = str(col_num)
                # model.save()
        return render(request,'dc_dash/eda_sidebar.html')



    
    # def dc_bokeh_BoxPlot_viewSmall(request):
    #     """
    #     dc_bokeh_BoxPlot_viewSmall
    #     """
    #     #
    #     bokeh_class_obj = bokeh_class() #
    #     js_bokeh,div_bokeh,cdn_js,cdn_css = bokeh_class_obj.bokeh_tukey_summary_boxplot_small()#
    #     #
    #     context = {"graphname": "tukey_boxPlot",
    #             "div_bokeh": div_bokeh,
    #             "js_bokeh": js_bokeh,
    #             "cdn_js": cdn_js,
    #             "cdn_css": cdn_css,
    #                 }
    #             #
    #             # 2nd PLOT on same page ..
    #             #    "div1": div1,
    #             #    "js1": js1,
    #             #    "cdn_js1": cdn_js1,
    #             #    "cdn_css1": cdn_css1,
    #             #
    #     #return JsonResponse(context, safe= False)
    #     return render(request,'dc_dash/dc_bokeh_tukey_boxplot_small.html',context) #
    #     # This PAGE = as iFRAME in the eda_SideBar MODAL . 

    def send_dfToJSON_forBokeh(request):
        """
        send_dfToJSON == 
        """
        from sqlalchemy import create_engine
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
        sql_command = "SELECT * FROM {} ;".format(str(dataset_name)) #
        df_for_bokeh = pd.read_sql(sql_command,engine)
        #df_for_bokeh.to_pickle("./df_holoviewPlots.pkl")
        # Inplace of above - done Local Storage in JS  --- localStorage.setItem --  # Send JSON from here
        data = json.loads(df_for_bokeh.to_json(orient='split')) 
        dict_json = {}
        dict_json['data_json'] = data
        return JsonResponse(dict_json, safe= False)



    def dc_holoviews_violinPlot_small(request):
        """
        dc_holoviews_violinPlot_small == This Method called always - its a default call within Sidebar.html 
        CREATE's a PICKLE file on Local DIR - of a DF from latest == temp_dataSetName_for_EDALanding
        DF from PICKLE used by ALL - Bokeh / Holoviews Plots - they will not have to read PSQL ..
        
        """
        
        holoviews_class_obj = holoviews_class() #
        js_violin_plot,div_violin_plot,cdn_js_violin_plot,cdn_css_violin_plot , js_violin_plot1,div_violin_plot1,cdn_js_violin_plot1,cdn_css_violin_plot1 = holoviews_class_obj.holoviews_violinPlot_small()#
        #
        context = {"graphname": "ViolinPlot",
                "div_bokeh": div_violin_plot1,
                "js_bokeh": js_violin_plot1,
                "cdn_js": cdn_js_violin_plot1,
                "cdn_css": cdn_css_violin_plot1,
                    }
                #
                # 2nd PLOT on same page ..
                #    "div1": div1,
                #    "js1": js1,
                #    "cdn_js1": cdn_js1,
                #    "cdn_css1": cdn_css1,
                #
        #return JsonResponse(context, safe= False)

        
        return render(request,'dc_dash/includes/Charts_and_Plots/dc_bokeh_HoloViews_plot2.html',context) #
        ## /media/dhankar/Dhankar_1/a1_19/bitbucket_up/newsdjangomain/dc_dash/templates/dc_dash/dc_bokeh_HoloViews_plot2.html
        # This PAGE = as iFRAME in the eda_SideBar MODAL . 
    

    def dc_holoviews_violinPlot_large(request):
        """
        dc_holoviews_violinPlot_large
        """
        #
        holoviews_class_obj = holoviews_class() #
        js_violin_plot,div_violin_plot,cdn_js_violin_plot,cdn_css_violin_plot , js_violin_plot1,div_violin_plot1,cdn_js_violin_plot1,cdn_css_violin_plot1 = holoviews_class_obj.holoviews_violinPlot_large()#
        #
        context = {"graphname": "ViolinPlot",
                "div_bokeh": div_violin_plot1,
                "js_bokeh": js_violin_plot1,
                "cdn_js": cdn_js_violin_plot1,
                "cdn_css": cdn_css_violin_plot1,
                    }
                #
                # 2nd PLOT on same page ..
                #    "div1": div1,
                #    "js1": js1,
                #    "cdn_js1": cdn_js1,
                #    "cdn_css1": cdn_css1,
                #
        #return JsonResponse(context, safe= False)
        return render(request,'dc_dash/includes/Charts_and_Plots/dc_bokeh_Holoviews_plot1.html',context) #
        # This PAGE = as iFRAME in the eda_SideBar MODAL . 
    
    


    # def dc_holoviews_plotview(request):
    #     """
    #     ORIGINAL -- Cars MPG Example -Not Reqd-- dc_holoviews_plotview
    #     """
    #     #
    #     holoviews_class_obj = holoviews_class() #
    #     #violin_plot = holoviews_class_obj.holoviews_violin_autompg()#
    #     ## js_violin_plot,div_violin_plot,cdn_js_violin_plot,cdn_css_violin_plot
    #     js_bokeh,div_bokeh,cdn_js,cdn_css = holoviews_class_obj.holoviews_plot_1()#
    #     #
    #     context = {"graphname": "tukey_boxPlot",
    #             "div_bokeh": div_bokeh,
    #             "js_bokeh": js_bokeh,
    #             "cdn_js": cdn_js,
    #             "cdn_css": cdn_css,
    #                 }
    #             #
    #             # 2nd PLOT on same page ..
    #             #    "div1": div1,
    #             #    "js1": js1,
    #             #    "cdn_js1": cdn_js1,
    #             #    "cdn_css1": cdn_css1,
    #             #
    #     #return JsonResponse(context, safe= False)
    #     return render(request,'dc_dash/dc_bokeh_Holoviews_plot1_test.html',context) #
    #     # This PAGE = as iFRAME in the eda_SideBar MODAL . 
    
    
        

    def dc_bokeh_BoxPlot_view(request):
        """
        ##bokeh_tukey_summary_boxplot 
        """
        #
        bokeh_class_obj = bokeh_class() #
        js_bokeh,div_bokeh,cdn_js,cdn_css = bokeh_class_obj.bokeh_tukey_summary_boxplot_large()#
        #
        context = {"graphname": "tukey_boxPlot",
                "div_bokeh": div_bokeh,
                "js_bokeh": js_bokeh,
                "cdn_js": cdn_js,
                "cdn_css": cdn_css,
                    }
                #
                # 2nd PLOT on same page ..
                #    "div1": div1,
                #    "js1": js1,
                #    "cdn_js1": cdn_js1,
                #    "cdn_css1": cdn_css1,
                #
        #return JsonResponse(context, safe= False)
        return render(request,'dc_dash/includes/Charts_and_Plots/dc_bokeh_tukey_boxplot_apr19.html',context) #
        # This PAGE = as iFRAME in the eda_SideBar MODAL . 
    
                  

    def summaryStats_getColVal(request):
        if request.method == 'POST':
            col_num = request.POST.get('col_num')
            ##print("----------col_num-----------",col_num)
            # if col_num != None:
            #     model = temp_colIndex_for_Eda()
            #     model.column_index_from_dataTables_js = str(col_num)
            #     model.save()
            dict_json = {}
            # Dummy Testing ...
        return JsonResponse(dict_json, safe= False)

    def drop_delete_click_from_js(request):
        if request.method == 'POST':
            clicked_drpDown = request.POST.get('clicked_drpDown')
            #print("----UTILY.py == drop_delete_click_from_js== ----clicked_drpDown-----------",clicked_drpDown)
            #if clicked_drpDown != None:
                # model = temp_colIndex_for_Eda()
                # model.column_index_from_dataTables_js = str(col_num)
                # model.save()
        return render(request,'dc_dash/dhankar_sidebar.html')


    #from django.views.decorators.csrf import csrf_exempt
    #@csrf_exempt

    def psql_tableNames_from_js_for_drop(request):
        """
        this is related to func above == drop_delete_click_from_js
        """
        if request.method == 'POST':
            # #print(request)
            # #print(request.POST)
            array_of_clicks = request.POST.getlist('array_of_clicks[]')
            #print("--psql_tableNames_from_js_for_drop===-LIST ===-----array_of_clicks-----------",array_of_clicks)
            #print("===========TESTING===AUg19==========")
            #print("        "*180)

            ### JIRA_ROHIT_PendingTask --- this array_of_clicks == always has only 1 VALUE ?? 
            ## This is because in the JS in dhankar_sidebar.html === we have == if (typeof array_of_clicks !== 'undefined' && array_of_clicks.length ==1) {
            ## then why do we need == str(array_of_clicks[0] == below ?? 
            db_table_name = psql_drop_delete_tables(str(array_of_clicks[0]))
            #print("-----------DROPPED ---------",db_table_name)
        return render(request,'dc_dash/dhankar_sidebar.html')


    def psql_tableNames_from_js_for_delete(request):
        """
        this is related to func above == drop_delete_click_from_js
        """
        if request.method == 'POST':
            # #print(request)
            # #print(request.POST)
            array_of_clicks = request.POST.getlist('array_of_clicks[]')
            ##print(type(array_of_clicks)) ## LIST from getlist()
            #print("--psql_tableNames_from_js_for_delete===-LIST ===-----array_of_clicks-----------",array_of_clicks)
            #def psql_merge_basic(data_table1,data_table2,new_table_name):
            df_new_table_name = psql_merge_basic(str(array_of_clicks[0]),str(array_of_clicks[1]),str("JIRA_ROHIT_PendingTask_JIRA_ROHIT_PendingTaskab"))
            #print("-------------psql_tableNames_from_js_for_delete----------UTILyyy",df_new_table_name)
            #print("    "*90)
        return render(request,'dc_dash/dhankar_sidebar.html')

    def psql_click_from_js(request):
        if request.method == 'POST':
            clicked_drpDown = request.POST.get('clicked_drpDown')
            #print("--------clicked_drpDown-----------",clicked_drpDown)
            #if clicked_drpDown != None:
                # model = temp_colIndex_for_Eda()
                # model.column_index_from_dataTables_js = str(col_num)
                # model.save()
        return render(request,'dc_dash/eda_sidebar.html')

    # def psql_tableNames_from_js_for_merge1(request):
    #     if request.method == 'POST':
    #         #print(request)
    #         #print(request.POST)
    #         new_merged_tableName = request.POST.get('new_merged_tableName')
    #         #print("---POST.get === new_merged_tableName=====>>",new_merged_tableName)
    #     return render(request,'dc_dash/sql_action_MergeTables.html')

    def render_merged_table_htmlPage(request):
        return render(request,'dc_dash/sql_action_MergeTables.html')

    def autocomplete(request):
        return render(request,'dc_dash/dc_autoCompleteTest.html')

    def reports_codeMirror(request):
        return render(request,'dc_dash/dc_reports_codeMirror.html')


    def view_pyTo_codeMirror(request):
        """
        """
        #
        ##print("------view_pyTo_codeMirror----HIT HERE -------------") # OK 
        # # CREATE CONN only if VALID POST Request Comes Through .......
        import psycopg2
        schema_default_public = "public"
        psql_user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        conn = psycopg2.connect("dbname="+str(database_name)+" "+"user="+str(psql_user)+" "+"password="+str(password)+"")
        conn_cursor = conn.cursor()
        
        #latest_dataSetName = temp_dataSetName_for_EDALanding.objects.values_list('dataset_name',flat=True).order_by('-pk') [0:5]
        
        #JIRA_ROHIT_PendingTask===>> flat=True
        latest_dataSetName= csv_document.objects.values_list('dataset_name',flat=True).order_by('-pk') [0:5]
        #dataset_name
        #### JIRA_ROHIT_PendingTask JIRA_ROHIT_PendingTask --- this Django Model table has --- 1900 Plus Records 
        ## http://localhost:8001/admin/dc_dash/temp_datasetname_for_edalanding/
        
        latest_dataSetName = list(latest_dataSetName)
        #print(type(latest_dataSetName))
        #print("    "*90)
        #print(len(latest_dataSetName))
        #print("    "*90)
        #
        ##print("---------ls_csv_documents--------",ls_csv_documents)
        #print("    "*90)
        ##print("---------latest_dataSetName------",latest_dataSetName)
        #print("    "*90)
        # conn_cursor.execute("INSERT INTO dc_tableNames_for_merge (temp_tableName, temp_tableName1 , new_merged_tableName) VALUES (%s, %s , NULL)", (str(array_of_clicks[0]), str(array_of_clicks[1])))
        # conn.commit()
        conn.close()
        #
        df_forCodeMirror = pd.DataFrame(latest_dataSetName) ## this doesnt give COL_NAMES 
        # json_ls = json.dumps(latest_dataSetName)
        # #print("---------json_ls--------",json_ls)
        # #print("    "*90)
        # #
        #json_ls = {'table_11':"nulla",'table_12':"nullb"} ## Not 
        #

        df_forCodeMirror.columns = ['tables_Colname']

        tables_forCodeMirror = json.loads(df_forCodeMirror.to_json(orient='split')) 
        ## If only ERROR == EXCEPT from FUNC == psql_merge_basic
        ## then above line will throw ERROR == data = json.loads(df_table_fromMerge.to_json(orient='split'))
        #AttributeError: 'str' object has no attribute 'to_json
        dict_json = {}
        dict_json['tables'] = latest_dataSetName
        #print("---dict_json-----",dict_json)
        # dict_json['table_one'] = table_one ## This line held on as an example - not used here 
        # dict_json['table_two'] = table_two ## This line held on as an example - not used here 
        ##print("---------------dict_json--------------",dict_json)
        return JsonResponse(dict_json, safe= False)
        #return JsonResponse(json_ls, safe= False)


    
    def view_codeMirror_toPy(request):
        """
        """
        #
        select_table = "SELECT"
        astrx = "*"
        from_table = "FROM"
        #
        if request.method == 'POST':
            ##print(request) ## <WSGIRequest: POST '/dc/url_codeMirror_toPy/'>
            #print(request.POST) 
            ## <QueryDict: {'csrfmiddlewaretoken': ['HrpptnbjqlR0576kHi02QwgeHmmDcRsfQQajRQ7Z3JL73xFcOxsKww7VL0tcKLae'], 'codeValue_toPy': [' SELECT * FROM dc_codeMirror;  new_line_JIRA_ROHIT_PendingTask SELECTnew_line_JIRA_ROHIT_PendingTask ']}>
            #array_of_clicks = request.POST.getlist('array_of_clicks[]')
            Sql_codeValues = request.POST.getlist('codeValue_toPy')
            #print("------Sql_codeValues----",Sql_codeValues)
            # CREATE CONN only if VALID SQL Comes Through .......
            import psycopg2
            schema_default_public = "public"
            psql_user = settings.DATABASES['default']['USER']
            password = settings.DATABASES['default']['PASSWORD']
            database_name = settings.DATABASES['default']['NAME']
            conn = psycopg2.connect("dbname="+str(database_name)+" "+"user="+str(psql_user)+" "+"password="+str(password)+"")
            conn_cursor = conn.cursor()
            #
            sql_query_str_mirror = "JIRA_ROHIT_PendingTask_EMPTY"
            if select_table in str(Sql_codeValues):
                #print("SELECT")
                sql_query_str_mirror = "SELECT"
            if astrx in str(Sql_codeValues):
                #print("*") 
                ### FAILS ---- gave it --- SELECT $ FROM ---- it gave me --- SELECT * FROM
                sql_query_str_mirror = "SELECT *"
            if from_table in str(Sql_codeValues):
                #print("FROM")
                sql_query_str_mirror = "SELECT * FROM"
            #print("------sql_query_str_mirror--------",sql_query_str_mirror)
            #    
            #ls_csv_documents = csv_document.objects.get_queryset().order_by('-pk')
            #latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk') 
            latest_dataSetName = temp_dataSetName_for_EDALanding.objects.values_list('dataset_name',flat=True).order_by('-pk') [0:5]
            #### JIRA_ROHIT_PendingTask JIRA_ROHIT_PendingTask --- this Django Model table has --- 1900 Plus Records 
            ## http://localhost:8001/admin/dc_dash/temp_datasetname_for_edalanding/
            # flat=True
            
            latest_dataSetName = list(latest_dataSetName)
            #print(type(latest_dataSetName))
            #print("    "*90)
            #print(len(latest_dataSetName))
            #print("    "*90)
            #
            ##print("---------ls_csv_documents--------",ls_csv_documents)
            #print("    "*90)
            ##print("---------latest_dataSetName------",latest_dataSetName)
            #print("    "*90)
            # conn_cursor.execute("INSERT INTO dc_tableNames_for_merge (temp_tableName, temp_tableName1 , new_merged_tableName) VALUES (%s, %s , NULL)", (str(array_of_clicks[0]), str(array_of_clicks[1])))
            # conn.commit()
            conn.close()
            #
            df_forCodeMirror = pd.DataFrame(latest_dataSetName) ## this doesnt give COL_NAMES 
            df_forCodeMirror.columns = ['tables']
        
            tables_forCodeMirror = json.loads(df_forCodeMirror.to_json(orient='split')) 
            ## If only ERROR == EXCEPT from FUNC == psql_merge_basic
            ## then above line will throw ERROR == data = json.loads(df_table_fromMerge.to_json(orient='split'))
            #AttributeError: 'str' object has no attribute 'to_json
            # dict_json = {}
            # dict_json['tables'] = tables_forCodeMirror
            # #print("---dict_json-----",dict_json)
            # # dict_json['table_one'] = table_one ## This line held on as an example - not used here 
            # dict_json['table_two'] = table_two ## This line held on as an example - not used here 
            ##print("---------------dict_json--------------",dict_json)
            #return JsonResponse(dict_json, safe= False)
            redirect_url = '/dc/test_CodeMirror/' 
            return HttpResponseRedirect(redirect_url)


        

    def psql_tableNames_js_to_py(request):
        """
        AJAX JSON POST Data comes here from -- eda_sibar.html 
        URL to come here -- cell_getJSVal1
        url(r'^cell_getJSVal1/',utily.utily_class.psql_tableNames_js_to_py, name='cell_getJSVal1'), # 
        """
        import psycopg2
        schema_default_public = "public"
        psql_user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        conn = psycopg2.connect("dbname="+str(database_name)+" "+"user="+str(psql_user)+" "+"password="+str(password)+"")
        conn_cursor = conn.cursor()
        #
        if request.method == 'POST':
            ##print(request)
            ##print(request.POST)
            array_of_clicks = request.POST.getlist('array_of_clicks[]')
            if array_of_clicks:
                #print("---------INSIDE == psql_tableNames_js_to_py-------array_of_clicks----",array_of_clicks)
                conn_cursor.execute("INSERT INTO dc_tableNames_for_merge (temp_tableName, temp_tableName1 , new_merged_tableName) VALUES (%s, %s , NULL)", (str(array_of_clicks[0]), str(array_of_clicks[1])))
                conn.commit()
                ### Probably Not An Issue ==>> 
                # Will See in TERMINAL --- Status == 300 or 302 for these URL's == "POST /dc/cell_getJSVal1/ HTTP/1.1" 302 0

            str_new_merged_tableName = request.POST.get('new_merged_tableName')
            if str_new_merged_tableName:
                str_new_merged_tableName = str(str_new_merged_tableName)
                #print("---------INSIDE == psql_tableNames_js_to_py-----str(str_new_merged_tableName)------",str_new_merged_tableName)
                conn_cursor.execute("""UPDATE dc_tableNames_for_merge SET new_merged_tableName = %s WHERE new_merged_tableName is NULL;""",(str_new_merged_tableName,))
                conn.commit()
                ### Probably Not An Issue ==>> 
                # Will See in TERMINAL --- Status == 300 or 302 for these URL's == "POST /dc/cell_getJSVal1/ HTTP/1.1" 302 0
                ### REDIRECT FAILS --- Doing REDIRECT from JavaScript in == eda_sidebar.html >>  window.location = forMergeRedirectURL; >> sql_action_MergeTables.html
                #returnFunc()  ## from .sql_queries_all import *
        #return render(request,'dc_dash/sql_action_MergeTables.html')
        #return redirect('call_merged_table_view') ## REDIRECT to this URL from URLs.py 
        # JIRA_ROHIT_PendingTask --- Also this REDIRECT -- HttpResponseRedirect(redirect_url) --- NOT Used ?? 
        redirect_url = '/dc/call_merged_table_view/' 
        return HttpResponseRedirect(redirect_url)


    def df_afterMerge_toAjax(self):
        import psycopg2
        schema_default_public = "public"
        psql_user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        conn = psycopg2.connect("dbname="+str(database_name)+" "+"user="+str(psql_user)+" "+"password="+str(password)+"")
        conn_cursor = conn.cursor()
        #
        # conn_cursor.execute("""UPDATE dc_tableNames_for_merge SET new_merged_tableName = %s WHERE new_merged_tableName is NULL;""",(str_new_merged_tableName,))
        #         conn.commit()

        conn_cursor.execute("""SELECT id, temp_tablename , temp_tablename1 , new_merged_tablename FROM dc_tableNames_for_merge ORDER BY id DESC LIMIT 1;""")
        psql_db_row_from_fetch_one = conn_cursor.fetchone() #
        # Seems to be OK for now --- the -- fetchone() --- is getting the LAST INSERTED Record. 
        #print("    "*90)
        # #print(type(psql_db_row_from_fetch_one)) ## <class 'tuple'>
        # #print(psql_db_row_from_fetch_one) ## (40, 'psql_db_table_jose_brazil', 'csv_1c', 'tuple')
        # #print("    "*90)
        table_one = str(psql_db_row_from_fetch_one[1])
        #print(table_one)
        table_two = str(psql_db_row_from_fetch_one[2])
        #print(table_two)
        new_merged_tableName = str(psql_db_row_from_fetch_one[3])
        #print(new_merged_tableName)
        #print("    "*90)
        df_table_fromMerge = "dummy STR"

        new_table_name_OR_exception_str = psql_merge_basic(str(table_one),str(table_two),str(new_merged_tableName))
        ##print("-----------new_table_name_OR_exception_str-----------",new_table_name_OR_exception_str)
        type_of_returnValue = str(type(new_table_name_OR_exception_str))
        #print("----------TYPE --------",type_of_returnValue) ## <class 'str'>
        if "str" in type_of_returnValue:
            print("-----ERROR == EXCEPT from FUNC == psql_merge_basic---------------",new_table_name_OR_exception_str)
        else:
            df_table_fromMerge = new_table_name_OR_exception_str    
        #print("    "*90)
        #
        data = json.loads(df_table_fromMerge.to_json(orient='split')) 
        ## If only ERROR == EXCEPT from FUNC == psql_merge_basic
        ## then above line will throw ERROR == data = json.loads(df_table_fromMerge.to_json(orient='split'))
        #AttributeError: 'str' object has no attribute 'to_json
        dict_json = {}
        dict_json['data_json'] = data
        dict_json['table_one'] = table_one
        dict_json['table_two'] = table_two
        dict_json['new_merged_tableName'] = new_merged_tableName

        ##print("---------------dict_json--------------",dict_json)
        return JsonResponse(dict_json, safe= False)






    def df_afterMerge_toAjax_Old(self): # TBD == new_merged_tableName
        """
        # JIRA_ROHIT_PendingTask Went to -- df_afterMerge_toAjax
        # JIRA_ROHIT_PendingTask Getting Values from 2 Diff Records of Django Queryset
        # --- Dont clean this code here below --- keep it documented 
        """
        # get temp_tableName ---- from == temp_tableName_forMerge
        #table_one = temp_tableName_forMerge.objects.all().values('temp_tableName').order_by('-pk')[0:1]
        #table_one = temp_tableName_forMerge.objects.values('temp_tableName').order_by('-pk')[0:1]
        # Above Gives == <QuerySet [{'temp_tableName': 'psql_db_table_jose_brazil'}]>
        table_one = temp_tableName_forMerge.objects.values_list('temp_tableName').order_by('-pk')[0:1]
        # flat=True
        #print("-------table_one--------",table_one) #NOT -- OK -- <QuerySet [('',)]>
        table_one = table_one[0] ### QuerySet to TUPLE's - 1st-value. 
        table_one = str(table_one[0]) #TUPLE's - 1st-value - as STR. 
        #print("-------table_one---111-----",table_one) #OK

        
        #table_two = temp_tableName_forMerge.objects.all().values('temp_tableName1').order_by('-pk')[0:1]
        #table_two = temp_tableName_forMerge.objects.values('temp_tableName1').order_by('-pk')[0:1]
        #table_two = temp_tableName_forMerge.objects.values_list('temp_tableName1').order_by('-pk')[0:1]
        table_two = temp_tableName_forMerge.objects.values_list('temp_tableName1').order_by('-pk')[0:1]
        #print("--table_two--------",table_two) # NOT--OK 
        #table_two = table_two[0] ## Here this ==>> ##print(type(table_two)) ## TUPLE
        table_two = table_two[0] ## QuerySet to TUPLE's - 1st-value. 
        table_two = str(table_two[0]) ##TUPLE's - 1st-value - as STR. 
        #print("--table_two---111-----",table_two) # OK 

        new_merged_tableName = temp_tableName_forMerge.objects.values_list('new_merged_tableName').order_by('-pk')[0:1]
        #print("-MIGHT BE BLANK QUERYSET ========= ",new_merged_tableName) # <QuerySet [('nopy1',)]> # <class 'django.db.models.query.QuerySet'>
        new_merged_tableName = new_merged_tableName[0] ## QuerySet to TUPLE's - 1st-value. 
        new_merged_tableName = str(new_merged_tableName[0]) ##TUPLE's - 1st-value - as STR. 
        #print("-MIGHT BE BLANK STR ========= ",new_merged_tableName)
        #print("     "*90)
        #
       
        new_table_name_OR_exception_str = psql_merge_basic(str(table_one),str(table_two),str(new_merged_tableName))
        #print("-----------new_table_name_OR_exception_str================",new_table_name_OR_exception_str)
        #print("     "*90)
        #
        
        #### Testing ---- OK below Line ...
        #df_new_table_name = psql_merge_basic(str(array_of_clicks[0]),str(array_of_clicks[1]))
        
        ##print("---call a FUNC here which takes ==-df_table_fromMerge---which is a DF and makes a JSON for AJAX----UTILyyy__",df_table_fromMerge)
        #print("    "*90)

        # df_table_fromMerge

        #dict_json = df_afterMerge_toAjax(df_table_fromMerge)

        data = json.loads(df_table_fromMerge.to_json(orient='split')) 
        ## If only ERROR == EXCEPT from FUNC == psql_merge_basic
        ## then above line will throw ERROR == data = json.loads(df_table_fromMerge.to_json(orient='split'))
        #AttributeError: 'str' object has no attribute 'to_json

        dict_json = {}
        dict_json['data_json'] = data
        #print(dict_json)
        # #print("  "*90)
        return JsonResponse(dict_json, safe= False)

    def psql_tableNames_from_py(self): ## JIRA_ROHIT_PendingTask 
        #ls_csv_documents = csv_document.objects.get_queryset().order_by('-pk')   
        #qs_counter_for_dfFromEDA = csv_document.objects.all().values('counter_for_dfFromEDA').order_by('-pk')
        queryset = csv_document.objects.values_list()
        df_psqlTableNames = pd.DataFrame(list(queryset)) ## this doesnt give COL_NAMES 
        # It gives COL_NAMES as - 0 , 1 , 2, 3 etc INTEGERS --- which isnt ok with dataTables.js
        df_psqlTableNames.columns = ['DataSet_PrimaryKey_ID','CSV_Uploaded_Name', 'CSV_File_GivenName','DataSet_Name','Created_Time','DataSet_UniqueID']
        data = json.loads(df_psqlTableNames.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        return JsonResponse(dict_json, safe= False)


    
    def eda_get_value_from_js(request):
        """
        ### USE This to get COL_INDEX for all EDA - JS to PY Column Clicks 
        JIRA_ROHIT_PendingTask_laterz --- create individual Columns within this DB for all the EDA Methods >>>
        - 1 for Emails-ColIndex , 2 - Fuzzy_ColIndex etc
        
        JIRA_ROHIT_PendingTask laterz --- create within this method - check for different text values within the >>>
        col_num_formatchSimilarText = request.POST.get('col_num_formatchSimilarText')
        col_num_forEmailparts = request.POST.get('col_num_forEmailparts')
        col_num_forFuzzySomeJIRA_ROHIT_PendingTask = request.POST.get('col_num_forFuzzySomeJIRA_ROHIT_PendingTask')

        """
        if request.method == 'POST':
            ##print("=====FILE---UTILY...In here === def eda_get_value_from_js(request):====")
            ##print("      ***        "*200)
            col_num = request.POST.get('col_num')
            ##print("----FILE===Utily.PY---eda_get_value_from_js---col_num-----------",col_num)
            ##print("      ***        "*200)
            if col_num != None:
                model = temp_colIndex_for_Eda()
                ### JIRA_ROHIT_PendingTask --- this Model / Django DB needs to be Deleted on some set time interval = to FLUSH Garbagae COL Indexes
                model.column_index_from_dataTables_js = str(col_num)
                model.save()
        return render(request,'dc_dash/eda_sidebar.html')

    def renderPage_extractEmailPart(request):
        if request.method == 'POST':
            #print("========GOT POST =====AAAA=======")
            #print("                "*90)
            emailPartsButtonClicked = request.POST.get('emailPartsButtonClicked')
            #print("========GOT POST ======baloney====AAAAAAA==",emailPartsButtonClicked)
            #print("                "*90)

        #/templates/dc_dash/eda_action_ExtractEmailParts.html
        return render(request,'dc_dash/eda_action_ExtractEmailParts.html')

    def extractEmailPart_outPut(request):
        #
        # call == def eda_ExtractEmailParts(self): === from CLASS == utility_eda_only_class
        utility_eda_only_obj = utility_eda_only_class() #
        df_emailParts = utility_eda_only_obj.eda_ExtractEmailParts()#
        data = json.loads(df_emailParts.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        #print("=======dict_json=============",dict_json)
        #print("                "*90)

        return JsonResponse(dict_json, safe= False)



    def modal_psqlDB_Conn_Status(self):
        df_for_pg_stat_activity = psql_liveConn_Status()
        data = json.loads(df_for_pg_stat_activity.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        return JsonResponse(dict_json, safe= False)

    def modal_data_summary_stats(self):
        """
        Method gets called in file >> nginx_demo_django/dc_dash/templates/dc_dash/includes/modal_summary_stats.html
        modal in SideBar = modal_data_summary_stats
        Actual path to method = nginx_demo_django/dc_dash/utily.py
        Js Code >> var mySummaryUrl = "{% url 'call_modal_data_summary_stats' %}" 
        
        JIRA_ROHIT_PendingTask_JIRA_ROHIT ==>> CHANGE THIS ....get last created DataSet the _bump1 ... show Summary of Last Modified version of DataSEt
        As of Now gets dataSet from EDA dataSets when INIT Created == DataSetName from - temp_dataSetName_for_EDALanding
        ..Summary to be SHOWN for Last Version of EDA DATASET with all changes done till then ...
        
        """
        from sqlalchemy import create_engine
        from .dc_eda_funcs import eda_modal_summary_stats
        
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
        #limit_records = 1500 ## DONT LIMIT as its EDA SUMMARY - All Records required 
        #
        
        latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        myDict_dataSetName = latest_dataSetName[0]
        for keys , values in myDict_dataSetName.items():
            if "dataset_name" in keys:
                dataset_name = str(values)

        # Not using Latest COLUMN Index - as we do SUMMARY STATS for Complete DF
        # latest_colIndex = temp_colIndex_for_Eda.objects.all().values('column_index_from_dataTables_js').order_by('-pk')[0:1]
        # myDict_colIndex = latest_colIndex[0]
        # for keys , values in myDict_colIndex.items():
        #     if "column_index_from_dataTables_js" in keys:
        #         column_index = str(values)
        
        #sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(dataset_name),str(limit_records))
        sql_command = "SELECT * FROM {}.{} ;".format(str(schema_default_public), str(dataset_name))
        df_for_summaryStats = pd.read_sql(sql_command,engine)
        summaryStats_df = eda_modal_summary_stats(df_for_summaryStats)
        data = json.loads(summaryStats_df.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        return JsonResponse(dict_json, safe= False)


    def eda_initList_display(self):
        """
        This was to get == get_absolute_url() == for Clicking and EDA>>GO Link Abs url to be passed further ... 
        ## 03AUG19 --- Code Audit == This Method is Not being used = Parked in HTML Template = dc_dash/templates/dc_dash/eda_dataset_name_listView_older.html
        # JIRA_ROHIT_PendingTask Ok this works -- basis my own SO question .
        Can get -- get_absolute_url , from the Model. 
        Now can make a DF and send to DataTables.js as JSON if required . 
        Right now --- this URL to be hit to test this FUNCTION == http://localhost:8000/dc/eda_initList_display/
        """
        
        #ls_csv_documents = csv_document.objects.get_queryset().order_by('-pk')  

        queryset = csv_document.objects.values_list()
        #queryset_2 = csv_document.objects.get_absolute_url()
        #call_eda_landing_view
        #queryset_2 = csv_document.objects.call_eda_landing_view()
        #.get(pk=1)
        #queryset_2 = csv_document.objects.get(.order_by('-pk')[0:1])
        #.get_queryset().order_by('-pk')
        queryset_2 = csv_document.objects.get_queryset().order_by('-pk')
        #
        myModel_instance = csv_document.objects.get(pk=164) ## This PK here is just hardcoded to check the SO Code .
        #print(myModel_instance)
        #print(myModel_instance.get_absolute_url())

        ##print(queryset_2)
        #print("     "*90)

        df_psqlTableNames = pd.DataFrame(list(queryset)) ## this doesnt give COL_NAMES 
        df_psqlTableNames.columns = ['DataSet_PrimaryKey_ID','CSV_Uploaded_Name', 'CSV_File_GivenName','DataSet_Name','Created_Time','DataSet_UniqueID']

        data = json.loads(df_psqlTableNames.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        return JsonResponse(dict_json, safe= False)



    def eda_landing_init_dataTable(self):  
        from sqlalchemy import create_engine
        ## READ the DataSetName from the MODEL == temp_dataSetName_for_EDALanding
        ## This will FAIL if EVEN ONE USER -- creates more than 1 EDA Page with TWO DIFFERENT DATASETS ??
        ### JIRA_ROHIT_PendingTask --- This is why the guys had used REST API Calls with USER ID and DATA SET ID's etc etc ....
        #time.sleep(3)

        latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        myDict = latest_dataSetName[0]
        ls_data_set_name = []
        for keys , values in myDict.items():
            if "dataset_name" in keys:
                ls_data_set_name.append(str(values))
                dataSetName = str(ls_data_set_name[0])
                ##print("------UTILY.py------dataSetName---------AAAAAAAAAAAAAAAAAA================------",dataSetName)
                ##print("   "*90)

        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        # All Above - are FIXED Values coming in from Settings.py
        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name,
        )
        engine = create_engine(database_url, echo=False)
        schema_default_public = "public"
        limit_records = 1500 ## EDA --- JIRA_ROHIT_PendingTask CHANGE 
        sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(dataSetName),str(limit_records))
        df_for_eda = pd.read_sql(sql_command,engine)
        ##print("------UTILY.py----eda_landing_init_dataTable(self)----------df_for_eda-------------",df_for_eda)
        ##print("     "*90)

        data = json.loads(df_for_eda.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        ##print("------UTILY.py----eda_landing_init_dataTable(self)----------dict_json=-------------",dict_json)
        ##print("     "*90)
        
        return JsonResponse(dict_json, safe= False)
    

    def eda_SearchAndReplace_formSave(request):
        """
        PARAMS from FORM ,besides == dataset_name and COL_NUM 
        Save FORM to MODEL - render HTML Page in which AJAX URL Call embeded. 
        """
        if request.method == 'POST':
            ### class eda_form(forms.ModelForm):
            eda_form_valid = eda_form(request.POST)
            if eda_form_valid.is_valid():
                """
                Done get DataSetName from Above FORM --- 
                get it from the DB in which we save when Landing on the INIT EDA_DataSets
                """
                # latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
                # myDict = latest_dataSetName[0]
                # ls_data_set_name = []
                # for keys , values in myDict.items():
                #     if "dataset_name" in keys:
                #         ls_data_set_name.append(str(values))
                #         dataset_name = str(ls_data_set_name[0]) ### THIS == dataset_name --- Not used anywhere ?? 
                #         ##print("--------------dataset_name--------------FROM UTILY to be passed to Django Template TAG --------",dataset_name)
                
                # form_input_new_column = eda_form_valid.cleaned_data['form_input_new_column']
                # #getting COLUMN INDEX from DataTables.js
                # django_form_input_operation_type = eda_form_valid.cleaned_data['django_form_input_operation_type']
                # str_search = eda_form_valid.cleaned_data['str_search']
                # str_replace = eda_form_valid.cleaned_data['str_replace'] ### JIRA_ROHIT_PendingTask --- Why are we getting these values ???
                eda_form_valid_object = eda_form_valid.save() #
                # JIRA_ROHIT_PendingTask --- Why cant we just save this FORM on TOP ??
                ### Testing DHANKAR --- 21MAY19 ---OK --- 
                # Form Fields Saved == http://localhost:8000/admin/dc_dash/eda_inputs_search_and_replace/186/change/

                context = {
                    'dataSetName': "DataSetName_Test"
                }

        return render(request,'dc_dash/eda_action_SearchAndReplace.html',context)



    def eda_ChangetoUpper_outPut(self):  
        """
        AVIRUP_CHATTARAJ - Apr2020
        #
        EDA_Action_Search and eda_ChangetoUpper --JSON Data >> AJAX in template
        """
        from sqlalchemy import create_engine
        from .dc_eda_funcs import save_postEdaDataSet
        from .eda_apr_20 import change_to_upper 

        latest_SearchParams = eda_inputs_search_and_replace.objects.all().values('dataset_name','form_input_new_column','column_name','django_form_input_operation_type','str_search','str_replace').order_by('-pk')[0:1]
        myDict = latest_SearchParams[0]
        for keys , values in myDict.items():
            if "form_input_new_column" in keys:
                new_column = str(values)
            if "django_form_input_operation_type" in keys:
                operation_type = str(values)
            if "str_search" in keys:
                str_search = str(values)
            if "str_replace" in keys:
                str_replace = str(values)
        
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
        limit_records = 1500 ## as its EDA 
        #
        qs_counter_for_dfFromEDA = temp_dataSetName_dfFromEDA.objects.all().values('counter_for_dfFromEDA').order_by('-pk')[0:1]
        #print("------QUERY SET--SEARCH_andREPLACE--qs_counter_for_dfFromEDA------------",qs_counter_for_dfFromEDA)
        ### First RUN ==  EMPTY QUERYSET -- as NO VALUES for COUNTER == <QuerySet []>
        ### Second RUN ==  <QuerySet [{'counter_for_dfFromEDA': 1}]>

        ## Testing_21MAY19
        #### JIRA_ROHIT_PendingTask Below Commented Out --- as seems have Disabled the DELETE / CREATE for temp data Sets 
        ## Testing_21MAY19



        # if qs_counter_for_dfFromEDA.exists():
        #     ## We are NOT in FIRST RUN ..
        #     myDict_counter = qs_counter_for_dfFromEDA[0]
        #     for keys , values in myDict_counter.items():
        #         if "counter_for_dfFromEDA" in keys:
        #             latest_counter_for_dfFromEDA = int(values)
        #     if latest_counter_for_dfFromEDA > 0: ## THIS will Always be TRUE HERE --- as above we Checked for NOT IN FIRST RUN ...
        #         ##print("---------GOT COUNTER > 0  latest_counter_for_dfFromEDA======",latest_counter_for_dfFromEDA)
        #         latest_dataSetName = temp_dataSetName_dfFromEDA.objects.all().values('temp_dataset_name').order_by('-pk')[0:1]
        #         myDict_dataSetName = latest_dataSetName[0]
        #         for keys , values in myDict_dataSetName.items():
        #             if "temp_dataset_name" in keys:
        #                 dataset_name = str(values)
        #                 #print("--NOT FIRST RUN as --latest_counter_for_dfFromEDA > 0 --- dataset_name---",dataset_name)
        # else:
        """
        DataSetName from - temp_dataSetName_for_EDALanding
        """
        latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        myDict_dataSetName = latest_dataSetName[0]
        for keys , values in myDict_dataSetName.items():
            if "dataset_name" in keys:
                dataset_name = str(values)
                #print("FIRST RUN OF DATA SET ___dataset_name_______",dataset_name)
                #print("     "*90)

        latest_colIndex = temp_colIndex_for_Eda.objects.all().values('column_index_from_dataTables_js').order_by('-pk')[0:1]
        if latest_colIndex.exists():
            #print("----------GOT a COL INDEX -----------JIRA_ROHIT_PendingTask get query SET Exists Check here -----")
            myDict_colIndex = latest_colIndex[0]
            for keys , values in myDict_colIndex.items():
                if "column_index_from_dataTables_js" in keys:
                    column_index = str(values)
        else:
            #print("---FROM UTILY.py NO COL INDEX YET ---------") #
            column_index = int(3)
            # JIRA_ROHIT_PendingTask Hardcoded below == column_index = int(3)
            # If USER has Not Clicked on a  COLUMN to Pass in JS >> latest_colIndex 
            # Just use default COLUMN_Index == 3 
            # This needs a JavaScript_WARNING - JavaScript_ALERT on the FRONT END. 
            

        ## JIRA_ROHIT_PendingTask earlier ERROR -- PSQL couldnt find ACTUAL TABLE with == dataset_name in PSQL ...due to Mixed Fonts.
        sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(dataset_name),str(limit_records))
        df_for_eda = pd.read_sql(sql_command,engine)
        df_from_eda , new_col_name = searchAndReplace(df_for_eda,new_column,column_index,operation_type,str_search,str_replace) ## Order of PARAM's IMPORTANT
        data = json.loads(df_from_eda.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        #
        counter_for_dfFromEDA = 0
        temp_dataset_name = save_postEdaDataSet(df_from_eda,dataset_name) 
        ## To Show == temp_dataset_name -- In the FrontEnd HTML without the trailing _n_n_n_ etc .
        ## We need not show these --- trailing _n_n_n_ etc , in the TEMPLATE 
        ## The == temp_dataset_name -- has the trailing _n_n_n_ appended as we need it for creating New PSQL Tables 
        temp_dataset_name = str(temp_dataset_name).strip("_n_")
        #print("------Stripped _n_----temp_dataset_name------------",temp_dataset_name)
        #print("      "*90)

        dict_json['temp_dataset_name'] = str(temp_dataset_name) ## _##_JIRA_ROHIT_PendingTask
        #new_col_name --- returned from EDA Action Func Above ...
        dict_json['new_col_name'] = str(new_col_name) ## _##_JIRA_ROHIT_PendingTask

        ## New dataSet created post EDA Action 
        # Saved in PSQL with NAME == temp_dataset_name
        #print("------UTILY---Sent to TEMPLATE FrontEnd ---dict_json['temp_dataset_name']----",temp_dataset_name)
        if temp_dataset_name != None:
            counter_for_dfFromEDA += 1
        model = temp_dataSetName_dfFromEDA()
        model.counter_for_dfFromEDA = int(counter_for_dfFromEDA)
        model.temp_dataset_name = str(temp_dataset_name)
        model.save()
       
        return JsonResponse(dict_json, safe= False)
        

    def eda_SearchAndReplace_outPut(self):  
        """
        EDA_Action_Search and Replace_Final JSON Data to AJAX in template
        """
        from sqlalchemy import create_engine
        from .dc_eda_funcs import searchAndReplace , save_postEdaDataSet

        latest_SearchParams = eda_inputs_search_and_replace.objects.all().values('dataset_name','form_input_new_column','column_name','django_form_input_operation_type','str_search','str_replace').order_by('-pk')[0:1]
        myDict = latest_SearchParams[0]
        for keys , values in myDict.items():
            if "form_input_new_column" in keys:
                new_column = str(values)
            if "django_form_input_operation_type" in keys:
                operation_type = str(values)
            if "str_search" in keys:
                str_search = str(values)
            if "str_replace" in keys:
                str_replace = str(values)
        
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
        limit_records = 1500 ## as its EDA 
        #
        qs_counter_for_dfFromEDA = temp_dataSetName_dfFromEDA.objects.all().values('counter_for_dfFromEDA').order_by('-pk')[0:1]
        #print("------QUERY SET--SEARCH_andREPLACE--qs_counter_for_dfFromEDA------------",qs_counter_for_dfFromEDA)
        ### First RUN ==  EMPTY QUERYSET -- as NO VALUES for COUNTER == <QuerySet []>
        ### Second RUN ==  <QuerySet [{'counter_for_dfFromEDA': 1}]>

        ## Testing_21MAY19
        #### JIRA_ROHIT_PendingTask Below Commented Out --- as seems have Disabled the DELETE / CREATE for temp data Sets 
        ## Testing_21MAY19



        # if qs_counter_for_dfFromEDA.exists():
        #     ## We are NOT in FIRST RUN ..
        #     myDict_counter = qs_counter_for_dfFromEDA[0]
        #     for keys , values in myDict_counter.items():
        #         if "counter_for_dfFromEDA" in keys:
        #             latest_counter_for_dfFromEDA = int(values)
        #     if latest_counter_for_dfFromEDA > 0: ## THIS will Always be TRUE HERE --- as above we Checked for NOT IN FIRST RUN ...
        #         ##print("---------GOT COUNTER > 0  latest_counter_for_dfFromEDA======",latest_counter_for_dfFromEDA)
        #         latest_dataSetName = temp_dataSetName_dfFromEDA.objects.all().values('temp_dataset_name').order_by('-pk')[0:1]
        #         myDict_dataSetName = latest_dataSetName[0]
        #         for keys , values in myDict_dataSetName.items():
        #             if "temp_dataset_name" in keys:
        #                 dataset_name = str(values)
        #                 #print("--NOT FIRST RUN as --latest_counter_for_dfFromEDA > 0 --- dataset_name---",dataset_name)
        # else:
        """
        DataSetName from - temp_dataSetName_for_EDALanding
        """
        latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        myDict_dataSetName = latest_dataSetName[0]
        for keys , values in myDict_dataSetName.items():
            if "dataset_name" in keys:
                dataset_name = str(values)
                #print("FIRST RUN OF DATA SET ___dataset_name_______",dataset_name)
                #print("     "*90)

        latest_colIndex = temp_colIndex_for_Eda.objects.all().values('column_index_from_dataTables_js').order_by('-pk')[0:1]
        if latest_colIndex.exists():
            #print("----------GOT a COL INDEX -----------JIRA_ROHIT_PendingTask get query SET Exists Check here -----")
            myDict_colIndex = latest_colIndex[0]
            for keys , values in myDict_colIndex.items():
                if "column_index_from_dataTables_js" in keys:
                    column_index = str(values)
        else:
            #print("---FROM UTILY.py NO COL INDEX YET ---------") #
            column_index = int(3)
            # JIRA_ROHIT_PendingTask Hardcoded below == column_index = int(3)
            # If USER has Not Clicked on a  COLUMN to Pass in JS >> latest_colIndex 
            # Just use default COLUMN_Index == 3 
            # This needs a JavaScript_WARNING - JavaScript_ALERT on the FRONT END. 
            

        ## JIRA_ROHIT_PendingTask earlier ERROR -- PSQL couldnt find ACTUAL TABLE with == dataset_name in PSQL ...due to Mixed Fonts.
        sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(dataset_name),str(limit_records))
        df_for_eda = pd.read_sql(sql_command,engine)
        df_from_eda , new_col_name = searchAndReplace(df_for_eda,new_column,column_index,operation_type,str_search,str_replace) ## Order of PARAM's IMPORTANT
        data = json.loads(df_from_eda.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        #
        counter_for_dfFromEDA = 0
        temp_dataset_name = save_postEdaDataSet(df_from_eda,dataset_name) 
        ## To Show == temp_dataset_name -- In the FrontEnd HTML without the trailing _n_n_n_ etc .
        ## We need not show these --- trailing _n_n_n_ etc , in the TEMPLATE 
        ## The == temp_dataset_name -- has the trailing _n_n_n_ appended as we need it for creating New PSQL Tables 
        temp_dataset_name = str(temp_dataset_name).strip("_n_")
        #print("------Stripped _n_----temp_dataset_name------------",temp_dataset_name)
        #print("      "*90)

        dict_json['temp_dataset_name'] = str(temp_dataset_name) ## _##_JIRA_ROHIT_PendingTask
        #new_col_name --- returned from EDA Action Func Above ...
        dict_json['new_col_name'] = str(new_col_name) ## _##_JIRA_ROHIT_PendingTask

        ## New dataSet created post EDA Action 
        # Saved in PSQL with NAME == temp_dataset_name
        #print("------UTILY---Sent to TEMPLATE FrontEnd ---dict_json['temp_dataset_name']----",temp_dataset_name)
        if temp_dataset_name != None:
            counter_for_dfFromEDA += 1
        model = temp_dataSetName_dfFromEDA()
        model.counter_for_dfFromEDA = int(counter_for_dfFromEDA)
        model.temp_dataset_name = str(temp_dataset_name)
        model.save()
       
        return JsonResponse(dict_json, safe= False)

    def eda_createDuplicate_Col(request):
        """
        File = Utily_EDAOnly.py 
        """
        if request.method == 'POST':
            oldColIndex = request.POST.get('oldColIndex')
            #print("----------oldColIndex----------",oldColIndex)
            if oldColIndex != None:
                """
                DataSetName from - temp_dataSetName_for_EDALanding
                """
                latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
                myDict_dataSetName = latest_dataSetName[0]
                for keys , values in myDict_dataSetName.items():
                    if "dataset_name" in keys:
                        dataset_name = str(values)
                        #print("__==def eda_createDuplicate_Col(request):_________dataset_name_______",dataset_name)
                        #print("                  "*90)

                # get Current DF 
                #call FUNC == createDuplicate_Col

                # model = temp_colIndex_for_Eda()
                # model.column_index_from_dataTables_js = str(col_num)
                # model.save()

        return render(request,'dc_dash/eda_sidebar.html')



    def eda_MatchSimilarText_renderPage(request):

        # if request.method == 'POST':
        #     #
        #     button_clixx_status = request.POST.get('button_clixx_status')
        #     #print("----------oldColIndex----------",button_clixx_status)
        #     if button_clixx_status != None:
        #         #
        return render(request,'dc_dash/eda_action_MatchSimilarText_Fuzz.html') ## JIRA_ROHIT_PendingTask --- earlier Now Changed - AUG 19



    def eda_MatchSimilarText_formSave(request):
        """
        PARAMS from FORM ,besides == dataset_name and COL_NUM 
        Save FORM to MODEL - render HTML Page in which AJAX URL Call embeded. 
        """
        if request.method == 'POST':
            eda_MatchSimilarText_form_valid = eda_MatchSimilarText_form(request.POST)
            if eda_MatchSimilarText_form_valid.is_valid():
                latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
                myDict = latest_dataSetName[0]
                ls_data_set_name = []
                for keys , values in myDict.items():
                    if "dataset_name" in keys:
                        ls_data_set_name.append(str(values))
                        dataset_name = str(ls_data_set_name[0])
                fuzziness = eda_MatchSimilarText_form_valid.cleaned_data['fuzziness']
                str_to_compare_with = eda_MatchSimilarText_form_valid.cleaned_data['str_to_compare_with']
                
                eda_MatchSimilarText_form_valid_object = eda_MatchSimilarText_form_valid.save() #
                #eda_MatchSimilarText_renderPage()
                #What are we doig with this OBJECT ?? Will the FORM save if we dont CREATE OBJECT ?? YES ?? 
        #return render(request,'dc_dash/eda_action_MatchSimilarText_Fuzz.html') ## JIRA_ROHIT_PendingTask --- earlier Now Changed - AUG 19
        return render(request,'dc_dash/includes/modal_EDA_Col_Actions.html')
    

    def eda_MatchSimilarText_outPut(self):   ## JIRA_ROHIT_PendingTask
        """
        #BUGGY CODE  ---commented out with  #JIRA_ROHIT_PendingTask== 
        """
        from sqlalchemy import create_engine
        from .dc_eda_funcs import matchSimilarText , save_postEdaDataSet

        latest_MatchSimilarText = eda_inputs_MatchSimilarText.objects.all().values('fuzziness','str_to_compare_with').order_by('-pk')[0:1]
        myDict = latest_MatchSimilarText[0]
        for keys , values in myDict.items():
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
        limit_records = 1500 ## as its EDA 
        
        #latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
        qs_counter_for_dfFromEDA = temp_dataSetName_dfFromEDA.objects.all().values('counter_for_dfFromEDA').order_by('-pk')[0:1]

        #JIRA_ROHIT_PendingTask== qs_counter_for_dfFromEDA = temp_dataSetName_dfFromEDA.objects.all().values('counter_for_dfFromEDA').order_by('-pk')[0:1]
        #JIRA_ROHIT_PendingTask== #print("------QUERY SET----qs_counter_for_dfFromEDA------------",qs_counter_for_dfFromEDA)
        ### First RUN Above shall be an EMPTY QUERYSET --- as NO VALUES for COUNTER == <QuerySet []>
        if qs_counter_for_dfFromEDA.exists():
            ## We are NOT in FIRST RUN ..
            myDict_counter = qs_counter_for_dfFromEDA[0]
            for keys , values in myDict_counter.items():
                if "counter_for_dfFromEDA" in keys:
                    latest_counter_for_dfFromEDA = int(values)
            if latest_counter_for_dfFromEDA > 0: ## THIS will Always be TRUE HERE --- as above we Checked for NOT IN FIRST RUN ...
                #print("---------GOT COUNTER > 0  latest_counter_for_dfFromEDA======",latest_counter_for_dfFromEDA)

                latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
                #print("=====FOR TESTING -- 06 AUG === ",latest_dataSetName) #
                #ABOVE OK Gets CurrentEDA Chosen EDA>>GO ... Not required to be last CSV Uploaded 
                ### JIRA_ROHIT_PendingTask == Below earlier Code Incorrect will only Work if ??? latest_dataSetName === is the DataSet created by LATEST CSV IMPORT ??
                #JIRA_ROHIT_PendingTask== latest_dataSetName = temp_dataSetName_dfFromEDA.objects.all().values('temp_dataset_name').order_by('-pk')[0:1]
                myDict_dataSetName = latest_dataSetName[0]
                for keys , values in myDict_dataSetName.items():
                    if "dataset_name" in keys: ## JIRA_ROHIT_PendingTask Corrected == earlier had == temp_dataset_name
                        dataset_name = str(values)
                        #print("----FILE==UTILY.py--latest_dataSetName = temp_dataSetName_for_EDALanding--dataset_name-------------",dataset_name)
                        #print("              JIRA_ROHIT_PendingTask======")
        else:
            #print("FIRST RUN OF DATA SET __________")
            #print("     "*90)
            ##print("---------GOT COUNTER == 0  latest_counter_for_dfFromEDA======",latest_counter_for_dfFromEDA)    
        
            latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('dataset_name').order_by('-pk')[0:1]
            myDict_dataSetName = latest_dataSetName[0]
            for keys , values in myDict_dataSetName.items():
                if "dataset_name" in keys:
                    dataset_name = str(values)
                    ##print("--------dataset_name-------------",dataset_name)


        #### JIRA_ROHIT_PendingTask----This here DOES NOT Give CORRECT COL INDEX == column_index_from_dataTables_js
        # THIS == temp_colIndex_for_Eda === gets saved in DJANGO MODEL ABOVE in FUNC == eda_get_value_from_js(request):

        latest_colIndex = temp_colIndex_for_Eda.objects.all().values('column_index_from_dataTables_js').order_by('-pk')[0:1]
        if latest_colIndex.exists():
        #this above Django QuerySet Exists:
            myDict_colIndex = latest_colIndex[0]
            for keys , values in myDict_colIndex.items():
                if "column_index_from_dataTables_js" in keys:
                    column_index = str(values)
                    #print("----FILE==Utily.py === def eda_MatchSimilarText_outPut(self): --GOT COL INDEX ---WHY THIS COMMENT == JIRA_ROHIT_PendingTask get query SET Exists Check here??? -----",column_index)
                    #print("              "*90)

        else:
            #print("---FROM UTILY.py NO COL INDEX YET ---------") #
            column_index = int(3)
            # JIRA_ROHIT_PendingTask Hardcoded below == column_index = int(3)
            # If USER has Not Clicked ona  COLUMN to Pass in JS >> latest_colIndex 
            # Just use default COLUMN_Index == 3 
            # This needs a JavaScript_WARNING - JavaScript_ALERT on the FRONT END. 
            

        sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(dataset_name),str(limit_records))
        df_for_eda = pd.read_sql(sql_command,engine)
        #print("======FROM UTILY.py=====df_for_eda===AAA==",df_for_eda) ## JIRA_ROHIT_PendingTask____NOT OK 
        #print("              "*90)

        df_from_eda = matchSimilarText(df_for_eda,fuzziness,str_to_compare_with,column_index) #
        #print("======FROM UTILY.py=====df_from_eda===BBB==",df_from_eda)
        #print("              "*90)

        data = json.loads(df_from_eda.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        #print("========FILE==UTILY.py==dict_json===========",dict_json)
        #print("              "*90)


        
        ##### JIRA_ROHIT_PendingTask == 06AUG19 --- All this below here CHECK ...
        counter_for_dfFromEDA = 0
        temp_dataset_name = save_postEdaDataSet(df_from_eda,dataset_name) ## JIRA_ROHIT_PendingTask
        #func-delete_temp_dataSets(temp_dataset_name) ## Some kind of delayed Delete of temp DataSets 
        #print("---FILE==UTILY.py--TBD---Send to TEMPLATE FrontEnd --- temp_dataset_name----",temp_dataset_name)
        if temp_dataset_name != None:
            counter_for_dfFromEDA += 1
        model = temp_dataSetName_dfFromEDA()
        model.counter_for_dfFromEDA = int(counter_for_dfFromEDA)
        model.temp_dataset_name = str(temp_dataset_name)
        model.save()
        
        return JsonResponse(dict_json, safe= False)













    ### 
    from pandas.api.types import is_string_dtype
    from pandas.api.types import is_numeric_dtype
    import psycopg2
    import io , os 

    def csv_to_psql(request):
        """
        copy_from - psql 
        Not very clear - where the CSV actual FILE is hitting the = form_csv_up_csv_to_psql(request.POST, request.FILES)
        Is it the ,PARAM == request.FILES -- in line above ?? 
        """
        import datetime
        # dt_now = str(datetime.datetime.now())
        dt_all_now = datetime.datetime.now()
        # minute_now = dt_all_now.minute

        if request.method == 'POST':
            print("--------In here -----AAAAAAAAAA")
            form_csv_to_psql = form_csv_up_csv_to_psql(request.POST, request.FILES)
            if form_csv_to_psql.is_valid():
                csv_file_name = form_csv_to_psql.cleaned_data['csv_file_name']
                dataset_name = form_csv_to_psql.cleaned_data['dataset_name'] #
                ## THIS -- dataset_name -- SAVED in MODEL == csv_document 
                # # Using-in Views.py-for_eda_dataset_name_listView-- as INIT Name to call DATASET for EDA. 
                dataset_name = str(dataset_name).lower()
                new_table_name = str(dataset_name)
                ## Forced to LOWER as PSQL saves it as LOWER 
                ## but in certain SqlAlchemy ERRORS etc they will show it as UPPER or even MIXED CASE 
                ## SOURCE -- SO -- https://stackoverflow.com/questions/695289/cannot-simply-use-postgresql-table-name-relation-does-not-exist

                csv_to_psql_object = form_csv_to_psql.save(commit=False)
                csv_to_psql_object.unq_id_nameField = str(csv_file_name) + "aacc" + str(dataset_name) + "aacc" + str(dt_all_now.minute) ## JIRA_ROHIT_PendingTask
                ## SOURCE - SO --- DANIEL ROSEMAN Answer -- https://stackoverflow.com/questions/17126983/add-data-to-modelform-object-before-saving
                csv_to_psql_object.save()         #obj_utily.model_from_csv(csv_object,dataset_name) # ### Original path for EXCEL File to Model etc. 
                from .models import csv_document  # CANT do ASTERIX == * import within a DEFINED Function. 
                MEDIA_ROOT = settings.MEDIA_ROOT  # Reading-path_to_csv_file() #already have CSV saved in MEDIA_ROOT 
                path_csv_for_psql = csv_to_psql_object.path_to_csv_file()
                #
                #
                #df_from_csv = pd.read_csv(path_csv_for_psql,keep_default_na=False, na_values=[""])
                df_from_csv = pd.read_csv(path_csv_for_psql,keep_default_na=False)
                ##print(df_from_csv.dtypes)         # Single DF Column Dtype == dataframe.column.dtype . Here PLURAL == dtypes , used. 
                df_col_dtypes_series = df_from_csv.dtypes
                cnt_df_cols = df_col_dtypes_series.size
                ##print("------LEN DF COLS -----------",cnt_df_cols) ## Count of COLUMNS in CSV 
                ##print("-----type(df_col_dtypes_series)-------------",type(df_col_dtypes_series)) ## pandas.core.Series
                ##print("      "*90)
                ##print(df_col_dtypes_series[0])
                #
                float64 = "float64"
                int64 = "int64"
                bigint = "bigint"
                varchar = "varchar"
                object_str = "object"
                #
                if cnt_df_cols == 1:
                    ##print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 1 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) #
                    # Own FUNC == convert_col_dType== in dc_eda_funcs.py File 
                    # For OPTIMIZATION this NOT Ok as this FUNC will be called - k - times for a CSV with -- k -- number of Columns. 
                    ##print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    
                elif cnt_df_cols == 2:
                    ##print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 2 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) ## Own FUNC == convert_col_dType== in dc_eda_funcs.py File 
                    ##print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    ##print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    
                elif cnt_df_cols == 3:
                    ##print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 3 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    ##print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    ##print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    ##print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)

                elif cnt_df_cols == 4:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 4 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)

                elif cnt_df_cols == 5:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)

                #
                elif cnt_df_cols == 6:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                #
                elif cnt_df_cols == 7:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)

                #
                elif cnt_df_cols == 8:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)

                #
                elif cnt_df_cols == 9:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)

                #
                elif cnt_df_cols == 10:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[9])
                    col_10_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_10_dtype------CODED for PSQL ----",col_10_dtype)


                #
                elif cnt_df_cols == 11:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[9])
                    col_10_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_10_dtype------CODED for PSQL ----",col_10_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[10])
                    col_11_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_11_dtype------CODED for PSQL ----",col_11_dtype)

                #
                elif cnt_df_cols == 12:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[9])
                    col_10_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_10_dtype------CODED for PSQL ----",col_10_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[10])
                    col_11_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_11_dtype------CODED for PSQL ----",col_11_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[11])
                    col_12_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_12_dtype------CODED for PSQL ----",col_12_dtype)


                    
                #
                elif cnt_df_cols == 13:
                    #print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    #print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[9])
                    col_10_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_10_dtype------CODED for PSQL ----",col_10_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[10])
                    col_11_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_11_dtype------CODED for PSQL ----",col_11_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[11])
                    col_12_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_12_dtype------CODED for PSQL ----",col_12_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[12])
                    col_13_dtype = convert_col_dType(df_col_dType_str)
                    #print("-----AAAAAAAA----col_12_dtype------CODED for PSQL ----",col_13_dtype)


                try:
                    import psycopg2
                    psql_user = settings.DATABASES['default']['USER']
                    print("-----psql_user -----------AAAAAA------------",psql_user)
                    print("     "*90)


                    password = settings.DATABASES['default']['PASSWORD']
                    print("------password-----------AAAAAA------------",password)
                    print("     "*90)

                    database_name = settings.DATABASES['default']['NAME']
                    print("-------database_name----------AAAAAA------------",database_name)
                    print("     "*90)

                    conn = psycopg2.connect("dbname="+str(database_name)+" "+"user="+str(psql_user)+" "+"host=localhost"+" "+"password="+str(password)+"")
                    print("-------conn------------AAAAAA------------")
                    print("     "*90)
                    conn_cursor = conn.cursor()
                    #
                    ls_cols = list(df_from_csv) ## Get COLUMN NAMES / LABELS
                    len_ls_df = len(ls_cols)
                    
                    #
                    """
                    dict_faster_colNames = {
                        1:str(ls_cols[0]),
                        2:str(ls_cols[1]),
                        3:str(ls_cols[2])
                    }
                    try:
                        # WHAT here --- Not OK as we will get LIST Index Out of range for the == 2:str(ls_cols[1]) , 3:str(ls_cols[2]) , above. 
                    """
                    #
                    if len_ls_df == 1:
                        col_1_name = str(ls_cols[0])
                    elif len_ls_df == 2:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+");")

                    elif len_ls_df == 3:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+");")

                    elif len_ls_df == 4:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+");")

                    elif len_ls_df == 5:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        col_5_name = str(ls_cols[4])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+","+str(col_5_name)+" "+" "+str(col_5_dtype)+");")

                    elif len_ls_df == 6:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        col_5_name = str(ls_cols[4])
                        col_6_name = str(ls_cols[5])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+","+str(col_5_name)+" "+" "+str(col_5_dtype)+","+str(col_6_name)+" "+" "+str(col_6_dtype)+");")

                    elif len_ls_df == 7:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        col_5_name = str(ls_cols[4])
                        col_6_name = str(ls_cols[5])
                        col_7_name = str(ls_cols[6])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+","+str(col_5_name)+" "+" "+str(col_5_dtype)+","+str(col_6_name)+" "+" "+str(col_6_dtype)+","+str(col_7_name)+" "+" "+str(col_7_dtype)+");")

                    elif len_ls_df == 8:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        col_5_name = str(ls_cols[4])
                        col_6_name = str(ls_cols[5])
                        col_7_name = str(ls_cols[6])
                        col_8_name = str(ls_cols[7])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+","+str(col_5_name)+" "+" "+str(col_5_dtype)+","+str(col_6_name)+" "+" "+str(col_6_dtype)+","+str(col_7_name)+" "+" "+str(col_7_dtype)+","+str(col_8_name)+" "+" "+str(col_8_dtype)+");")

                    elif len_ls_df == 9:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        col_5_name = str(ls_cols[4])
                        col_6_name = str(ls_cols[5])
                        col_7_name = str(ls_cols[6])
                        col_8_name = str(ls_cols[7])
                        col_9_name = str(ls_cols[8])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+","+str(col_5_name)+" "+" "+str(col_5_dtype)+","+str(col_6_name)+" "+" "+str(col_6_dtype)+","+str(col_7_name)+" "+" "+str(col_7_dtype)+","+str(col_8_name)+" "+" "+str(col_8_dtype)+","+str(col_9_name)+" "+" "+str(col_9_dtype)+");")

                    elif len_ls_df == 10:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        col_5_name = str(ls_cols[4])
                        col_6_name = str(ls_cols[5])
                        col_7_name = str(ls_cols[6])
                        col_8_name = str(ls_cols[7])
                        col_9_name = str(ls_cols[8])
                        col_10_name = str(ls_cols[9])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+","+str(col_5_name)+" "+" "+str(col_5_dtype)+","+str(col_6_name)+" "+" "+str(col_6_dtype)+","+str(col_7_name)+" "+" "+str(col_7_dtype)+","+str(col_8_name)+" "+" "+str(col_8_dtype)+","+str(col_9_name)+" "+" "+str(col_9_dtype)+","+str(col_10_name)+" "+" "+str(col_10_dtype)+");")
                    
                    elif len_ls_df == 11:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        col_5_name = str(ls_cols[4])
                        col_6_name = str(ls_cols[5])
                        col_7_name = str(ls_cols[6])
                        col_8_name = str(ls_cols[7])
                        col_9_name = str(ls_cols[8])
                        col_10_name = str(ls_cols[9])
                        col_11_name = str(ls_cols[10])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+","+str(col_5_name)+" "+" "+str(col_5_dtype)+","+str(col_6_name)+" "+" "+str(col_6_dtype)+","+str(col_7_name)+" "+" "+str(col_7_dtype)+","+str(col_8_name)+" "+" "+str(col_8_dtype)+","+str(col_9_name)+" "+" "+str(col_9_dtype)+","+str(col_10_name)+" "+" "+str(col_10_dtype)+","+str(col_11_name)+" "+" "+str(col_11_dtype)+");")

                    elif len_ls_df == 12:
                        col_1_name = str(ls_cols[0])
                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        col_5_name = str(ls_cols[4])
                        col_6_name = str(ls_cols[5])
                        col_7_name = str(ls_cols[6])
                        col_8_name = str(ls_cols[7])
                        col_9_name = str(ls_cols[8])
                        col_10_name = str(ls_cols[9])
                        col_11_name = str(ls_cols[10])
                        col_12_name = str(ls_cols[11])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+","+str(col_5_name)+" "+" "+str(col_5_dtype)+","+str(col_6_name)+" "+" "+str(col_6_dtype)+","+str(col_7_name)+" "+" "+str(col_7_dtype)+","+str(col_8_name)+" "+" "+str(col_8_dtype)+","+str(col_9_name)+" "+" "+str(col_9_dtype)+","+str(col_10_name)+" "+" "+str(col_10_dtype)+","+str(col_11_name)+" "+" "+str(col_11_dtype)+","+str(col_12_name)+" "+" "+str(col_12_dtype)+");")

                    elif len_ls_df == 13:
                        col_1_name = str(ls_cols[0])
                        #print("----AAAAAAAA--col_1_name-------from LEN == 12----",col_1_name)
                        #print("     -----        "*90)

                        col_2_name = str(ls_cols[1])
                        col_3_name = str(ls_cols[2])
                        col_4_name = str(ls_cols[3])
                        col_5_name = str(ls_cols[4])
                        col_6_name = str(ls_cols[5])
                        col_7_name = str(ls_cols[6])
                        col_8_name = str(ls_cols[7])
                        col_9_name = str(ls_cols[8])
                        col_10_name = str(ls_cols[9])
                        col_11_name = str(ls_cols[10])
                        col_12_name = str(ls_cols[11])
                        col_13_name = str(ls_cols[12])
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+","+str(col_5_name)+" "+" "+str(col_5_dtype)+","+str(col_6_name)+" "+" "+str(col_6_dtype)+","+str(col_7_name)+" "+" "+str(col_7_dtype)+","+str(col_8_name)+" "+" "+str(col_8_dtype)+","+str(col_9_name)+" "+" "+str(col_9_dtype)+","+str(col_10_name)+" "+" "+str(col_10_dtype)+","+str(col_11_name)+" "+" "+str(col_11_dtype)+","+str(col_12_name)+" "+" "+str(col_12_dtype)+","+str(col_13_name)+" "+" "+str(col_13_dtype)+");")

                    else:
                        pass

                    ##### JIRA_ROHIT_PendingTask --- MAIN TBD --- CSV Upload Dailogue Like R STudio - Separator etc etc etc ...

                    #conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+");")
                        #
                        #conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+");")
                        #conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+" "+str(col_1_dtype)+", "+str(col_2_name)+" "+" "+str(col_2_dtype)+","+str(col_3_name)+" "+" "+str(col_3_dtype)+","+str(col_4_name)+" "+" "+str(col_4_dtype)+");")

                        
                        # conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"("+str(col_1_name)+" "+"serial PRIMARY KEY, "+str(col_2_name)+" "+" "+str(col_2_dtype)+", \
                        # "+str(col_3_name)+" "+" "+str(col_3_dtype)+", "+str(col_4_name)+" "+" "+str(col_4_dtype)+",  \
                        #   "+str(col_5_name)+" "+" "+str(col_5_dtype)+",   "+str(col_6_name)+" "+" "+str(col_6_dtype)+",   \
                        #     "+str(col_7_name)+" "+" "+str(col_7_dtype)+",  "+str(col_8_name)+" "+" "+str(col_8_dtype)+",   \
                        #       "+str(col_9_name)+" "+" "+str(col_9_dtype)+",    "+str(col_10_name)+" "+" "+str(col_10_dtype)+",     \
                        #         "+str(col_11_name)+" "+" "+str(col_11_dtype)+",  "+str(col_12_name)+" "+" "+str(col_12_dtype)+");")

                    conn.commit() # <--WE Need COMMIT to actually EXECUTE in DB
                        #conn.close()
                    
                except Exception as e:
                    print("----UTILY----def csv_to_psql(request):-----ERRRRRRROORRRRRRR-----except Exception as e----------",e)
                    print("   "*90)


                #### JIRA_ROHIT_PendingTask---Indented csv_up_cursor = conn.cursor() --Nginx Production
                ### CONN Creatiin Steps ALREADY Done ABOVE .... 
                ### Above here the PSQL  TABLE is Created --- below here the CSV Data is actually COPIED into the BLANK TABLE..
                csv_up_cursor = conn.cursor()
                with open(path_csv_for_psql, 'r') as f:
                    next(f)  # Skip the header row.
                    csv_up_cursor.copy_from(f, str(new_table_name), sep=',')
                    conn.commit() # <--WE Need COMMIT to actually EXECUTE in DB
                    """
                    ERROR if SQL Table already has RECORD == psycopg2.IntegrityError: duplicate key value violates unique constraint "test_222a_pkey"
                    DETAIL:  Key (id)=(1) already exists. ...CONTEXT:  COPY test_222a, line 1
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
                
                sql_command = "SELECT * FROM {}.{};".format(str(schema_default_public), str(new_table_name))
                df_new_table_name = pd.read_sql(sql_command,engine)
                df_new_table_name.to_csv("df_new_table_name_from_CSV_to_PSQL.csv")
                #df_new_table_name.to_csv('df_new_table_name.csv', mode='a', header=False) #
                #print("---UTILY.py----df_new_table_name.shape------def csv_to_psql(request):-------",df_new_table_name.shape)
                #print("    "*90)
                #
                
                
                    
                #return render(request,'dc_dash/csv_to_psql.html') 
                # Earlier ABOVE --- Now REDIRECT TO == eda_dataset_name_listView - from Views.py -- Which LISTS the DATASETS Names from DB
                return redirect('for_eda_dataset_name_listView') ## REDIRECT to this URL from URLs.py 


























    def json_to_dtable_csv_to_psql(self):
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        # All Above - are FIXED Values coming in from Settings.py
        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name,
        )
        engine = create_engine(database_url, echo=False)
        ##print("---------type(engine)---------",type(engine)) ##  <class 'sqlalchemy.engine.base.Engine'>

        ### TBD 
        table_name = 'test_222a'
        limit_records = "200"
        schema_default_public = "public"
        sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(table_name),str(limit_records))
        #db_table = 'public.auth_user' ## Ok 
        #sql_command = "SELECT * FROM {}".format(str(db_table)) ## OK 

        ##print("---UTIL == json_to_dtable_csv_to_psql == --------sql_command------------",sql_command)
        df_forJson = pd.read_sql(sql_command,engine)
        ##print("-----------df_forJson-------------",df_forJson)
        ##print("   "*90)
        data = json.loads(df_forJson.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        ##print("-------dict_json----------from UTILy-----",dict_json) ## OK Dont 
        ##print("   "*90)

        return JsonResponse(dict_json, safe= False)


    
    
    def SqlDb_to_json(request):
        """
        Html Form >> Save in Models >> Render template == json_dataTable_1
        """
        if request.method == 'POST':
            form_sqlQuery = sql_query_form(request.POST)
            if form_sqlQuery.is_valid():
                table_name = form_sqlQuery.cleaned_data['table_name'] ## ALSO input for EDA DataSetName if given Manually 
                limit_records = form_sqlQuery.cleaned_data['limit_records']
                new_table_name = form_sqlQuery.cleaned_data['new_table_name']
                sql_query_input = form_sqlQuery.cleaned_data['sql_query_input'] #BLANK Validation from JS ##JIRA_ROHIT 
                import psycopg2
                psql_user = settings.DATABASES['default']['USER']
                password = settings.DATABASES['default']['PASSWORD']
                database_name = settings.DATABASES['default']['NAME']
                ### conn = psycopg2.connect("dbname=test user=postgres password=secret")
                ### 'dbname=dc_dash_newspaper user=dc_dash_newspaper_user" password=JIRA_ROHIT_PendingTasktball123"'
                conn = psycopg2.connect("dbname="+str(database_name)+" "+"user="+str(psql_user)+" "+"password="+str(password)+"")
                #print("-----------type(conn)------------",type(conn)) ## <class 'psycopg2.extensions.connection'>
                # Open a cursor to perform database operations
                conn_cursor = conn.cursor()
                #print("-----------Type--conn_cursor----",type(conn_cursor)) ##<class 'psycopg2.extensions.cursor'>
                #

                if table_name == "":

                    table_name = new_table_name
                    limit_records = "100"
                    sqlQuery_object = form_sqlQuery.save() ##
                    # # JIRA_ROHIT_PendingTask --- if this gets saved Without a TABLE NAME and Limit records 
                    # # the Below - JSON / AJAX Function kicks in and displays ERROR for EMPTY INPUT
                    #print("------IF ------type(sqlQuery_object)-----------",type(sqlQuery_object))
                    #print("------IF ------sqlQuery_object---------",sqlQuery_object)
                    time.sleep(3)
                    # Execute a command: this creates a new table
                    conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"(id serial PRIMARY KEY, num integer, data varchar);")
                    #
                    # Pass data to fill a query placeholders and let Psycopg perform
                    # the correct conversion (no more SQL injections!)
                    conn_cursor.execute("INSERT INTO"+" "+str(new_table_name)+" "+"(num, data) VALUES (%s, %s)",(100, "abc'def"))
                    #
                    conn.commit() # <--WE Need COMMIT to actually EXECUTE in DB
                    #conn.close()

                    return render(request,'dc_dash/json_dataTable_1.html') #
                    
                else:
                    sqlQuery_object = form_sqlQuery.save() ##
                    # JIRA_ROHIT_PendingTask --- if this gets saved Without a TABLE NAME and Limit records 
                    # the Below - JSON / AJAX Function kicks in and displays ERROR for EMPTY INPUT
                    #print("----ELSE--------type(sqlQuery_object)-----------",type(sqlQuery_object))
                    #
                    if new_table_name =="":
                        return render(request,'dc_dash/json_dataTable_1.html') #
                        time.sleep(2)
                        pass
                    else:
                        # Execute a command: this creates a new table
                        conn_cursor.execute("CREATE TABLE"+" "+str(new_table_name)+" "+"(id serial PRIMARY KEY, num integer, data varchar);")
                        #
                        # Pass data to fill a query placeholders and let Psycopg perform
                        # the correct conversion (no more SQL injections!)
                        conn_cursor.execute("INSERT INTO"+" "+str(new_table_name)+" "+"(num, data) VALUES (%s, %s)",(100, "abc'def"))
                        #
                        conn.commit() # <--WE Need COMMIT to actually EXECUTE in DB
                        #conn.close()

                        return render(request,'dc_dash/json_dataTable_1.html') #
               
                
    def json_to_dataTable(self):
        """
        Within template == json_dataTable_1
        AJAX Call to this View with URL == 
        DB_SqlTable/DB_SqlQuery >> Pandas_DF >> Dict_JSON >> DataTables.js
        """
        from sqlalchemy import create_engine

        # Model --- for strings of SQL 
        #SqlQueryStr
        #latest_SqlQueryStr = SqlQueryStr.objects.all().values_list('table_name', flat=True).order_by('-pk')[0:1]
        latest_SqlQueryStr = SqlQueryStr.objects.all().values('table_name','limit_records').order_by('-pk')[0:1]
        #latest_SqlQueryStr = list(latest_SqlQueryStr)
        myDict = latest_SqlQueryStr[0]
        ls_mydict = list(myDict.values())
        #
        if len(str(ls_mydict[0])) > 5:
            table_name = str(ls_mydict[0])      ## Table Name STR - can be longer than 200,000 == 5 DIGITS 
            limit_records = str(ls_mydict[1])
        else :
            table_name = str(ls_mydict[1])
            limit_records = str(ls_mydict[0])

        #print("----------TABLE NAME == ",table_name)
        #print("---------lLImIt records == ",limit_records)

        ##print("---------myDict.values()--------",list(myDict.values()))
        ## dict_values(['dc_dash_data_table_1a', '77'])
        ## Much better --- list(myDict.values())
        ## Could get into ISSUE of OrderedDict
        ## SO -- SOURCE == https://stackoverflow.com/questions/17431638/get-typeerror-dict-values-object-does-not-support-indexing-when-using-python

        #print("---latest_SqlQueryStr-----------",latest_SqlQueryStr[0])

        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        # All Above - are FIXED Values coming in from Settings.py
        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name,
        )
        engine = create_engine(database_url, echo=False)
        #print("---------type(engine)---------",type(engine)) ##  <class 'sqlalchemy.engine.base.Engine'>

        # table_name =  is Hardcoded for now after looking at values from - python manage.py inspectdb
        #table_name = 'dc_dash_data_table_1a'
        #limit_records = "15"
        schema_default_public = "public"
        sql_command = "SELECT * FROM {}.{} limit {};".format(str(schema_default_public), str(table_name),str(limit_records))
        #db_table = 'public.auth_user' ## Ok 
        #sql_command = "SELECT * FROM {}".format(str(db_table)) ## OK 

        #print("-----------sql_command------------",sql_command)
        df_forJson = pd.read_sql(sql_command,engine)
        #print("-----------df_forJson-------------",df_forJson)
        #print("   "*90)
        data = json.loads(df_forJson.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        #print("-------dict_json----------from UTILy-----",dict_json)
        #print("   "*90)
        

        return JsonResponse(dict_json, safe= False)

    
    #def df_pandas_to_sql(self,df_pandas):
    def df_pandas_to_sql(self,df_pandas):
        """
        File utily.py - Newspaper - FEB 19 
        df_pandas_to_sql
        """
        from sqlalchemy import create_engine
        #
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']

        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name,
        )

        engine = create_engine(database_url, echo=False)
        ### PANDAS FUNCTION -- df.to_sql == SOURCE == http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
        #df_pandas.to_sql(name='name_df_pandas', con=engine ,if_exists = 'replace', index=False)
        df_pandas.to_sql(name='name_df_pandas2', con=engine ,if_exists = 'append', index=True)


        # SOURCE == https://creativedata.atlassian.net/wiki/spaces/SAP/pages/130318375/Python+-+Read+Write+tables+from+PostgreSQL+with+Security
        # Connecting to PostgreSQL by providing a sqlachemy engine
        #engine = create_engine('postgresql://'+os.environ['POSTGRESQL_USER']+':'+os.environ['POSTGRESQL_PASSWORD']+'@'+os.environ['POSTGRESQL_HOST_IP']+':'+os.environ['POSTGRESQL_PORT']+'/'+os.environ['POSTGRESQL_DATABASE'],echo=False)
        # DHANKAR - hardcoded below for testing 
        #engine = create_engine('postgresql://{user}:{password}@localhost:/{database_name}',echo=False)
        # Writing Dataframe to PostgreSQL and replacing table if it already exists
        #df.to_sql(name='helloworld', con=engine, if_exists = 'replace', index=False

        # ====== Reading table ======
        # Reading PostgreSQL table into a pandas DataFrame
        #data = pd.read_sql('SELECT * FROM helloworld', engine)









    #from .scraping import * ### Done above 
    #def records_from_modFields(self,model_name,model_field):

    def records_from_modFields(self,model_name,model_field):
        # model_name = news_startup_1
        # model_field = 'ORG_Name'
        entry_list = list(model_name.objects.all().values(model_field))
        #print("------entry_list---------",entry_list)
        #print("      "*90)

        mod_queryset = model_name.objects.all().values(model_field)
        record_obj = [x[model_field] for x in mod_queryset]
        #
        #return render(request, 'dc_dash/summary_stats_2.html') ## 
        return record_obj

    def data_from_model(self):
        ls_modFld_1 = []
        ls_modFld_2 = []

        model_name = news_startup_1
        model_field = 'ORG_Name'
        record_obj = self.records_from_modFields(model_name,model_field)
        return record_obj

        #fields_list =  ['ORG_Name','ORG_URL','ENG_Levl','LinkedIn_URL','COY_Stage','ORG_Industry','ORG_Sector','ORG_loca']
        # for k in len(fields_list):
        #     record_obj = records_from_modFields(model_name,str(fields_list[k]))
            #ls_modFld_1.append(record_obj)


        
        # for field in fields_list:
        #     obj = summary_stat() ## 
        #     sum_obj,mean_obj,min_obj,max_obj,median_1,lowerQ,upperQ = obj.sum_stat_1(mod_name,field)
        #     # ENSURE -- objects RETURNED in same ORDER as RETURN from "summary_stats_1.py" FUNC

        #     lowerQ_list.append(lowerQ)
        #     upperQ_list.append(upperQ)
        #     #
        #     sum_obj_list.append(sum_obj)
        #     mean_obj_list.append(mean_obj)
        #     min_obj_list.append(max_obj)
        #     max_obj_list.append(min_obj)
        #     medians_list.append(median_1)
            
        # zipped_lists = zip(cols_list,sum_obj_list,mean_obj_list,min_obj_list,max_obj_list,medians_list,lowerQ_list,upperQ_list)

        # context = {
        #            'zipped_lists':zipped_lists ### COMMA HERE if we have sheet_names_2 below ??

        #             # for sheet name 
        #             #'sheet_1_mod4':sheet_names_2[0] # No Comma here - Last Value of the "context" DICT

        #            }

        # return render(request, 'dc_dash/summary_stats_2.html') ## 
        # #return render(request, 'dc_dash/summary_stats_2.html',context) ## 


    def scrapLnkd_view(request):
        """
        Newspaper - Lnkd TGT Google Scrap
        -- gets Init Search Strings from -MODEL- model_init_lnkd
        -- Searches  Init Search Strings in Google
        """
        parms = {}

        objLnkd = linkedin_Scraper() ## from Own File == scrap_linkedin_.py
        latest_Lnkd_ls = model_init_lnkd.objects.all().order_by('-TimeStamp','-pk')[0:1] 
        # Gets Last Org and Profile entered into DB - LIFO
        if len(latest_Lnkd_ls) > 0:
            for k in range(len(latest_Lnkd_ls)):
                #df_lnkd_init = objLnkd.init_scrap_linkedin(str(latest_Lnkd_ls[k].createdStr_lnkd)) ## Original Dhank
                #google_per_page_soup_ls = objLnkd.init_scrap_linkedin(str(latest_Lnkd_ls[k].createdStr_lnkd)) #
                parms["designation"] = str(latest_Lnkd_ls[k].designation)
                parms["org_name"] = str(latest_Lnkd_ls[k].Org_Name)
                parms["city"] = str(latest_Lnkd_ls[k].Geo_City)
                parms["cntry"] = str(latest_Lnkd_ls[k].Geo_Country)
                parms["college"] = str(latest_Lnkd_ls[k].college)
                parms["university"] = str(latest_Lnkd_ls[k].university)
                parms["google_per_page_soup_ls"] = objLnkd.init_scrap_linkedin(str(latest_Lnkd_ls[k].createdStr_lnkd)) #

                #print("--from UTIL--------str(latest_Lnkd_ls[k]------------",str(latest_Lnkd_ls[k]))
                #print("    "*90)
                
                

                df_lnkd_init = objLnkd.data_from_per_page_soup(parms)
                # getting the DF == df_lnkd_init , from - scrap_Linkedin_.py
                # Saving DF to Model and Pulling QS from Model to Display in Template
                for index, row in df_lnkd_init.iterrows():
                        model = model_scrape_lnkd()
                        model.First_Name = row['First_Name']
                        model.Middle_Name = row['Middle_Name']
                        model.Last_Name = row['Last_Name']
                        model.college = row['college']
                        model.university = row['university']
                        model.designation = row['designation']
                        model.LinkdeIn = row['LinkdeIn']  
                        model.Organization = row['Org_Name']  
                        model.City = row['City']  
                        model.Country = row['Country']  
                        model.TimeStamp = row['TimeStamp'] 
                        model.save()
    
        qs_tgt_search_lnkd_level_1 = model_scrape_lnkd.objects.get_queryset().order_by('-TimeStamp')  
        """
        .order_by('-TimeStamp') # Line above changed to SOLVE for ERROR == UnorderedObjectListWarning: Pagination may yield inconsistent 
        """
        context = {}
        context['qs_tgt_search_lnkd_level_1'] = qs_tgt_search_lnkd_level_1
        return render(request, 'dc_dash/init_search_1.html' , context) 
        # return render(request,'dc_dash/loader_.html', context)

    def initSearchTracxn_view(request):
        """
        Form POST request -- get getInitSearchStrTracxn from userinput , 
        create DB entry of this STR , pass this STR as a List to scrapTracxn.
        After FORM is submitted user Lands back on the same page -- dc_dash/init_search_1.html
        """
        initSearchTracxn_ls = []
        searchPortal_ls = []
        dt_now_ls = []
        ls_InitStrSearch = []
        form = "dummy string placeholder"
        try:
            if request.method == 'POST':
                form = initSearchTracxn(request.POST) ### initSearchTracxn is - Form in dc_dash/forms.py 
                InitStrSearch = str(form["initSearchStrTracxn"].value())
                if form.is_valid():
                    ls_InitStrSearch.append(str(InitStrSearch))
                    # Add TRACXN to SEARCH STRING 
                    traxcn_str_1 = "tracxn"
                    traxcn_str_2 = "FUNDING ROUND tracxn-analyst-notes"
                    #artificial  --- Example ACTUAL STR being entered in Own Django Form
                    InitStrSearch = traxcn_str_1 + " " + str(InitStrSearch) + " " + traxcn_str_2
                    initSearchTracxn_ls.append(str(InitStrSearch))

                    searchPortal_ls.append("Tracxn")
                    dt_now_ls.append(str(dt_now))
            df_tracxn = pd.DataFrame({'initSearchStr':ls_InitStrSearch,'initSearchStrTracxn':initSearchTracxn_ls,'SearchPortal':searchPortal_ls,'TimeStamp':dt_now_ls})  
            for index, row in df_tracxn.iterrows():
                model = model_SearchTracxn()
                model.initSearchStr = row['initSearchStr']
                model.initSearchStrTracxn = row['initSearchStrTracxn']
                model.SearchPortal = row['SearchPortal']
                model.TimeStamp = row['TimeStamp']   
                model.save()

        except Exception as e:
            raise e 
            #print("    "*90)
            print("EXCEPTION from ---utily.py--- getInitSearchStrTracxn",e)
            print("    "*90)
        return render(request, 'dc_dash/init_search_1.html', {'form' : form }) 
        
        #As seen below --- Can return other LISTS etc - along with FORM and RENDER the template.
        #return render(request, 'init_search_1.html' , {'form' : form ,'snapdeal_url_list':cL,'snapdeal_names_list':dL,'snapdeal_price_list':eL,'snapdeal_pics_url_list':fL}) ## Add here -->>  dictionary2 --- As of now these RETURN's not being used     
                    
    def scrapTracxn_view(request):
        """
        Newspaper - Tracxn Init Google Scrap --- will get all TEXT Strings from -- MODEL --- model_SearchTracxn
        Will search all these Text Strings in Google
        """
        dt_now_ls = []
        
        #try: ## Indent below the TRY - uncomment the EXCEPT below 
        objTracxn = Startup_Scraper()
        
        
        #Uncomment this is MAIN ----
        # objTracxn = Startup_Scraper()
        latest_Tracxn_list = model_SearchTracxn.objects.all().order_by('-TimeStamp')[0:3] ## TBD --- Change -
        if len(latest_Tracxn_list) > 0:
            for k in range(len(latest_Tracxn_list)):
                all_soups_list = objTracxn.scrapingTracxn(str(latest_Tracxn_list[k].initSearchStrTracxn))
        str_soup_inFile = str(all_soups_list)
        ###  Messages TBD --- " We are Web Scraping the information required ..."
        #" We are Looking up ---- LIST of the Search terms given earlier ..."
        
        ### Writing Text File for TESTING ---
        textfilename = 'startUpIndia_Soup_'+dt_now+'.txt'
        with io.open(textfilename, 'w') as outfile:  #'w' WRITE STRING to FILE  ## 
            outfile.write(str(all_soups_list))
        #
        #textfilename = "test_text.txt"
        with io.open(textfilename,'r',encoding='utf-8',errors='ignore') as infile:
            str_soup_inFile = infile.read()
            str_soup_inFile = str(str_soup_inFile)
            infile.close()
        #ls_org_name_main , ls_org_url_main  = objTracxn.parse_soup_tcxn(str_soup_inFile)
        ls_org_name_main , ls_org_url_main , ls_comparables_org_urls , ls_comparables_org_urls_others , ls_comparables_org_name , ls_comparables_org_name_others = objTracxn.parse_soup_tcxn(str_soup_inFile)
        # #print("-------ls_comparables_org_urls----------------",len(ls_comparables_org_urls))
        # ##print("-------ls_comparables_org_urls----------------",ls_comparables_org_urls)
        
        # #print("-------ls_comparables_org_urls_others---------",len(ls_comparables_org_urls_others))
        # ##print("-------ls_comparables_org_urls_others---------",ls_comparables_org_urls_others)
        
        # #print("-------ls_comparables_org_name-----------------",len(ls_comparables_org_name))
        # ##print("-------ls_comparables_org_name-----------------",ls_comparables_org_name)
        
        # #print("-------ls_comparables_org_name_others----------",len(ls_comparables_org_name_others))
        # ##print("-------ls_comparables_org_name_others----------",ls_comparables_org_name_others)
        

        for k in range(len(ls_comparables_org_name)):
            dt_now_ls.append(str(dt_now))

        #df_tracxn_main = pd.DataFrame({'Org_NAME':ls_org_name_main,'Org_URL':ls_org_url_main,'News':ls_org_news,'TimeStamp':dt_now_ls})  
        #ls_org_name_main , ls_org_url_main , ls_comparables_org_urls , ls_comparables_org_urls_others , ls_comparables_org_name , ls_comparables_org_name_others
        
        df_tracxn_others = pd.DataFrame({'MAIN_Org_NAME':ls_comparables_org_name,'MAIN_Org_URL':ls_comparables_org_urls,'Others_Org_NAME':ls_comparables_org_name_others,'Others_Org_URL':ls_comparables_org_urls_others,'TimeStamp':dt_now_ls})  
        ##print("-------FROM----UTIL----df_tracxn_locals-------",df_tracxn_others) ##
        #print("    "*90)
        
        with open('df_tracxn_others_.csv', 'a') as f:
            df_tracxn_others.to_csv(f, header=True)

        for index, row in df_tracxn_others.iterrows():
            model = model_ScrapeTracxn()
            model.Org_NAME = row['MAIN_Org_NAME']
            model.Org_URL = row['MAIN_Org_URL']
            model.Org_NAME_Others = row['Others_Org_NAME']
            model.Org_URL_Others = row['Others_Org_URL']
            #model.Org_NEWS = row['News']
            model.TimeStamp = row['TimeStamp']   
            model.save()


        
        # df_tracxn_main = pd.DataFrame({'Org_NAME':ls_org_name_main,'Org_URL':ls_org_url_main,'TimeStamp':dt_now_ls})  
        # #print("    "*90)
        # #print("-------FROM----UTIL----df_tracxn_locals-------",df_tracxn_main) ##
        # #print("    "*90)
        # with open('df_tracxn_main_.csv', 'a') as f:
        #     df_tracxn_main.to_csv(f, header=True)

        # for index, row in df_tracxn_main.iterrows():
        #     model = model_ScrapeTracxn()
        #     model.Org_NAME = row['Org_NAME']
        #     model.Org_URL = row['Org_URL']
        #     #model.Org_NEWS = row['News']
        #     model.TimeStamp = row['TimeStamp']   
        #     model.save()

        


        # df_tracxn_locals = pd.DataFrame({'Primary_Org_NAME':ls_org_name_main,'Primary_Org_URL':ls_org_url_main,'Similar_LOCAL_Org_NAME':ls_org_name_locals,'Similar_LOCAL_Org_URL':ls_org_url_locals,'Similar_GLOBAL_Org_NAME':ls_org_name_globals,'Similar_GLOBAL_Org_URL':ls_org_url_globals})  
        # #print("    "*90)
        # #print("-------FROM----UTIL----df_tracxn_locals-------",df_tracxn_locals) ##
        # # ERROR --- Was getting this DF THREE Times in the CSV ?? View was being called TWICE from TEMPLATE
        # #print("    "*90)
        # with open('df_df_tracxn_locals_.csv', 'a') as f:
        #     df_tracxn_locals.to_csv(f, header=True)
            
            

        # except Exception as e:
        #     #raise e 
        #     #print("    "*90)
        #     #print("EXCEPTION from ---utily.py--- scrapTracxn_view",e)
        #     #EXCEPTION from ---utily.py--- scrapTracxn_view list index out of range
        #     #print("    "*90)
        return render(request, 'dc_dash/init_search_2.html') # As of Now Returns -- init_search_2.html
        ## Change the RETURNED HTML Page to a LIST View Page like --- data_ListView --- check in Views.py 

            
            
            # gzip_filePathLocal = '/media/dhankar/Dhankar_1/a1_19/bitbucket_up/newsdjangomain/dc_dash/gzip_soup/soup_file_tcxn.txt.gz'
            # with gzip.open(gzip_filePathLocal, 'w') as file_to_be_written:
            #     file_to_be_written.write(str(all_soups_list).encode('utf-8'))
            
            # file_read = gzip.open(gzip_filePathLocal, 'r') #
            # #‘rb’ the 'b' flag - file opened in binary mode. 
            # str_soup_inFile = file_read.read()
            # str_soup_inFile = str(str_soup_inFile)
            # file_read.close()
            # #



        #list_str1 , tcxn_list_str2 , tcxn_list_str3 , tcxn_list_str4 , org_name_locals , org_url_locals , org_name_main , org_url_main = objTracxn.parse_soup_tcxn(str_soup_inFile)
        
        #list_str1 , tcxn_list_str2 , tcxn_list_str3,tcxn_list_str4,ls_org_url_globals,ls_org_name_globals,ls_org_url_locals,ls_org_name_locals, ls_org_name_main , ls_org_url_main = objTracxn.parse_soup_tcxn(str_soup_inFile)
        
        #df_tracxn_ls = pd.DataFrame({'list_str1':list_str1,'tcxn_list_str2':tcxn_list_str2,'tcxn_list_str3':tcxn_list_str3,'tcxn_list_str4':tcxn_list_str4})  
        # #print("    "*90)
        # #print("-------FROM----UTIL-------",df_tracxn_ls) ###  getting this DF THREE Times in the CSV ??
        # #print("    "*90)
        # with open('df_df_tracxn_ls_.csv', 'a') as f:
        #     df_tracxn_ls.to_csv(f, header=True)

        ##print("FROM UTIL------------=======AAAAAAAA==================",ls_org_name_main)

        

        

    def summary_stats_1(request):
        """
        Newspaper - StartupIndia - Scraping
        """
        obj = Startup_Scraper()
        base_url = "https://www.startupindia.gov.in/content/sih/en/search.html?roles=Startup&page="
        ls_url_nums , df_indl_urls = obj.scraping_main(base_url)
        all_soups_list = obj.scraping_indl_pgs(ls_url_nums)
        gzip_filePathLocal = '/media/dhankar/Dhankar_1/a1_19/bitbucket_up/newsdjangomain/dc_dash/gzip_soup/soup_file.txt.gz'
        with gzip.open('soup_file.txt.gz', 'w') as file_to_be_written:
            file_to_be_written.write(str(all_soups_list).encode('utf-8'))
        
        file_read = gzip.open(gzip_filePathLocal, 'r') #
        #‘rb’ the 'b' flag - file opened in binary mode. 
        #https://docs.python.org/2/library/gzip.html#examples-of-usage
        str_soup_inFile = file_read.read()
        str_soup_inFile = str(str_soup_inFile)
        file_read.close()
        #

        # path_soup_file = "/media/dhankar/Dhankar_1/a7_18/a7_18_NewsPaper/news_django/news_app/soup_file.txt" # ok 
        # with io.open(path_soup_file,'r',encoding='utf-8',errors='ignore') as infile:
        #     str_soup_inFile = infile.read()

        #### LONG Returns below 
        df_forJSON , df_data1 , list_str2,list_str3,ls_eng_levl, ls_linkedin,ls_org_img,ls_reg_coy,ls_stage,ls_indus,ls_sector,ls_loc,ls_about_me,ls_timeStamp  = obj.parse_soup(str_soup_inFile)
        #print("---from Views --DF DATA------",#print(df_data1))
        #print("   "*90)

        df_forJSON = json.loads(df_forJSON.to_json(orient='records')) #
        #print(df_forJSON)
        #print("   "*90)

        # ##print(df_indl_urls) ## df_indl_urls = pd.DataFrame({'Indl_Page_URLs':ls_url_nums,'TimeStamp':ls_timeStamp})
        # #print("   "*90)

        ## Saving the --- df_data1 to DB --- 
        # col_names = ['ORG_Name','ORG_URL','ENG_Levl','LinkedIn_URL','ORG_Image','REG_Coy','COY_Stage','ORG_Industry',
        # 'ORG_Sector','ORG_loca','ORG_AboutMe','TimeStamp']

        for index, row in df_data1.iterrows():
            model = news_startup_1()
            model.ORG_Name = row['ORG_Name']
            model.ORG_URL = row['ORG_URL']
            model.ENG_Levl = row['ENG_Levl']
            model.LinkedIn_URL = row['LinkedIn_URL']
            model.ORG_Image = row['ORG_Image']
            model.REG_Coy = row['REG_Coy']
            model.COY_Stage = row['COY_Stage']
            model.ORG_Industry = row['ORG_Industry']
            model.ORG_Sector = row['ORG_Sector']
            model.ORG_loca = row['ORG_loca']
            model.ORG_AboutMe = row['ORG_AboutMe']
            model.TimeStamp = row['TimeStamp']

            model.save()
        #print(" created == model = news_startup_1() _________")

        record_obj = data_from_model()
        
        
        
        zipped_lists = zip( list_str2,list_str3,ls_eng_levl, ls_linkedin,ls_org_img,ls_reg_coy,ls_stage,ls_indus,ls_sector,ls_loc,ls_about_me,ls_timeStamp )
        
        context = {
                   'zipped_lists':zipped_lists ### COMMA HERE if we have sheet_names_2 below ??
                   }

        return render(request, 'dc_dash/summary_stats_1.html',context) ## 

    

    #def json_for_dt(request,csv_object):
    # def json_for_dt(request):
    #     from .models import csv_document  
    #     from collections import OrderedDict
        
    #     ## CANT do ASTERIX == * import within a DEFINED Function. 
    #     #MEDIA_ROOT = settings.MEDIA_ROOT
    #     ## When we are Reading this --- path_to_csv_file()
    #     ## We already have the excel saved in the MEDIA_ROOT 
    #     #path = csv_object.path_to_csv_file()
        
    #     #xls_file = pd.ExcelFile(path) 
    #     # sheet_names_2 = xls_file.sheet_names 
    #     # #print("---------sheet_names_2----------",sheet_names_2) 
    #     # ## Sheet Names is a LIST - of all the SHEETS in the Excel

    #     #df_xls = xls_file.parse()  

    #     post_request = request.POST
    #     #print("----------post_request----------",post_request)
    #     #print("     "*90)

    #     # ls_col_1 = ["NIXON","WINTERS","COL_3_VALUE"]
    #     # ls_col_2 = ["SysAdmin","SE","COL_3_VALUE"]
    #     # ls_col_3 = ["GGN","BLR","COL_3_VALUE"]
    #     # ls_col_4 = ["GGN_1","BLR_1","COL_3_VALUE"]
    #     # ls_col_5 = ["GGN_1","BLR_1","COL_3_VALUE"]

    #     ls_col_1 = ["Col_1_Row_1","Col_1_Row_2","Col_1_Row_3"]
    #     ls_col_2 = ["Col_2_Row_1","Col_2_Row_2","Col_2_Row_3"]
    #     ls_col_3 = ["Col_3_Row_1","Col_3_Row_2","Col_3_Row_3"]
    #     ls_col_4 = ["Col_4_Row_1","Col_4_Row_2","Col_4_Row_3"]
    #     ls_col_5 = ["Col_5_Row_1","Col_5_Row_2","Col_5_Row_3"]
    #     ls_col_6 = ["Col_6_Row_1","Col_6_Row_2","Col_6_Row_3"]


    #     #df_xls = pd.DataFrame({'ZCol_A':ls_col_1,'MCol_B':ls_col_2,'BCol_C':ls_col_3,'XCol_3':ls_col_4,'Col_E':ls_col_5,'Col_F':ls_col_6})
    #     ### From RT AVE  --- },index=[0])
    #     #             #
    #     # #df_xls = pd.DataFrame(OrderedDict({'ZaaCol_A':ls_col_1,'MCol_B':ls_col_2,'BCol_C':ls_col_3,'XCol_3':ls_col_4,'Col_E':ls_col_5,'Col_F':ls_col_6},index=[1]))
    #     #df_xls = pd.DataFrame(data=[ls_col_1,ls_col_2,ls_col_3,ls_col_4,ls_col_5,ls_col_6],columns=['ZaaCol_A','MCol_B','BCol_C','XCol_3','Col_E','Col_F'])

    #     #df_xls = pd.DataFrame(data=[ls_col_1,ls_col_2,ls_col_3],columns=['ZaaCol_A','MCol_B','BCol_C'])
    #     df_xls = pd.DataFrame(data=[ls_col_1,ls_col_2,ls_col_4],columns=['MCol_B','BCol_MM','ZaaCol_A'],index=["Row_1","Row_2","Row_3"])
        
        
    #     #df_xls.columns = ['ZaaCol_A','MCol_B','BCol_C','XCol_3','Col_E','Col_F']
    #     #print("-----------df_xls--------------",df_xls)
    #     #col_names_py = df_xls.keys()
    #     col_names_py = list(df_xls)
    #     #print("----------col_names_py-----------",col_names_py)
    #     # #

    #     #df_xls_json = json.loads(df_xls.to_json(orient='records')) # Test others --- orient = 'values' etc . 
    #     #df_xls_json = json.loads(df_xls.to_json(orient='columns')) # allowed values are: {‘split’,’records’,’index’,’columns’,’values’,’table’}
    #     #df_xls_json = json.loads(df_xls.to_json(orient='values')) # allowed values are: {‘split’,’records’,’index’,’columns’,’values’,’table’}
        
    #     #data = json.loads(df_xls.to_json(orient='values')) # allowed values are: {‘split’,’records’,’index’,’columns’,’values’,’table’}
    #     #data = json.loads(df_xls.to_json(orient='columns')) # allowed values are: {‘split’,’records’,’index’,’columns’,’values’,’table’}
    #     #data = json.loads(df_xls.to_json(orient='records')) # allowed values are: {‘split’,’records’,’index’,’columns’,’values’,’table’}
    #     data = json.loads(df_xls.to_json(orient='split')) # allowed values are: {‘split’,’records’,’index’,’columns’,’values’,’table’}
    #     #data = df_xls.to_json(orient='split') # allowed values are: {‘split’,’records’,’index’,’columns’,’values’,’table’}
    #     #print("-----json.loads --- from UTIL-------------",data)

    #     ### JIRA_ROHIT-- tob be done Like Old Sick EDA Views from Sick Web 
    #     getDataSet = {}
    #     tableDataKeys = {} # this DICT will hold - 
        
    #     #tableDataKey = getDataSet['data']['tableKey']

    #     tableData = {}
    #     #tableData = getDataSet['data1']['table']

    #     dict_json = {}
    #     dict_json['data_json'] = data
    #     #dict_json['data_cols'] = col_names_py
    #     #print("-------dict_json----------from UTILy-----",dict_json)
    #     #print("   "*90)
        
    #     status = 200
    #     #return JsonResponse(status, data, safe= False)
    #     return JsonResponse(dict_json, safe= False)
    #     #return render(request, 'json_dataTable_1.html',{'tableData':tableData,'tableDataKey':tableDataKey,'dataset_id':id})
    #     #return render(request, 'json_dataTable_1.html',{'tableData':tableData,'tableDataKey':tableDataKey})
        
        

    


    
    def model_from_csv(self,csv_object,dataset_name):
        """
        File utily.py - Newspaper - FEB 19 
        model_from_csv
        """
        from .models import csv_document  ## CANT do ASTERIX == * import within a DEFINED Function. 
        MEDIA_ROOT = settings.MEDIA_ROOT
        ## When we are Reading this --- path_to_csv_file()
        ## We already have the excel saved in the MEDIA_ROOT 
        path = csv_object.path_to_csv_file()
        
        xls_file = pd.ExcelFile(path) 
        sheet_names_2 = xls_file.sheet_names 
        #print("---------sheet_names_2----------",sheet_names_2) 
        ## Sheet Names is a LIST - of all the SHEETS in the Excel

        df_2 = xls_file.parse()  
        #print("------df_2------model_from_csv-----",df_2)
        #print("   "*90)
        #
        #df_pandas_to_sql
        #self.df_pandas_to_sql(df_pandas) #
        # ## Doesnt Work --- dataFrame.to_sql === FAILS 03FEB19
        ##print("------df_2-----------",df_2)
        ##print("----from UTILY----DF Coulmn Names ----------",df_2.keys())
        

        col_names_2 = list(df_2.columns.values)
        #print("-------col_names_2--------from UTILY----",col_names_2)
        len_col_names_2 = len(col_names_2)
        
        
        if len_col_names_2 == 7:   
                # dff = pd.DataFrame({'list_1':col_names_2})  
                # for index, row in dff.iterrows():
                for k in range(0,1):
                    model = model_1_col_names() 
                    model.f1 = str(col_names_2[0]) ## Changed DHANKAR FEB19
                    model.f2 = str(col_names_2[1])
                    model.f3 = str(col_names_2[2])
                    model.f4 = str(col_names_2[3])
                    model.f5 = str(col_names_2[4])
                    model.f6 = str(col_names_2[5])
                    model.f7 = str(col_names_2[6])
                    model.f8 = str(dataset_name)
                    model.save()

                    ##print("--------INDEX--1 -----",str(col_names_2[0])) ## OK 
                    #### DHANKAR FEB 19 ---- Here INIT DAta Ingress is OK --- But this DATA TABLE in DB needs to be saved with ANOTHER NAME 
                    ### So that Next time we again to a CSV Upload it doesnt OevrWrite the EARLIER DATATABLE in DB 
                
                for index, row in df_2.iterrows():
                    model = data_table_1a()
                    model.f1 = row[col_names_2[0]]
                    #print("--------ROW--1 -----",row[col_names_2[0]])
                    model.f2 = row[col_names_2[1]]
                    #print("--------ROW--2 -----",row[col_names_2[1]])
                    model.f3 = row[col_names_2[2]]   
                    model.f4 = row[col_names_2[3]]  
                    model.f5 = row[col_names_2[4]]
                    model.f6 = row[col_names_2[5]]
                    model.f7 = row[col_names_2[6]]   
                    model.save()
                #print(" DHANKAR ------created == model_2 , columns = 7 _____data_table_1a____model_1_col_names____")
                #print("      "*90)

        #return # Nothing yet 
                
        # elif len_col_names_2 == 5:
        #         dff = pd.DataFrame({'list_1':col_names_2})  
        #         for index, row in dff.iterrows():
        #             model = model_1b_col_names()   ## Created-- model_2_col_names --to store the col_names_2 - LIST
        #             model.f1 = row['list_1']
        #             model.save()
                
        #         for index, row in df_2.iterrows():
        #             model = data_table_1b()
        #             model.f1 = row[col_names_2[0]]
        #             model.f2 = row[col_names_2[1]]
        #             model.f3 = row[col_names_2[2]]   
        #             model.f4 = row[col_names_2[3]]  
        #             model.f5 = row[col_names_2[4]]
        #             model.save()
        #         #print(" created == data_table_1b , columns = 5_____________")
    


        # elif len_col_names_2 == 8:
        #         dff = pd.DataFrame({'list_1':col_names_2})  
        #         for index, row in dff.iterrows():
        #             model = model_2_col_names()   ## Created-- model_2_col_names --to store the col_names_2 - LIST
        #             model.f1 = row['list_1']
        #             model.save()
                
        #         for index, row in df_2.iterrows():
        #             model = data_table_2()
        #             model.f1 = row[col_names_2[0]]
        #             model.f2 = row[col_names_2[1]]
        #             model.f3 = row[col_names_2[2]]   
        #             model.f4 = row[col_names_2[3]]  
        #             model.f5 = row[col_names_2[4]]
        #             model.f6 = row[col_names_2[5]]
        #             model.f7 = row[col_names_2[6]]   
        #             model.f8 = row[col_names_2[7]]  
        #             model.save()
        #         #print(" created == model_2 , columns = 7 to 9_____________")
    

        # elif len_col_names_2 == 9:     
        #         dff = pd.DataFrame({'list_1':col_names_2})  
        #         for index, row in dff.iterrows():
        #             model = model_3_col_names()   ## Created-- model_2_col_names --to store the col_names_2 - LIST
        #             model.f1 = row['list_1']
        #             model.save()
                
        #         for index, row in df_2.iterrows():
        #             model = data_table_3()
        #             model.f1 = row[col_names_2[0]]
        #             model.f2 = row[col_names_2[1]]
        #             model.f3 = row[col_names_2[2]]   
        #             model.f4 = row[col_names_2[3]]  
        #             model.f5 = row[col_names_2[4]]
        #             model.f6 = row[col_names_2[5]]
        #             model.f7 = row[col_names_2[6]]   
        #             model.f8 = row[col_names_2[7]]  
        #             model.f9 = row[col_names_2[8]]  
        #             model.save()
        #         #print(" created model = model_5 , with _ count of columns = 9 ______")
                
        # elif len_col_names_2 == 10:     
        #         dff = pd.DataFrame({'list_1':col_names_2})  
        #         for index, row in dff.iterrows():
        #             model = model_4_col_names()   ## Created-- model_2_col_names --to store the col_names_2 - LIST
        #             model.f1 = row['list_1']
        #             model.save()
                
        #         for index, row in df_2.iterrows():
        #             model = data_table_4()
        #             model.f1 = row[col_names_2[0]]
        #             model.f2 = row[col_names_2[1]]
        #             model.f3 = row[col_names_2[2]]   
        #             model.f4 = row[col_names_2[3]]  
        #             model.f5 = row[col_names_2[4]]
        #             model.f6 = row[col_names_2[5]]
        #             model.f7 = row[col_names_2[6]]   
        #             model.f8 = row[col_names_2[7]]  
        #             model.f9 = row[col_names_2[8]]  
        #             model.f10 = row[col_names_2[9]]  
        #             model.save()
        #         #print(" created model = model_5 , with _ count of columns = 9 ______")
                
                
        # elif len_col_names_2 == 11:     
        #         dff = pd.DataFrame({'list_1':col_names_2})  
        #         for index, row in dff.iterrows():
        #             model = model_4_col_names()   ## Created-- model_2_col_names --to store the col_names_2 - LIST
        #             model.f1 = row['list_1']
        #             model.save()
                
        #         for index, row in df_2.iterrows():
        #             model = data_table_4()
        #             model.f1 = row[col_names_2[0]]
        #             model.f2 = row[col_names_2[1]]
        #             model.f3 = row[col_names_2[2]]   
        #             model.f4 = row[col_names_2[3]]  
        #             model.f5 = row[col_names_2[4]]
        #             model.f6 = row[col_names_2[5]]
        #             model.f7 = row[col_names_2[6]]   
        #             model.f8 = row[col_names_2[7]]  
        #             model.f9 = row[col_names_2[8]]  
        #             model.f10 = row[col_names_2[9]]  
        #             model.save()
        #         #print(" created model = model_5 , with _ count of columns = 9 ______")
                


        # else:
        #     #print("The Excel/CSV File being loaded has more than - 40 Columns")

        # #return df_2,col_names_2,len_col_names_2,sheet_names_2 ### FEB 19 --- Original 
        #status = 200 
        #return Response(responsejson(data_json, status)) ### DjangoREST API Style - RESPONSE as used by ISCK
        #from django.http import JsonResponse ### DHANK --- Import Done above 
        #return JsonResponse(data_json)



        


    # def summary_stats_1(request):
    #     mod_name = data_table_1a
    #     fields_list =  ['f1','f2','f3','f4','f5','f6','f7']
    #     sum_obj_list = []
    #     mean_obj_list = []
    #     min_obj_list = []
    #     max_obj_list = []
    #     medians_list = []
    #     lowerQ_list = []
    #     upperQ_list = []
        
    #     col_names_from_model = model_1_col_names.objects.all().values('f1')
    #     ls_cols = list(col_names_from_model)
    #     cols_list = [d['f1'] for d in ls_cols]
        
    #     for field in fields_list:
    #         obj = summary_stat() ## 
    #         sum_obj,mean_obj,min_obj,max_obj,median_1,lowerQ,upperQ = obj.sum_stat_1(mod_name,field)
    #         # ENSURE -- objects RETURNED in same ORDER as RETURN from "summary_stats_1.py" FUNC

    #         lowerQ_list.append(lowerQ)
    #         upperQ_list.append(upperQ)
    #         #
    #         sum_obj_list.append(sum_obj)
    #         mean_obj_list.append(mean_obj)
    #         min_obj_list.append(min_obj)
    #         max_obj_list.append(max_obj)
    #         medians_list.append(median_1)
            
    #         zipped_lists = zip(cols_list,sum_obj_list,mean_obj_list,min_obj_list,max_obj_list,medians_list,lowerQ_list,upperQ_list)

    #     context = {
    #                'zipped_lists':zipped_lists ### COMMA HERE if we have sheet_names_2 below ??

    #                 # for sheet name 
    #                 #'sheet_1_mod4':sheet_names_2[0] # No Comma here - Last Value of the "context" DICT

    #                }

    #     return render(request, 'dc_dash/summary_stats_1.html',context) ## 
    #     #return medians_list ## 

        
        
    def summary_stats_2(request):
        mod_name = data_table_2
        fields_list =  ['f1','f2','f3','f4','f5','f6','f7','f8']
        sum_obj_list = []
        mean_obj_list = []
        min_obj_list = []
        max_obj_list = []
        medians_list = []
        lowerQ_list = []
        upperQ_list = []
        
        col_names_from_model = model_2_col_names.objects.all().values('f1')
        ls_cols = list(col_names_from_model)
        cols_list = [d['f1'] for d in ls_cols]
        
        for field in fields_list:
            obj = summary_stat() ## 
            sum_obj,mean_obj,min_obj,max_obj,median_1,lowerQ,upperQ = obj.sum_stat_1(mod_name,field)
            # ENSURE -- objects RETURNED in same ORDER as RETURN from "summary_stats_1.py" FUNC

            lowerQ_list.append(lowerQ)
            upperQ_list.append(upperQ)
            #
            sum_obj_list.append(sum_obj)
            mean_obj_list.append(mean_obj)
            min_obj_list.append(max_obj)
            max_obj_list.append(min_obj)
            medians_list.append(median_1)
            
            zipped_lists = zip(cols_list,sum_obj_list,mean_obj_list,min_obj_list,max_obj_list,medians_list,lowerQ_list,upperQ_list)

        context = {
                   'zipped_lists':zipped_lists ### COMMA HERE if we have sheet_names_2 below ??

                    # for sheet name 
                    #'sheet_1_mod4':sheet_names_2[0] # No Comma here - Last Value of the "context" DICT

                   }

        return render(request, 'dc_dash/summary_stats_2.html',context) ## 
        

        
    def summary_stats_3(request):
        mod_name = data_table_3
        fields_list =  ['f1','f2','f3','f4','f5','f6','f7','f8','f9']
        sum_obj_list = []
        mean_obj_list = []
        min_obj_list = []
        max_obj_list = []
        medians_list = []
        lowerQ_list = []
        upperQ_list = []

        col_names_from_model = model_3_col_names.objects.all().values('f1')
        ls_cols = list(col_names_from_model)
        cols_list = [d['f1'] for d in ls_cols]
        
        for field in fields_list:
            obj = summary_stat() ## 
            sum_obj,mean_obj,min_obj,max_obj,median_1,lowerQ,upperQ = obj.sum_stat_1(mod_name,field)
            # ENSURE -- objects RETURNED in same ORDER as RETURN from "summary_stats_1.py" FUNC

            lowerQ_list.append(lowerQ)
            upperQ_list.append(upperQ)
            #
            sum_obj_list.append(sum_obj)
            mean_obj_list.append(mean_obj)
            min_obj_list.append(max_obj)
            max_obj_list.append(min_obj)
            medians_list.append(median_1)

            zipped_lists = zip(cols_list,sum_obj_list,mean_obj_list,min_obj_list,max_obj_list,medians_list,lowerQ_list,upperQ_list)

        context = {
                   'zipped_lists':zipped_lists ### COMMA HERE if we have sheet_names_2 below ??

                    # for sheet name 
                    #'sheet_1_mod4':sheet_names_2[0] # No Comma here - Last Value of the "context" DICT

                   }

        return render(request, 'dc_dash/summary_stats_3.html',context) ## 
        
    
    def summary_stats_4(request):
        mod_name = data_table_4
        fields_list =  ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10']
        sum_obj_list = []
        mean_obj_list = []
        min_obj_list = []
        max_obj_list = []
        medians_list = []
        lowerQ_list = []
        upperQ_list = []

        col_names_from_model = model_4_col_names.objects.all().values('f1')
        ls_cols = list(col_names_from_model)
        cols_list = [d['f1'] for d in ls_cols]
        
        for field in fields_list:
            obj = summary_stat() ## 
            sum_obj,mean_obj,min_obj,max_obj,median_1,lowerQ,upperQ = obj.sum_stat_1(mod_name,field)
            # ENSURE -- objects RETURNED in same ORDER as RETURN from "summary_stats_1.py" FUNC

            lowerQ_list.append(lowerQ)
            upperQ_list.append(upperQ)
            #
            sum_obj_list.append(sum_obj)
            mean_obj_list.append(mean_obj)
            min_obj_list.append(max_obj)
            max_obj_list.append(min_obj)
            medians_list.append(median_1)

            
            zipped_lists = zip(cols_list,sum_obj_list,mean_obj_list,min_obj_list,max_obj_list,medians_list,lowerQ_list,upperQ_list)

        context = {
                   'zipped_lists':zipped_lists ### COMMA HERE if we have sheet_names_2 below ??

                    # for sheet name 
                    #'sheet_1_mod4':sheet_names_2[0] # No Comma here - Last Value of the "context" DICT

                   }

        return render(request, 'dc_dash/summary_stats_4.html',context) ## 
        

        
        
    def summary_stats_5(request):
        mod_name = data_table_5
        fields_list =  ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11']
        sum_obj_list = []
        mean_obj_list = []
        min_obj_list = []
        max_obj_list = []
        medians_list = []
        lowerQ_list = []
        upperQ_list = []

        col_names_from_model = model_5_col_names.objects.all().values('f1')
        ls_cols = list(col_names_from_model)
        cols_list = [d['f1'] for d in ls_cols]
        
        for field in fields_list:
            obj = summary_stat() ## 
            sum_obj,mean_obj,min_obj,max_obj,median_1,lowerQ,upperQ = obj.sum_stat_1(mod_name,field)
            # ENSURE -- objects RETURNED in same ORDER as RETURN from "summary_stats_1.py" FUNC

            lowerQ_list.append(lowerQ)
            upperQ_list.append(upperQ)
            #
            sum_obj_list.append(sum_obj)
            mean_obj_list.append(mean_obj)
            min_obj_list.append(max_obj)
            max_obj_list.append(min_obj)
            medians_list.append(median_1)

            
            zipped_lists = zip(cols_list,sum_obj_list,mean_obj_list,min_obj_list,max_obj_list,medians_list,lowerQ_list,upperQ_list)

        context = {
                   'zipped_lists':zipped_lists ### COMMA HERE if we have sheet_names_2 below ??

                    # for sheet name 
                    #'sheet_1_mod4':sheet_names_2[0] # No Comma here - Last Value of the "context" DICT

                   }

        return render(request, 'dc_dash/summary_stats_5.html',context) ## 
        
        
    def summary_stats_6(request):
        mod_name = data_table_6
        fields_list =  ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12']
        sum_obj_list = []
        mean_obj_list = []
        min_obj_list = []
        max_obj_list = []
        medians_list = []
        lowerQ_list = []
        upperQ_list = []

        col_names_from_model = model_6_col_names.objects.all().values('f1')
        ls_cols = list(col_names_from_model)
        cols_list = [d['f1'] for d in ls_cols]
        
        for field in fields_list:
            obj = summary_stat() ## 
            sum_obj,mean_obj,min_obj,max_obj,median_1,lowerQ,upperQ = obj.sum_stat_1(mod_name,field)
            # ENSURE -- objects RETURNED in same ORDER as RETURN from "summary_stats_1.py" FUNC

            lowerQ_list.append(lowerQ)
            upperQ_list.append(upperQ)
            #
            sum_obj_list.append(sum_obj)
            mean_obj_list.append(mean_obj)
            min_obj_list.append(max_obj)
            max_obj_list.append(min_obj)
            medians_list.append(median_1)

            
            zipped_lists = zip(cols_list,sum_obj_list,mean_obj_list,min_obj_list,max_obj_list,medians_list,lowerQ_list,upperQ_list)

        context = {
                   'zipped_lists':zipped_lists ### COMMA HERE if we have sheet_names_2 below ??

                    # for sheet name 
                    #'sheet_1_mod4':sheet_names_2[0] # No Comma here - Last Value of the "context" DICT

                   }

        return render(request, 'dc_dash/summary_stats_5.html',context) ## 
        
        
        
    def chart_1(request):  
        # for details of FUNC to get Columns List - read above in own --- summary_stats_2
        
        col_names_from_model_1 = model_1_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_1 = list(col_names_from_model_1)
        cols_list_1 = [x['f1'] for x in ls_cols_1]
        

        col_names_from_model_2 = model_2_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_2 = list(col_names_from_model_2)
        cols_list_2 = [x['f1'] for x in ls_cols_2]
        
        col_names_from_model_3 = model_3_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_3 = list(col_names_from_model_3)
        cols_list_3 = [x['f1'] for x in ls_cols_3]
        

        col_names_from_model_4 = model_4_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_4 = list(col_names_from_model_4)
        cols_list_4 = [x['f1'] for x in ls_cols_4]
        
        

        #CSV File objects - for creating list from DB on Index page
        documents = csv_document.objects.all()
        
        context = { 'documents': documents ,
                   'cols_list_1':cols_list_1,
                   'cols_list_2':cols_list_2,
                   'cols_list_3':cols_list_3,
                   'cols_list_4':cols_list_4
                   
                  }


        return render(request,'dc_dash/chart_1.html',context) ## 


    
    
    
    
    def summary_stats_index(request):  
        # for details of FUNC to get Columns List - read above in own --- summary_stats_2
        
        col_names_from_model_1 = model_1_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_1 = list(col_names_from_model_1)
        cols_list_1 = [x['f1'] for x in ls_cols_1]
        

        col_names_from_model_2 = model_2_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_2 = list(col_names_from_model_2)
        cols_list_2 = [x['f1'] for x in ls_cols_2]
        
        col_names_from_model_3 = model_3_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_3 = list(col_names_from_model_3)
        cols_list_3 = [x['f1'] for x in ls_cols_3]
        

        col_names_from_model_4 = model_4_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_4 = list(col_names_from_model_4)
        cols_list_4 = [x['f1'] for x in ls_cols_4]
        
    
        #CSV File objects - for creating list from DB on Index page
        documents = csv_document.objects.all()
        
        context = { 'documents': documents ,
                   'cols_list_1':cols_list_1,
                   'cols_list_2':cols_list_2,
                   'cols_list_3':cols_list_3,
                   'cols_list_4':cols_list_4
                   
                  }


        return render(request, 'dc_dash/summary_stats_index.html',context) ## 


    
    def data_del_index(request):  
        # for details of FUNC to get Columns List - read above in own --- summary_stats_2
        
        col_names_from_model_1 = model_1_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_1 = list(col_names_from_model_1)
        cols_list_1 = [x['f1'] for x in ls_cols_1]
        

        col_names_from_model_2 = model_2_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_2 = list(col_names_from_model_2)
        cols_list_2 = [x['f1'] for x in ls_cols_2]
        
        col_names_from_model_3 = model_3_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_3 = list(col_names_from_model_3)
        cols_list_3 = [x['f1'] for x in ls_cols_3]
        

        col_names_from_model_4 = model_4_col_names.objects.all().values('f1')[0:5] #Only 1-5 Colmn names to display
        ls_cols_4 = list(col_names_from_model_4)
        cols_list_4 = [x['f1'] for x in ls_cols_4]
        
    
        #CSV File objects - for creating list from DB on Index page
        documents = csv_document.objects.all()
        
        context = { 'documents': documents ,
                   'cols_list_1':cols_list_1,
                   'cols_list_2':cols_list_2,
                   'cols_list_3':cols_list_3,
                   'cols_list_4':cols_list_4
                   
                  }


        return render(request, 'dc_dash/data_del_index.html',context) ## 

    
    
    
    
"""        ### TBD --- last Five Column Names 
        ### https://code.djangoproject.com/ticket/13089
        ### https://code.djangoproject.com/ticket/13089
        ### https://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python
        
        col_names_from_model_3_1 = model_3_col_names.objects.all().values('f1')[-5:] #Last 5 Colmn names
        # Model.objects.all().order_by('-id')[0:1]
        ls_cols_3_1 = list(col_names_from_model_3_1)
        cols_list_3_1 = [x['f1'] for x in ls_cols_3_1]
"""        













        
        
        
#obj_utily = utily_class() ## Intentionally spelt as Utily and NOT UTILITY
        #df_2,col_names_2,len_col_names_2,sheet_names_2 = self.model_from_csv(csv_object) 
        ## Func Called within same Class with a SELF 

            
"""

model.f21 = row[col_names_2[20]]  
                    model.f22 = row[col_names_2[21]]
                    model.f23 = row[col_names_2[22]]
                    model.f24 = row[col_names_2[23]]   
                    model.f25 = row[col_names_2[24]]  
                    model.f26 = row[col_names_2[25]]
                    model.f27 = row[col_names_2[26]]
                    model.f28 = row[col_names_2[27]]   
                    model.f29 = row[col_names_2[28]]  
                    model.f30 = row[col_names_2[29]]  
                    model.f31 = row[col_names_2[30]]  
                    model.f32 = row[col_names_2[31]]  
                    model.f33 = row[col_names_2[32]]
                    model.f34 = row[col_names_2[33]]
                    model.f35 = row[col_names_2[34]]   ### Till 35 Columns 
#                    model.f36 = row[col_names_2[35]]  
#                    model.f37 = row[col_names_2[36]]
#                    model.f38 = row[col_names_2[37]]
#                    model.f39 = row[col_names_2[38]]   
#                    model.f40 = row[col_names_2[39]]  
                    #model.f41 = row[col_names[40]]  
"""

    