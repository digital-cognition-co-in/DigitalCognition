from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from django.contrib.sessions.models import Session
from django.core.files import File
import re , io , json , gzip , time , psycopg2 , os
import pandas as pd
#import codecs
import subprocess
from subprocess import call

from django.conf import settings
#from settings import * ## Doesnt Work -- Code below has chained Imports === user = settings.DATABASES['default']['USER']
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse 
from collections import OrderedDict
from sqlalchemy import create_engine
from django.shortcuts import render , redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
#
# For Printing Tweets Lists PAGINATOR---------
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.template import RequestContext
from django.template import Context ,Template
from django.core.paginator import Paginator, InvalidPage, EmptyPage ,PageNotAnInteger

from django.template import loader
from django.template.loader import get_template

from .pv_bonds import *
from .models import *
from .dc_eda_funcs import convert_col_dType
from .forms import form_csvUp_pvBonds_csvToPsql
#
import numpy as np
import os , random , copy , math 
import datetime
dt_now = str(datetime.datetime.now())


"""
STARTS == FOO_userInputParamsForpvBonds
"""
def js_toPy_params_pvBonds(request):
    """
    FOO_userInputParamsForpvBonds
    params - come here from == URL == js_toPy_params_pvBonds
    """
    if request.method == 'POST':
        request.session['f_bondfaceValue'] = request.POST.get('f_bondfaceValue')
        request.session['SAIR_Value'] = request.POST.get('SAIR_Value')
        request.session['t_couponValue'] = request.POST.get('t_couponValue')
    return render(request,'dc_dash/pvBonds_renderPage.html')

def py_toJS_DF_pvBonds(request):
    """
    FOO_userInputParamsForpvBonds
    JIRA_ROHIT_PendingTask --- using GIT Code === https://github.com/lianfengluo/django-assessment/blob/329e72404dc7e30f71a8ed9b3630012b25421f19/assessproject/views.py#L148
    """
    ls_pv = []
    ls_F = []
    ls_R = []
    ls_T = []
    ls_pv_percOfFace = []
    ls_dtNow = []

    if request.method == 'GET':
        try:
            for session in Session.objects.all():
                # print("=GOT===JIRA_ROHIT_PendingTaskK---AACC    "*10)
                if 'f_bondfaceValue' in session.get_decoded():
                    f_bondfaceValue = session.get_decoded().get("f_bondfaceValue")
                    SAIR_Value = session.get_decoded().get("SAIR_Value")
                    t_couponValue = session.get_decoded().get("t_couponValue")
                    #print(session.get_decoded())
                    params = {}
                    params['F'] = float(f_bondfaceValue) #MILLION_Dollars , MILLION = SIX ZERO's , this is  FACE VALUE / PRINCIPAL / DENOMINATION 
                    params['R'] = float(SAIR_Value)      # in % SAIR - STATED ANNUAL INTEREST RATE 
                    params['T'] = float(t_couponValue)   # COUPON PAYMENT PERIODS
                    #print(params)
                    pv,pv_percOfFace = vanila_pv_paramsUI(params)
                    ls_pv.append(pv)
                    ls_F.append(f_bondfaceValue)
                    ls_R.append(SAIR_Value)
                    ls_pv_percOfFace.append(pv_percOfFace)
                    ls_T.append(t_couponValue)

                    #df_pvBonds = pd.DataFrame({'ls_pv':ls_pv,'ls_F':ls_F,'ls_R':ls_R,'ls_pv_percOfFace':ls_pv_percOfFace,'TimeStamp':ls_T})  
                    df_pvBonds = pd.DataFrame({'Present Value':ls_pv,'Face Value':ls_F,'Rate - SAIR':ls_R,'Percent - PV of FACE':ls_pv_percOfFace,'Coupon Value':ls_T})  
                    #print("======AAA=====       "*30)

                    #print(df_pvBonds)
                    #df_pvBonds - df.stack()
                    ## JIRA_ROHIT_PendingTask Test --- 
                    df_pvBondsStacked = df_pvBonds.stack(level=0)
                    #print(type(df_pvBondsStacked)) ## <class 'pandas.core.series.Series'>
                    #print("======DDD=====   SERIES    "*30)
                    df_pvBondsStacked = df_pvBondsStacked.to_frame()
                    df_pvBondsStacked.reset_index(inplace=True)
                    print("         "*30)

                    df_pvBondsStacked.columns = ['Index','Col_Labels','Values_Numeric']
                    print(df_pvBondsStacked.index)
                    print("=========JIRA_ROHIT_PendingTask ===INDEX ONLY ==AAAA=======    "*30)
                    data = json.loads(df_pvBondsStacked.to_json(orient='split')) ## Original 
                    print(data)
                    #data = json.loads(df_pvBondsStacked.to_json(orient='records')) ## Not Ok  
                    #data = json.loads(df_pvBondsStacked.to_json(orient='table')) ## What the F** JIRA_ROHIT_PendingTask ---??
                    #data = json.loads(df_pvBondsStacked.to_json(orient='index')) ## What the F** JIRA_ROHIT_PendingTask ---
                    #data = json.loads(df_pvBondsStacked.to_json(orient='values')) ## What the F** JIRA_ROHIT_PendingTask ---
                    print("=========JIRA_ROHIT_PendingTask .stack()==BBB=======    "*30)

                    #data = json.loads(df_pvBonds.to_json(orient='split')) ## Original 
                    dict_json = {}
                    dict_json['data_json'] = data
                    print(dict_json)
                    
        except KeyError:
            pass
            print("===def py_toJS_DF_pvBonds(request):==GOT==except KeyError:    "*10)
        
    return JsonResponse(dict_json, safe= False)

"""
ENDS == FOO_userInputParamsForpvBonds
"""















### STARTS Methods and Class for - pvBonds CSV dataSets == CSV_uploadDF_forPvBonds

#df_pvBonds = pd.DataFrame({'Present Value':ls_pv,'Face Value':ls_F,'Rate - SAIR':ls_R,'Percent - PV of FACE':ls_pv_percOfFace,'Coupon Value':ls_T})  
"""
csv to df of actual bonds will have col_name = face val , or Not cant say thus need to get Col_Index as JS Click into PARAMS
"""
# params = {}
# params['face_val'] = 'Face Value'
# params['SAIR'] = 'Rate - SAIR'
# params['Coupon_T'] = 'Coupon Value'

def colClick_indx_fromJs(request):
    """
    CSV_uploadDF_forPvBonds

    #JIRA_ROHIT_PendingTask_laterz## USE This to get COL_INDEX for all pvBonds- JS to PY Column Clicks 
     --- create individual Columns within this DB for all the EDA Methods >>>
    - 1 for Emails-ColIndex , 2 - Fuzzy_ColIndex etc
    
    JIRA_ROHIT_PendingTask laterz --- create within this method - check for different text values within the >>>
    col_num_formatchSimilarText = request.POST.get('col_num_formatchSimilarText')
    col_num_forEmailparts = request.POST.get('col_num_forEmailparts')
    col_num_forFuzzySomeFoo = request.POST.get('col_num_forFuzzySomeFoo')

    """
    if request.method == 'POST':
        #print("=====FILE---UTILY_Bonds...In here === colClick_indx_fromJs:====")
        #print("      ***        "*200)
        if request.POST.get('col_faceValue'):
            col_faceValue = request.POST.get('col_faceValue')
        elif request.POST.get('col_SAIR_Value'):
            col_SAIR_Value = request.POST.get('col_SAIR_Value')
        elif request.POST.get('col_couponValue'):
            col_couponValue = request.POST.get('col_couponValue')
        else:
            pass
        
        if col_faceValue != None:
            model = temp_colIndex_for_Eda()
            ### JIRA_ROHIT_PendingTask --- this Model / Django DB needs to be Deleted on some set time interval = to FLUSH Garbagae COL Indexes
            model.colIndx_js_to_py_pvBonds = str(col_faceValue)
            model.save()
        if col_SAIR_Value != None:   ## JIRA_ROHIT_PendingTask ERROR -- UnboundLocalError: local variable 'col_SAIR_Value' referenced before assignment
            model = temp_colIndex_for_Eda()
            model.col_SAIR_Value = str(col_SAIR_Value)
            # model.col_couponValue = str(col_couponValue)
            model.save()
    return render(request,'dc_dash/eda_sidebar.html')

def pv_BondsDataFrame(df,params):
    """
    CSV_uploadDF_forPvBonds
    """
    F = params['face_val'] ## indx of F col of csv to df 
    R = params['SAIR']
    T = params['Coupon_T']

    df['PresentValue'] = df[col].apply(lambda x: pv_BondsSingleRecord(params))
    print(df)
    return df


class for_pvBonds_dataset_name_listView(ListView):
    """
    CSV_uploadDF_forPvBonds
    Same as == class for_eda_dataset_name_listView(ListView): ===>> SEP19
    Linked to the MAIN Sidebar - just used for going to -- UNIQUE DataSetName of DataSetID --- Trigger EDA 
    Once we are in UNIQUE dataSet Mode - we link the above -- call_eda_dataset_name_listView == to the eda_SideBar
    """
    model = csv_document                                      #---------- CHANGE MODEL NAME HERE 
    # model ## from above --- Dont change MODEL == Whatevere ... it is the DJANGO GENERIC ListView Default
    # https://docs.djangoproject.com/en/2.1/ref/class-based-views/generic-display/#listview
        
    #template_name = 'dc_dash/eda_dataset_name_listView.html'  #-----------
    template_name = 'dc_dash/dhank_tables_main.html'
    paginate_by = 200
        
    def get_context_data(self, **kwargs):
        context = super(for_eda_dataset_name_listView, self).get_context_data(**kwargs)   #------- CHANGE ListView NAME HERE 
        ls_csv_documents = csv_document.objects.get_queryset().order_by('-pk')  
        """
        .order_by('-pk')  -  Line above changed to SOLVE for ERROR == UnorderedObjectListWarning: Pagination may yield inconsistent 
        # results with an unordered object_list: <class 'dc_dash.models.csv_document'> QuerySet.
        """
        paginator = Paginator(ls_csv_documents, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_dataPage = paginator.page(page)
        except PageNotAnInteger:
            file_dataPage = paginator.page(1)
        except EmptyPage:
            file_dataPage = paginator.page(paginator.num_pages)

        context['ls_csv_documents'] = file_dataPage
        # context['list_targetSearchTerm'] = list_targetSearchTerm
        # context['ls_obj_count'] = ls_obj_count # ls_obj_count
        # context['data_table_name'] = data_table_name #data_table_name
        return context ### Context is a DICTIONARY - can have Multiple KEY Value pairs



class utily_bondsClass():
    def __init__(self):
        pass        ## JIRA_ROHIT_PendingTask Does this here - pass - mean we dont have to have a SELF param for Class methods defined in this Class?? 

    import datetime
    dt_now = str(datetime.datetime.now())
    dt_all_now = datetime.datetime.now()
    minute_now = dt_all_now.minute
    #print("--------dt_all_now.minute---------",dt_all_now.minute)
    # now = datetime.datetime.now()
    #print(now.year, now.month, now.day, now.hour, now.minute, now.second)

    def pvbonds_initLandingListView(request):
        """
        Simple REDIRECT to Page == pvBonds_initLanding_index_bonds_go.html
        After Clicking on Button == in == dhankar_sidebar.html
        
        """
        print("===HIT FILE --utily_bonds.py--====pvbonds_initLandingListView======")
        print("===   AA       "*10)
        from .models import pvbonds_csv_document

        model = pvbonds_csv_document
        print(model)
        pvBonds_ls_csv = pvbonds_csv_document.objects.get_queryset().order_by('-pk')  
        print(pvBonds_ls_csv) ## JIRA_ROHIT_PendingTask_Nginx --- This is an EMPTY Queryset 
        template_name = 'dc_dash/pyFindTrader_templates/pvBonds_initLanding_index_bonds_go.html'
        paginate_by = 200
        paginator = Paginator(pvBonds_ls_csv,paginate_by)

        page = request.GET.get('page')
        print(page) # NONE --- 05SEP19

        try:
            file_dataPage = paginator.page(page)
        except PageNotAnInteger:
            file_dataPage = paginator.page(1)
        except EmptyPage:
            file_dataPage = paginator.page(paginator.num_pages)

        context = {}
        context['pvBonds_ls_csv'] = file_dataPage
        print(context) ## {'pvBonds_ls_csv': <Page 1 of 1>}
        print("====BBBBB=====context['pvBonds_ls_csv'] = file_dataPage====             "*30)
        return render(request, 'dc_dash/pyFindTrader_templates/pvBonds_initLanding_index_bonds_go.html',context)

    def view_pvBonds_csvUploadiFrame(request):
        """
        URL == call_view_pvBonds_csvUploadiFrame
        This calls iFRAME into dhankar_SideBar. 
        # /dc_dash/pyFindTrader_templates/pvBonds_csv_to_Psql_iFrame.html
        """
        # print("========HIT THE VIEW=====def view_pvBonds_csvUploadiFrame(request):======")
        # print("===========            BBB        "*90)

        return render(request,'dc_dash/pyFindTrader_templates/pvBonds_csv_to_Psql_iFrame.html') #


    def view_pvBondsLanding_index(request):
        """
        Init landing page = == pvBondsLanding_index.html , for INDIVIDUAL dataSet of pvBonds CSV from PSQL 
        This will include datatable.js 
        """
        return render(request,'dc_dash/pyFindTrader_templates/pvBondsLanding_index.html') #


    def pvBonds_landing_init_dataTable(self):  
        """
        ## READ the DataSetName from the MODEL == temp_dataSetName_for_EDALanding
        ## In this File --- below method is saving this dataSetName - in the model == 
        ## After extracting the --- dataSetName from the URL 
                # model = temp_dataSetName_for_EDALanding()
                # model.pvBondsTempDataSetName = str(dataset_name)
                # model.save()

        JIRA_ROHIT_PendingTask --- Change the == .objects.all().values( ==== get a values_list 
        #/media/dhankar/Dhankar_1/a1_19/bitbucket_up/newsdjangomain/dc_dash/templates/dc_dash/pyFindTrader_templates/pvBondsLanding_index.html
        
        """
        from sqlalchemy import create_engine

        latest_dataSetName = temp_dataSetName_for_EDALanding.objects.all().values('pvBondsTempDataSetName').order_by('-pk')[0:1]
        myDict = latest_dataSetName[0]
        ls_data_set_name = []
        for keys , values in myDict.items():
            if "pvBondsTempDataSetName" in keys:
                ls_data_set_name.append(str(values))
                dataSetName = str(ls_data_set_name[0])
                print("------UTILY_BONDS.py------dataSetName---------AAAAAAAAAAAAAAAAAA================------",dataSetName)
                print("  =======     "*90)

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
        #print("------UTILY.py----eda_landing_init_dataTable(self)----------df_for_eda-------------",df_for_eda)
        #print("     "*90)

        data = json.loads(df_for_eda.to_json(orient='split'))
        dict_json = {}
        dict_json['data_json'] = data
        print("------UTILY.py----pvBonds_landing_init_dataTable----------dict_json=-------------",dict_json)
        print("   ====  "*90)
        
        return JsonResponse(dict_json, safe= False)


    def pvBonds_listView(request,pvBonds_unq_id_nameField=None):
        """
        being called within eda_sidebar.html
        as on 01SEP19 -- same as ==> class for_eda_dataset_name_listView(ListView): ....from FILE ==> views.py 
        get List from Django model - pass list with ABSOLUTE URL to JS DataTables
        Below JIRA_ROHIT_PendingTask --- not OK 
        """
        from .models import temp_dataSetName_for_EDALanding
        # ### Creating an entry for pvBonds dataSets within this == temp_dataSetName_for_EDALanding.pvBondsTempDataSetName

        pvBonds_unq_id_nameField = str(pvBonds_unq_id_nameField)
        #print("------In the eda_landing_view with ---pvBonds_unq_id_nameField== ",pvBonds_unq_id_nameField)
        #csv_to_psql_object.pvBonds_unq_id_nameField = str(csv_file_name) + "axmnpvbonds" + str(new_table_name) + "pvbonds" + str(dt_all_now.minute) ## Foo
        #print("===============csv_to_psql_object.pvBonds_unq_id_nameField ==========",csv_to_psql_object.pvBonds_unq_id_nameField)
        
        ls_dataSetName = pvBonds_unq_id_nameField.split("axmnpvbonds")
        # print("----pvBonds_listView----ls_dataSetName---------",ls_dataSetName) # OK 
        dataset_name = str(ls_dataSetName[1]) ## List element - 1 Index
        dataset_name = str(dataset_name.split("pvbonds"))
        # print("----pvBonds_listView------dataset_name----AA-----",dataset_name) # OK 
        # print("----pvBonds_listView------dataset_name----AABB-----",type(dataset_name))
        # dataset_name = dataset_name.replace('[','') # OK 
        # dataset_name = dataset_name.replace("'",'')
        import re # regex 
        dataset_name = re.search("\[\'(.+?)\'",dataset_name) ## this is STR not List 
        dataset_name = dataset_name.group(1)

        # print("----pvBonds_listView------dataset_name-----BB----",type(dataset_name)) # OK 
        # print("----pvBonds_listView------dataset_name-----CC----",dataset_name)
        # print("          "*90)
        model = temp_dataSetName_for_EDALanding()
        model.pvBondsTempDataSetName = str(dataset_name)
        model.save()
        
        # ## Calling FUNCS to Delete and Create the TEMP_DB's for EDA
        #del_model_temp_dataSetName_dfFromEDA()
        #del_model_temp_colIndex_for_Eda()
        #time.sleep(2)
        #create_model_temp_dataSetName_dfFromEDA()
        #create_model_temp_colIndex_for_Eda()

        #return render(request, 'dc_dash/pyFindTrader_templates/pvBonds_initLanding_index_bonds_go.html')
        # Just the landing page again --- the actual redirect happens from csv_to_psql funcs return 
        #return render(request, 'dc_dash/eda_landing_index.html')   ### JIRA_ROHIT_PendingTask --- Change 
        return render(request,'dc_dash/pyFindTrader_templates/pvBondsLanding_index.html') 
      

    def view_pvBonds_renderPage(request):
        """
        REDIRECT to Main Window page from iFrame Sidebar
        call dataTables within this pvBonds_renderPage.html
        """
        return render(request,'dc_dash/pvBonds_renderPage.html') 

    def iFrame_pvBonds_view(request):
        """
        this just calls iFRAME into eda_SideBar. 
        """
        return render(request,'dc_dash/pvBondsIframe.html') #
    

    def pvBonds_csvToPsql(request):
        """
        Create a JS Form in MAIN_Sidebar.html
        <form action="/dc/csv_to_psql/" method="post" enctype="multipart/form-data">
        Not very clear - where the CSV actual FILE is hitting the = form_csvUp_pvBonds_csvToPsql(request.POST, request.FILES)
        Is it the ,PARAM == request.FILES -- in line below  ?? 
                                           
        """
        import datetime
        # dt_now = str(datetime.datetime.now()) ## JIRA_ROHIT_PendingTask
        dt_all_now = datetime.datetime.now()
        # minute_now = dt_all_now.minute

        if request.method == 'POST':
            print("-------------REQUEST----------------",request)
            print("===========request.POST==============",request.POST)
            print("===========request.FILES==============",request.FILES)
            form_pvBonds_csv_to_psql = form_csvUp_pvBonds_csvToPsql(request.POST, request.FILES)
            print("===========form_pvBonds_csv_to_psql=============",form_pvBonds_csv_to_psql)
            # -------------REQUEST---------------- <WSGIRequest: POST '/dc/pvBonds_csvToPsql/'>
            # ===========request.POST============== <QueryDict: {'pvBonds_dataset_name': ['testALPHA1'], 'csrfmiddlewaretoken': ['Q6PK4Bz3h15AuK2w6PKxkIf3SHgt51ilGPIeci3mGXEU8ZmRVEMUWj202szhwXBM'], 'pvBonds_csv_file_name': ['testALPHA']}>
            # ===========request.FILES============== <MultiValueDict: {'pvBonds_csv_file': [<InMemoryUploadedFile: 3BondsNSE.csv (text/csv)>]}>

            if form_pvBonds_csv_to_psql.is_valid():
                # print("=======UTILY_Bonds====== form_csvUp_pvBonds_csvToPsql.is_valid():=             "*30) # OK
                csv_file_name = form_pvBonds_csv_to_psql.cleaned_data['pvBonds_csv_file_name']
                print("============csv_file_name============",csv_file_name)
                print("                                    "*10)
                dataset_name = form_pvBonds_csv_to_psql.cleaned_data['pvBonds_dataset_name'] #
                print("============dataset_name===========",dataset_name)
                print("                                    "*10)
                
                ## THIS -- dataset_name -- SAVED in MODEL == csv_document 
                # # Using-in Views.py-for_eda_dataset_name_listView-- as INIT Name to call DATASET for EDA. 
                dataset_name = str(dataset_name).lower()
                new_table_name = str(dataset_name)
                ## Forced to LOWER as PSQL saves it as LOWER 
                ## but in certain SqlAlchemy ERRORS etc they will show it as UPPER or even MIXED CASE 
                ## SOURCE -- SO -- https://stackoverflow.com/questions/695289/cannot-simply-use-postgresql-table-name-relation-does-not-exist

                csv_to_psql_object = form_pvBonds_csv_to_psql.save(commit=False)
                print("============csv_to_psql_object===========AAA=============",csv_to_psql_object)
                print("                                    "*90)
                csv_to_psql_object.pvBonds_unq_id_nameField = str(csv_file_name) + "axmnpvbonds" + str(new_table_name) + "pvbonds" + str(dt_all_now.minute) ## Foo
                print("===============csv_to_psql_object.pvBonds_unq_id_nameField ==========",csv_to_psql_object.pvBonds_unq_id_nameField)
                print("                                    "*90)
                ## SOURCE - SO --- DANIEL ROSEMAN Answer -- https://stackoverflow.com/questions/17126983/add-data-to-modelform-object-before-saving
                csv_to_psql_object.save()         #obj_utily.model_from_csv(csv_object,dataset_name) # ### Original path for EXCEL File to Model etc. 
                
                print("============csv_to_psql_object===========BBB=============",csv_to_psql_object)
                print("                                    "*90)
                from .models import pvbonds_csv_document  # CANT do ASTERIX == * import within a DEFINED Function. 
                MEDIA_ROOT = settings.MEDIA_ROOT  # Reading-pvBonds_csv_file() #already have CSV saved in MEDIA_ROOT 
                path_to_pvBonds_csv_file = csv_to_psql_object.path_to_pvBonds_csv_file()
                print("===========path_to_pvBonds_csv_file=========",path_to_pvBonds_csv_file)
                print("                                    "*90)
                #df_from_csv = pd.read_csv(path_csv_for_psql,keep_default_na=False, na_values=[""])
                df_from_csvPVBonds = pd.read_csv(path_to_pvBonds_csv_file,keep_default_na=False)
                #print(df_from_csv.dtypes)         # Single DF Column Dtype == dataframe.column.dtype . Here PLURAL == dtypes , used. 
                df_col_dtypes_series = df_from_csvPVBonds.dtypes
                cnt_df_cols = df_col_dtypes_series.size
                print("------LEN DF COLS -----------",cnt_df_cols) ## Count of COLUMNS in CSV 
                print("-----type(df_col_dtypes_series)-------------",type(df_col_dtypes_series)) ## pandas.core.Series
                print("                                    "*90)
                #print(df_col_dtypes_series[0])
                #
                float64 = "float64"
                int64 = "int64"
                bigint = "bigint"
                varchar = "varchar"
                object_str = "object"
                #
                if cnt_df_cols == 1:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 1 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) #
                    # Own FUNC == convert_col_dType== in dc_eda_funcs.py File 
                    # For OPTIMIZATION this NOT Ok as this FUNC will be called - k - times for a CSV with -- k -- number of Columns. 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    
                elif cnt_df_cols == 2:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 2 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) ## Own FUNC == convert_col_dType== in dc_eda_funcs.py File 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    
                elif cnt_df_cols == 3:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 3 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)

                elif cnt_df_cols == 4:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 4 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)

                elif cnt_df_cols == 5:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 5 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)

                #
                elif cnt_df_cols == 6:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 6 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                #
                elif cnt_df_cols == 7:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 7 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)

                #
                elif cnt_df_cols == 8:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 8 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)

                #
                elif cnt_df_cols == 9:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 9 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)

                #
                elif cnt_df_cols == 10:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 10 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[9])
                    col_10_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_10_dtype------CODED for PSQL ----",col_10_dtype)


                #
                elif cnt_df_cols == 11:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 11 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[9])
                    col_10_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_10_dtype------CODED for PSQL ----",col_10_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[10])
                    col_11_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_11_dtype------CODED for PSQL ----",col_11_dtype)

                #
                elif cnt_df_cols == 12:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 12 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[9])
                    col_10_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_10_dtype------CODED for PSQL ----",col_10_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[10])
                    col_11_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_11_dtype------CODED for PSQL ----",col_11_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[11])
                    col_12_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_12_dtype------CODED for PSQL ----",col_12_dtype)


                    
                #
                elif cnt_df_cols == 13:
                    print("---FILE == UTILY.py == FUNC== csv_to_psql-------GOT 13 COLS -----------")
                    df_col_dType_str = str(df_col_dtypes_series[0])
                    col_1_dtype = convert_col_dType(df_col_dType_str) 
                    print("-----AAAAAAAA----col_1_dtype------CODED for PSQL ----",col_1_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[1])
                    col_2_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_2_dtype------CODED for PSQL ----",col_2_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[2])
                    col_3_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_3_dtype------CODED for PSQL ----",col_3_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[3])
                    col_4_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_4_dtype------CODED for PSQL ----",col_4_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[4])
                    col_5_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_5_dtype------CODED for PSQL ----",col_5_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[5])
                    col_6_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_6_dtype------CODED for PSQL ----",col_6_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[6])
                    col_7_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_7_dtype------CODED for PSQL ----",col_7_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[7])
                    col_8_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_8_dtype------CODED for PSQL ----",col_8_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[8])
                    col_9_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_9_dtype------CODED for PSQL ----",col_9_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[9])
                    col_10_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_10_dtype------CODED for PSQL ----",col_10_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[10])
                    col_11_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_11_dtype------CODED for PSQL ----",col_11_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[11])
                    col_12_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_12_dtype------CODED for PSQL ----",col_12_dtype)
                    df_col_dType_str = str(df_col_dtypes_series[12])
                    col_13_dtype = convert_col_dType(df_col_dType_str)
                    print("-----AAAAAAAA----col_12_dtype------CODED for PSQL ----",col_13_dtype)


                try:
                    import psycopg2
                    psql_user = settings.DATABASES['default']['USER']
                    password = settings.DATABASES['default']['PASSWORD']
                    database_name = settings.DATABASES['default']['NAME']
                    conn = psycopg2.connect("dbname="+str(database_name)+" "+"user="+str(psql_user)+" "+"password="+str(password)+"")
                    conn_cursor = conn.cursor()
                    print(conn_cursor)
                    print("=========conn_cursor ===============",conn_cursor)
                    #
                    ls_cols = list(df_from_csvPVBonds) ## Get COLUMN NAMES / LABELS
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
                        print("----AAAAAAAA--col_1_name-------from LEN == 12----",col_1_name)
                        print("     -----        "*90)

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

                    conn.commit() # <--WE Need COMMIT to actually EXECUTE in DB
                        #conn.close()
                    
                except Exception as e:
                    print("----UTILY_Bonds.py----def csv_to_psql(request):-----ERRRRRRROORRRRRRR-----except Exception as e----------",e)
                    #print("   "*90)


            ### CONN Creatiin Steps ALREADY Done ABOVE .... 
            ### Above here the PSQL  TABLE is Created --- below here the CSV Data is actually COPIED into the BLANK TABLE..
            csv_up_cursor = conn.cursor()
            with open(path_to_pvBonds_csv_file, 'r') as f:
                next(f)  # Skip the header row.
                csv_up_cursor.copy_from(f, str(new_table_name), sep=',',null='None')
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
            print("---UTILY_BONDS.py----df_new_table_name.shape------def csv_to_psql(request):-------",df_new_table_name.shape)
            print("    "*90)
            return redirect('for_pvBonds_dataset_name_listView')
            #
            #return redirect('pvbonds_initLandingListView') ## REDIRECT to this URL PATTERN from URLs.py == call_pvbonds_initLandingListView
            # If we give Actual URL PATTERN in place of PATTERN NAME == 
            # django.urls.exceptions.NoReverseMatch: Reverse for 'pvbonds_initLandingListView' not found. 'pvbonds_initLandingListView' is not a valid view function or pattern name.

### ENDS Methods and Class for - pvBonds CSV dataSets