from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.conf import settings

import json
from django.db import connections
from django.db.models import When,Count,Sum,FloatField,F,Q,Avg
from django.contrib import messages

from django.db.models import Q
from django.http import Http404 , HttpResponseForbidden , HttpResponse , HttpResponseRedirect, HttpResponseServerError ,HttpResponseBadRequest
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect #, render_to_response
from django.utils import timezone

# For Printing Tweets Lists PAGINATOR---------
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# For Search and D3 Graphs -- views.py
# from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.core import serializers
# from django.core.serializers.json import DjangoJSONEncoder

from django.shortcuts import * # FOO_Check ??

from django.template import RequestContext
from django.template import Context ,Template
from django.core.paginator import Paginator, InvalidPage, EmptyPage ,PageNotAnInteger

from django.template import loader
from django.template.loader import get_template
import datetime
from datetime import datetime
import numpy as np 
import pandas as pd
from numpy import array
from django.core.serializers.json import DjangoJSONEncoder

from django import forms

import time , csv , os 
from django.urls import reverse
from django.views import generic
from django.utils import timezone


import os, base64
from .models import*
#from .utily import* ### summary_stats_1
#from .forms import*

from django.template import RequestContext
from django.conf import settings 

MEDIA_ROOT = settings.MEDIA_ROOT

from django.contrib.auth.decorators import login_required

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import render, redirect
# """
# FOO_N$e$w$s$p$ap imports 
# """
# from .scrap_LinkedIn_ import *
# from .dc_eda_funcs import *
import datetime
dt_now = str(datetime.datetime.now())


def pyfintrader_login(request):
    print("====HERE===def pyfintrader_login(request):==")
    return render(request, 'registration/login.html') #
    #/templates/login_registration/login_index.html

## Parameter -- login_url=-- given to REDIRECT the USER who is Not Logged in ..
## IMPORTED ABOVE == from django.contrib.auth.decorators import login_required
@login_required(login_url='/admin_approved_accounts/login/') 
def pyfintrader_landing(request):
    print("====HERE===def pyfintrader_landing(request):==")
    return render(request, 'index.html') #


"""
JIRA_ROHIT_PendingTask-- below OK gives 
"""
# def get_siteID(request):
#     from django.contrib.sites.models import Site
#     new_site = Site.objects.create(domain='https://digitalCognition.co.in', name='digitalCognition.co.in')
#     print(new_site.id) #2
#     print(new_site) #https://digitalCognition.co.in
#     print("-----------AAAAAAAAAAA-----       -" *30)
#     return render(request, 'index.html') #


from django.conf import settings

import json
from django.db import connections
from django.db.models import When,Count,Sum,FloatField,F,Q,Avg
from django.contrib import messages

from django.db.models import Q
from django.http import Http404 , HttpResponseForbidden , HttpResponse , HttpResponseRedirect, HttpResponseServerError ,HttpResponseBadRequest
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect #, render_to_response
from django.utils import timezone

# For Printing Tweets Lists PAGINATOR---------
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# For Search and D3 Graphs -- views.py
# from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.core import serializers
# from django.core.serializers.json import DjangoJSONEncoder

from django.shortcuts import * # FOO_Check ??

from django.template import RequestContext
from django.template import Context ,Template
from django.core.paginator import Paginator, InvalidPage, EmptyPage ,PageNotAnInteger

from django.template import loader
from django.template.loader import get_template
import datetime
from datetime import datetime
import numpy as np 
import pandas as pd
from numpy import array
from django.core.serializers.json import DjangoJSONEncoder

from django import forms

import time , csv , os 
from django.urls import reverse
from django.views import generic
from django.utils import timezone


import os, base64
from .models import*
from .utily import* ### summary_stats_1
from .forms import*

from django.template import RequestContext
from django.conf import settings 

MEDIA_ROOT = settings.MEDIA_ROOT

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import render, redirect
"""
FOO_N$e$w$s$p$ap imports 
"""
#from .scrap_LinkedIn_ import *
from .dc_eda_funcs import *
import datetime
dt_now = str(datetime.datetime.now())


## IMPORT the FORMS --- which are passing in the END USER Search Query 
#from .forms import NameForm , SelectForm

#
# def index_sideBar(request):
#     return render(request, 'dc_dash/index_1.html') #

def test_loader(request):
    #return render(request, 'dc_dash/loader_hello_js_medium.html') # JIRA_ROHIT_PendingTask --- TBD Laterz == https://blog.hellojs.org/create-a-very-basic-loading-screen-using-only-javascript-css-3cf099c48b19
    return render(request, 'dc_dash/loader_test.html') #


def drop_table_psql_view(request,unq_id_nameField=None):
    """
    from HTML Template ==> eda_dataset_name_listView.html ,  get absolute URL ==> {{ entry.get_absolute_url_for_DROP_Table }}
    with this ABSOLUTE URL hit the URLS.py file 
    #Below Step -- Not entirely clear HOW ? 
    unq_id_nameField --- from the MODELS.py -- is getting passed to the URLS.py files URL with REGEX 
    The HTML TEMPLATE URL in frontend is also showing this -- unq_id_nameField
    
    from URLS.py file , come to this VIEWS.py and this FUNC ==> drop_table_psql_view
    The -- unq_id_nameField , is passed to this FUNC as a PARAMETER. 
    ## Further in case of EDA --- we used this -- unq_id_nameField , to IDENTIFY the SQL Data Table to be Displayed
    ## in the UTILY.py file  ==>> utily.utily_class.eda_landing_init_dataTable ==>> we pick the LAST record from Django Table == temp_dataSetName_for_EDALanding
    ## this is a Hack not a good solution 

    ## JIRA_ROHIT_PendingTask --- Now  below we need a MODAL Alert in Right Bottom - which will alert using this - unq_id_nameField >> dataset_name
    ## asking user if he want to actually DROP the TABLE
    ## if yes DROP otherwise ask and DELETE ...

    ### MODAL ALERT from eda_sidebar.html ==>> <div id="modal_alerts" class="modal_alerts_backdrop"> 
 
    """
    unq_id_nameField = str(unq_id_nameField)
    #print("------In the eda_landing_view with ---unq_id_nameField== ",unq_id_nameField)
    ls_dataSetName = unq_id_nameField.split("aacc")
    #print("--------ls_dataSetName---------",ls_dataSetName)
    dataset_name = str(ls_dataSetName[1])
    print("----------dataset_name--from VIEWS.py FUNC == drop_table_psql_view------",dataset_name)
    return render(request, 'dc_dash/eda_dataset_name_listView_older.html')
    #/media/dhankar/Dhankar_1/a1_19/bitbucket_up/newsdjangomain/dc_dash/templates/dc_dash/eda_dataset_name_listView.html
                    # context = {}

                    # context['table_for_drop_name'] = str(dataset_name)
                    
                    # return render(request, 'dc_dash/dataTable_Sql_Drop.html',context)
                    # #/media/dhankar/Dhankar_1/a1_19/bitbucket_up/newsdjangomain/dc_dash/templates/dc_dash/dataTable_Sql_Drop.html









#def eda_landing_view(request,unqId_passedFromURL):
def eda_landing_view(request,unq_id_nameField=None):
    """
    EDA Landing View - APR20_JIRA_ROHIT_Document
    ### For now --- Again save this -- dataset_name ---we get from the URL of template into a DB == temp_dataSetName_for_EDALanding
    ### from this DB we again pick this --- dataset_name --- do a SQL SELECT Query and get JSON DICT to DataTable 
    ### Challenge --- we have 2 -- dataset_name --- with same NAME. 
    ### Which actually -- CAN NOT-- happen as we get INTEGRITY Error from PSQL - 
    ### Need to show that INTEGRITY ERROR in FRONT END as ERROR MESSAGE 
    """

    from .models import temp_dataSetName_for_EDALanding

    unq_id_nameField = str(unq_id_nameField)
    #print("------In the eda_landing_view with ---unq_id_nameField== ",unq_id_nameField)
    ls_dataSetName = unq_id_nameField.split("aacc")
    print("--------ls_dataSetName---------",ls_dataSetName)
    print("             "*120)
    dataset_name = str(ls_dataSetName[1])
    # print("----------dataset_name---------",dataset_name)
    # print("          "*90)
    model = temp_dataSetName_for_EDALanding()
    model.dataset_name = str(dataset_name)
    model.save()
    ## Calling FUNCS to Delete and Create the TEMP_DB's for EDA
    #del_model_temp_dataSetName_dfFromEDA()
    #del_model_temp_colIndex_for_Eda()
    #time.sleep(2)
    #create_model_temp_dataSetName_dfFromEDA()
    #create_model_temp_colIndex_for_Eda()

    return render(request, 'dc_dash/eda_landing_index.html')



class call_eda_dataset_name_listView(ListView):
    """
    Using this as eda_Sidebar linked List View after we have reached the UNIQUE ID DataSetName 
    """
    model = csv_document                                         #----------- CHANGE MODEL NAME HERE 
    #template_name = 'dc_dash/eda_call_DataSetName_ListView.html'  #-----------dhank_tables_main
    #dc_dash/dhank_tables_main.html
    template_name = 'dc_dash/dhank_tables_main.html'

    paginate_by = 200
        
    def get_context_data(self, **kwargs):
        context = super(call_eda_dataset_name_listView, self).get_context_data(**kwargs)   #------- CHANGE ListView NAME HERE 
        ls_csv_documents = csv_document.objects.get_queryset().order_by('-pk')  
        
        paginator = Paginator(ls_csv_documents, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_dataPage = paginator.page(page)
        except PageNotAnInteger:
            file_dataPage = paginator.page(1)
        except EmptyPage:
            file_dataPage = paginator.page(paginator.num_pages)

        context['ls_csv_documents'] = file_dataPage
        return context ### Context is a DICTIONARY - can have Multiple KEY Value pairs


"""
# from django.contrib.auth.decorators import login_required
# @login_required(login_url='/admin_approved_accounts/login/') 

JIRA_ROHIT_PendingTask---If we keep the --- @login_required above the '''class''' - here above then in terminal ERROR 
File "/media/dhankar/Dhankar_1/demo/nginx_dc_oct19/nginx_demo_django/dc_dash/urls.py", line 264, in <module>
    url(r'^datasets_listView',  for_eda_dataset_name_listView.as_view(), name='for_eda_dataset_name_listView'), #
AttributeError: 'function' object has no attribute 'as_view'
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

#class for_eda_dataset_name_listView(LoginRequiredMixin,ListView): # OK 
#class for_eda_dataset_name_listView(UserPassesTestMixin,ListView): # OK 
### #JIRA_ROHIT_PendingTask --- for_eda_dataset_name_listView is missing the implementation of the test_func() method.
class for_eda_dataset_name_listView(ListView): # OK 
    """
    Linked to the MAIN Sidebar - just used for going to -- UNIQUE DataSetName of DataSetID --- Trigger EDA 
    Once we are in UNIQUE dataSet Mode - we link the above -- call_eda_dataset_name_listView == to the eda_SideBar
    """
    #JIRA_ROHIT_PendingTask --- below comented out -- 9APR20 -- uses -- admin_approved_accounts/login
    # Errors out if we dont have an Auth user Logged in == 'AnonymousUser' object has no attribute 'email'
    # def test_func(self):
    #     print("------EMAIL---------",self.request.user.email)
    #     return self.request.user.email.endswith('@gmail.com')
    # login_url = '/admin_approved_accounts/login/'

    model = csv_document                                      #---------- CHANGE MODEL NAME HERE 
    #template_name = 'dc_dash/eda_dataset_name_listView.html'  #-----------
    template_name = 'dc_dash/dhank_tables_main.html'
    paginate_by = 200

    def get_context_data(self, **kwargs):
        #searchTerm = 'TECH'
        context = super(for_eda_dataset_name_listView, self).get_context_data(**kwargs)   #------- CHANGE ListView NAME HERE 
        #list_mod_4 = news_startup_1.objects.all() # ERROR = #.get_queryset().order_by('id')   #-- CHANGE MODEL NAME HERE 
        ls_csv_documents = csv_document.objects.get_queryset().order_by('-pk')  
        """
        .order_by('-pk')  
        # Line above changed to SOLVE for ERROR == UnorderedObjectListWarning: Pagination may yield inconsistent 
        # results with an unordered object_list: <class 'dc_dash.models.csv_document'> QuerySet.
        # paginator = Paginator(list_mod_4, self.paginate_by)
        """
        # model ## from above --- Dont change MODEL == Whatevere ... it is the DJANGO GENERIC ListView Default
        # https://docs.djangoproject.com/en/2.1/ref/class-based-views/generic-display/#listview
        # ls_obj_count = len(list(csv_document.objects.all()))  
        # ls_obj_count = str(ls_obj_count)
        # # str_count = "Data Table Name = " + "Startup India "#ls_obj_count
        # str_count1 = "Count of Database Records = " + ls_obj_count
        # str_count2 = "Count of Duplicate Records = " + "NONE"#ls_obj_count
        # #raise ValidationError("Not an Email Address")
        # messages.error(self.request,str_count)
        # messages.error(self.request,str_count1)
        # messages.error(self.request,str_count2)
        # ## JIRA_ROHIT_PendingTask --- Even though this MESSAGE is defined in this VIEW - which is tied up with this == dc_dash/dhank_tables_main.html'  
        ## It Shows up in the SIDEBAR Template ??

        #data_table_name = str(news_startup_1) ## JIRA_ROHIT_PendingTask Hardcoded needs to come in from ...somewhere

        #list_targetSearchTerm = news_startup_1.objects.filter(ORG_URL__icontains=searchTerm) # to use Filters
        #list_targetSearchTerm = model_SearchTracxn.objects.filter(initSearchStr__icontains=searchTerm) # to use Filters
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













def eda_dc_jan19(request):
    """
    eda_dc_jan19
    """
    model_data =  data_table_1a ## Pass in PARAMS --- as of Now for Testing == data_table_1a AND model_1_col_names
    model_colnames =  model_1_col_names ## Pass in PARAMS --- as of Now for Testing == data_table_1a AND model_1_col_names
    #
    ls_eda_allObj = model_data.objects.get_queryset().order_by('-pk')
    ls_eda_colNames = model_colnames.objects.get_queryset().order_by('-pk')[0:1] ## JIRA_ROHIT_PendingTask --- HardCoded Needs to Change
    template_name = 'dc_dash/eda_dc_jan19.html'           #----------------------- TEMPLATE 
    
    context = {}
    context['ls_eda_allObj'] = ls_eda_allObj
    context['ls_eda_colNames'] = ls_eda_colNames

    #return context ### Context is a DICTIONARY - can have Multiple KEY Value pairs
    return render(request, 'dc_dash/eda_dc_jan19.html', context)






"""
JAN19 UploadCSV - JIRA_ROHIT_PendingTask Not main 
"""
def upload_csv_page(request):
    print("VIEW HIT --upload_csv_page---------------")
    if request.method == 'POST':
        #
        print("--------GOT POST in VIEWS -----------")
        
        form_csv_upload = form_csv_up(request.POST, request.FILES)
        if form_csv_upload.is_valid():
            print("----------FORM VALID from Views.py ---------------")
            csv_file_name = form_csv_upload.cleaned_data['csv_file_name']
            print("-----csv_file_name------",csv_file_name)
            dataset_name = form_csv_upload.cleaned_data['dataset_name']
            print("-----dataset_name------",dataset_name)
            
            #csv_object = request.FILES['csv_file']
            obj_utily = utily_class()

            #obj_utily.json_for_dt(csv_object) ### Cant be triggered from view which uplodas excel 
            #obj_utily.df_to_json_test(csv_object) ## Cant be triggered from view which uplodas excel 
            
            obj_utily.model_from_csv(csv_object,dataset_name) # ### JIRA_ROHIT_PendingTask Original path for EXCEL File to Model etc. 

            ## Passing dataset_name to Model wont work - we create SQL Table of dataset_name. 
             

            #summary_stats_2
            #obj_utily.summary_stats_2(csv_object) ## for MODEL_1
            
            #model_from_csv(csv_object) ## this is OWN - model_from_csv - FUNC from below in this "views.py" File
            #return redirect('initSearchTerms_ListView') ## upload_csv_to_model and REDIRECT to this URL from URLs.py 
            ## To be Changed
        else:
            print("FORM Not valid --------------")
            form_csv_upload = form_csv_upload()
    return render(request, 'dc_dash/init_search_1.html', {'form_csv_upload': form_csv_upload})


"""
Newspaper Landing page
"""
# def index_1(request):  
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             #csv_object = form.save()
#             #model_from_csv(csv_object) ## this is OWN - model_from_csv - FUNC from below in this "views.py" File
#             return redirect('index_1')
#     else:
#         form = DocumentForm()
        
#     #CSV File objects - for creating list from DB on Index page
#     #documents = csv_document.objects.all() ## Ok DEC 18 Uncomment Laterz 
#     #upload_csv_to_model()
#     #context = { 'documents': documents,'form': form, }
#     #return render(request, 'dc_dash/index_1.html',context) ## 
#     return render(request, 'dc_dash/index_1.html') ### Ok DEC 18 Uncomment Laterz 

def view_d3jsTree(request):
    return render(request, 'dc_dash/tree_2_d3js_.html') #


#def json_for_d3js(request):
    #searchTerm = 'PRIVATE'
    #ls_1 = model_4.objects.filter(f5__icontains='Travel').annotate(Count_f5=Count(f2))
    #ls_tree = model_ScrapeTracxn.objects.filter(ORG_Name__icontains=searchTerm).count()
    #Org_NAME_Others
    #Org_NAME

    # ls_tree = {"error": 0.6667, 
    #     "samples": 150, 
    #     "value": [50.0, 50.0, 50.0], 
    #     "label": "X[2] <= 2.45", 
        
    #     "type": "split", 
    #     "children": [
    #         {"error": 0.0000, "samples": 50, "value": [50.0, 0.0, 0.0], "label": "Leaf - 1", "type": "leaf"
    #         }, 
    #         {"error": 0.5000, "samples": 100, "value": [0.0, 50.0, 50.0], "label": "X[3] <= 1.75", "type": "split", 
    #     "children": [
    #         {"error": 0.1680, "samples": 54, "value": [0.0, 49.0, 5.0], "label": "X[2] <= 4.95", "type": "split", 
    #     "children": [
    #         {"error": 0.0408, "samples": 48, "value": [0.0, 47.0, 1.0], "label": "X[3] <= 1.65", "type": "split", 
    #     "children": [
    #         {"error": 0.0000, "samples": 47, "value": [0.0, 47.0, 0.0], "label": "Leaf - 5", "type": "leaf"}, 
    #         {"error": 0.0000, "samples": 1, "value": [0.0, 0.0, 1.0], "label": "Leaf - 6", "type": "leaf"}]}, 
    #         {"error": 0.4444, "samples": 6, "value": [0.0, 2.0, 4.0], "label": "X[3] <= 1.55", "type": "split", 
    #     "children": [
    #         {"error": 0.0000, "samples": 3, "value": [0.0, 0.0, 3.0], "label": "Leaf - 8", "type": "leaf"}, 
    #         {"error": 0.4444, "samples": 3, "value": [0.0, 2.0, 1.0], "label": "X[0] <= 6.95", "type": "split", 
    #     "children": [
    #         {"error": 0.0000, "samples": 2, "value": [0.0, 2.0, 0.0], "label": "Leaf - 10", "type": "leaf"}, 
    #         {"error": 0.0000, "samples": 1, "value": [0.0, 0.0, 1.0], "label": "Leaf - 11", "type": "leaf"}]
    #         }]
    #         }]
    #         }, 
    #         {"error": 0.0425, "samples": 46, "value": [0.0, 1.0, 45.0], "label": "X[2] <= 4.85", "type": "split", 
    #     "children": [
    #         {"error": 0.4444, "samples": 3, "value": [0.0, 1.0, 2.0], "label": "X[0] <= 5.95", "type": "split", 
    #     "children": [
    #         {"error": 0.0000, "samples": 1, "value": [0.0, 1.0, 0.0], "label": "Leaf - 14", "type": "leaf"
    #         }, 
    #         {"error": 0.0000, "samples": 2, "value": [0.0, 0.0, 2.0], "label": "Leaf - 15", "type": "leaf"}]}, 
    #         {"error": 0.0000, "samples": 43, "value": [0.0, 0.0, 43.0], "label": "Leaf - 16", "type": "leaf"}]
    #         }]
    #         }]
    #         }
    
    # #ls_final = list(ls_1)
    # return JsonResponse(ls_tree, safe=False)



def form_view(request):
    """
    FORM and Strings to be stored in Linkedin Init Search Model
    """
    Designation_ls = []
    Org_name_ls = []
    Geo_City_ls = []
    Geo_Country_ls = []
    college_ls = []
    university_ls = []
    createdStr_lnkd_ls = []
    searchPortal_ls = []
    dt_now_ls = []

    if request.method == 'POST':
        form_linkedIn = initSearch_Portal_form(request.POST)
        if form_linkedIn.is_valid():
            Designation = form_linkedIn.cleaned_data['Designation']
            Organization_Name = form_linkedIn.cleaned_data['Organization_Name']
            # ## NOT REQD we have -- forms.py == required=False
            # if not form_linkedIn.cleaned_data['Geo_City']:
            #     #print("----------Geo_City----EMPTY--------")  
            #     Geo_City = " "
            # else:
            Geo_City = form_linkedIn.cleaned_data['Geo_City']
            Geo_Country = form_linkedIn.cleaned_data['Geo_Country']
            college = form_linkedIn.cleaned_data['college']
            university = form_linkedIn.cleaned_data['university']
            #
            linkedIn = "Linkedin profile"
            searchPortal_ls.append("LinkedIn")
            dt_now_ls.append(str(dt_now))
            createdStr_lnkd = linkedIn + " " + Designation + " " + Organization_Name + " " + Geo_City + " " + Geo_Country + " " + college + " " + university
            createdStr_lnkd_ls.append(str(createdStr_lnkd))
            Designation_ls.append(str(Designation))
            Org_name_ls.append(str(Organization_Name))
            Geo_City_ls.append(str(Geo_City))
            Geo_Country_ls.append(str(Geo_Country))
            college_ls.append(str(college))
            university_ls.append(str(university))
            df_init_lnkd = "test"
            df_init_lnkd = pd.DataFrame({'Designation':Designation_ls,'Org_Name':Org_name_ls,'Geo_City':Geo_City_ls,'Geo_Country':Geo_Country_ls,'university':university_ls,'college':college_ls,'createdStr_lnkd':createdStr_lnkd_ls,'SearchPortal':searchPortal_ls,'TimeStamp':dt_now_ls})  
        else:
            print(" FORM NOT VALID -------------")
            # print(form_linkedIn.as_p())
            form_linkedIn = initSearch_Portal_form()

        for index, row in df_init_lnkd.iterrows():
            model = model_init_lnkd()
            model.designation = row['Designation']
            model.Org_Name = row['Org_Name']
            model.Geo_City = row['Geo_City']
            model.Geo_Country = row['Geo_Country']
            model.college = row['college']
            model.university = row['university']
            model.createdStr_lnkd = row['createdStr_lnkd']
            model.SearchPortal = row['SearchPortal']
            model.TimeStamp = row['TimeStamp']   
            model.save()
            
            context = {}
            context['form_linkedIn'] = form_linkedIn

        return render(request,'dc_dash/init_search_1.html', context) 
        ## This render the Template == init_search_1.html is OK 
        # as it pulls in the embeded == dhankar_sidebar.html 
        
"""
list_init_LinkedIn
qs_tgt_search_lnkd_level_1
"""
# def initSearch_LinkedIn_view(request):
#     # ls_designation_str_Portal = []
#     # initSearchLinked_ls = []
#     # ls_InitStrLnkd = []
#     # dt_now_linkedin = []
#     # searchPortal_ls = []
#     # form_lnkd = "dummy form"
#     #template_name = 'dc_dash/init_search_1.html'     
#     #paginate_by = 200 ## Actual pagination managed with dataTable - JS , not Django
#     if request.method == 'POST':
#         form_lnkd = initSearch_Portal_form(request.POST) #
#         # initSearchTracxn is - Form in dc_dash/forms.py 
#         #InitStr_LinkedIn = str(form["initSearch_str_Portal"].value())
#         if form_lnkd.is_valid():
#             designation_str_Portal = form_lnkd.cleaned_data['designation_str_Portal']
#             #Org_Name_str_Portal = form_lnkd.cleaned_data['Org_Name_str_Portal']
            
#             print("form_isValid--------LINKEDIN------------",designation_str_Portal)
#             #print("form_isValid--------LINKEDIN------------",Org_Name_str_Portal)

#             # designation_str_Portal = str(form["designation_str_Portal"].value())
#             # Org_Name_str_Portal = str(form["Org_Name_str_Portal"].value())
#             # print("-------------designation_str_Portal------------------",designation_str_Portal)
            
#             # # ls_designation_str_Portal.append(str(designation_str_Portal))
#             # linkedin_str_1 = "Linkedin"
#             # linkedin_str_2 = "Product Manager New York"
#             # #artificial  --- Example ACTUAL STR being entered in Own Django Form
#             # createdStr_LinkedIn = linkedin_str_1 + " " + str(InitStr_LinkedIn)+ " " + linkedin_str_2
#             # initSearchLinked_ls.append(str(createdStr_LinkedIn))
#             # searchPortal_ls.append("LinkedIn")
#             # dt_now_linkedin.append(str(dt_now))
#             # print("----------createdStr_LinkedIn-------from Views-------",createdStr_LinkedIn)
            
#             context = {}
#             #qs_tgt_search_lnkd_level_1
#             context['qs_tgt_search_lnkd_level_1'] = qs_tgt_search_lnkd_level_1
#             context['form_lnkd'] = form_lnkd

#     # df_init_lnkd = pd.DataFrame({'init_Str':ls_InitStrLnkd,'createdStr_LinkedIn':createdStr_LinkedIn,'SearchPortal':searchPortal_ls,'TimeStamp':dt_now_linkedin})  
#     # for index, row in df_init_lnkd.iterrows():
#     #     model = model_init_lnkd()
#     #     model.init_Str_lnkd = row['init_Str']
#     #     model.createdStr_lnkd = row['createdStr_LinkedIn']
#     #     model.SearchPortal = row['SearchPortal']
#     #     model.TimeStamp = row['TimeStamp']   
#     #     model.save()

#     # qs_init_search_lnkd = model_init_lnkd.objects.get_queryset().order_by('-TimeStamp')  
#     # context['qs_init_search_lnkd'] = qs_init_search_lnkd
       
#     return render(request,'dc_dash/init_search_1.html', context)
#     #return render(request,'dc_dash/dhankar_sidebar.html', context)


class data_ListView(ListView):
    
    model =  news_startup_1                                        #----------------------- CHANGE MODEL NAME HERE 
    #template_name = 'dc_dash/data_ListView.html'                  #----------------------- TEMPLATE to be Created
    #template_name = 'dc_dash/dhankar_data_ListView.html'          #----------------------- TEMPLATE to be Created
    template_name = 'dc_dash/dhank_tables_main.html'            #---------------All DATATables Main Template - dhank_tables_main.html
    
    paginate_by = 200
        
    def get_context_data(self, **kwargs):
        searchTerm = 'TECH'
        context = super(data_ListView, self).get_context_data(**kwargs)   #----------------------- CHANGE ListView NAME HERE 
        #list_mod_4 = news_startup_1.objects.all() # ERROR = #.get_queryset().order_by('id')   #-- CHANGE MODEL NAME HERE 
        list_mod_4 = news_startup_1.objects.get_queryset().order_by('-TimeStamp')  
        """
        .order_by('-TimeStamp')  
        # Line above changed to SOLVE for ERROR == UnorderedObjectListWarning: Pagination may yield inconsistent 
        # results with an unordered object_list: <class 'dc_dash.models.news_startup_1'> QuerySet.
        # paginator = Paginator(list_mod_4, self.paginate_by)
        """
        # model ## from above --- Dont change MODEL == Whatevere ... it is the DJANGO GENERIC ListView Default
        # https://docs.djangoproject.com/en/2.1/ref/class-based-views/generic-display/#listview
        ls_obj_count = len(list(news_startup_1.objects.all()))  
        ls_obj_count = str(ls_obj_count)
        str_count = "Data Table Name = " + "Startup India "#ls_obj_count
        str_count1 = "Count of Database Records = " + ls_obj_count
        str_count2 = "Count of Duplicate Records = " + "NONE"#ls_obj_count
        #raise ValidationError("Not an Email Address")
        messages.error(self.request,str_count)
        messages.error(self.request,str_count1)
        messages.error(self.request,str_count2)
        ## JIRA_ROHIT_PendingTask --- Even though this MESSAGE is defined in this VIEW - which is tied up with this == dc_dash/dhank_tables_main.html'  
        ## It Shows up in the SIDEBAR Template ??

        data_table_name = str(news_startup_1) ## JIRA_ROHIT_PendingTask Hardcoded needs to come in from ...somewhere

        #list_targetSearchTerm = news_startup_1.objects.filter(ORG_URL__icontains=searchTerm) # to use Filters
        list_targetSearchTerm = model_SearchTracxn.objects.filter(initSearchStr__icontains=searchTerm) # to use Filters
        paginator = Paginator(list_mod_4, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_dataPage = paginator.page(page)
        except PageNotAnInteger:
            file_dataPage = paginator.page(1)
        except EmptyPage:
            file_dataPage = paginator.page(paginator.num_pages)

        context['list_mod_4'] = file_dataPage
        context['list_targetSearchTerm'] = list_targetSearchTerm
        context['ls_obj_count'] = ls_obj_count # ls_obj_count
        context['data_table_name'] = data_table_name #data_table_name
        return context ### Context is a DICTIONARY - can have Multiple KEY Value pairs



"""
list_init_search_terms
"""

import datetime
dt_now = str(datetime.datetime.now())
    
#class initSearchTerms_ListView(request , ListView):
def initSearchTerms_ListView(request):
    ls_InitStrSearch = []
    initSearchTracxn_ls = []
    searchPortal_ls = []
    dt_now_ls = []
    form = "dummy string placeholder"
    
    model =  model_SearchTracxn                            #----------------------- CHANGE MODEL NAME HERE 
    template_name = 'dc_dash/init_search_1.html'           #----------------------- TEMPLATE 
    paginate_by = 200 ## Actual pagination managed with dataTable - JS , not Django

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

    # def get_context_data(self, **kwargs):
    #     context = super(initSearchTerms_ListView, self).get_context_data(**kwargs)   #------------- CHANGE ListView NAME HERE 
    #     #list_init_search_terms = news_startup_1.objects.all() # ERROR = #.get_queryset().order_by('id')   #-- CHANGE MODEL NAME HERE 
    
    list_init_search_terms = model_SearchTracxn.objects.get_queryset().order_by('-TimeStamp')  
    """
    .order_by('-TimeStamp')  
    # Line above changed to SOLVE for ERROR == UnorderedObjectListWarning: Pagination may yield inconsistent 
    # results with an unordered object_list: <class 'dc_dash.models.news_startup_1'> QuerySet.
    # paginator = Paginator(list_mod_4, self.paginate_by)
    """
    # model ## from above --- Dont change MODEL == Whatevere ... it is the DJANGO GENERIC ListView Default
    # https://docs.djangoproject.com/en/2.1/ref/class-based-views/generic-display/#listview
    # ls_obj_count = len(list(news_startup_1.objects.all()))  
    # ls_obj_count = str(ls_obj_count)
    # str_count = "Data Table Name = " + "Startup India "#ls_obj_count
    # str_count1 = "Count of Database Records = " + ls_obj_count
    # str_count2 = "Count of Duplicate Records = " + "NONE"#ls_obj_count
    
    # messages.error(self.request,str_count)
    # messages.error(self.request,str_count1)
    # messages.error(self.request,str_count2)
    
    # data_table_name = str(news_startup_1) ## JIRA_ROHIT_PendingTask Hardcoded needs to come in from ...somewhere

    #list_targetSearchTerm = news_startup_1.objects.filter(ORG_URL__icontains=searchTerm) # to use Filters
    # list_targetSearchTerm = model_SearchTracxn.objects.filter(initSearchStr__icontains=searchTerm) # to use Filters
    # paginator = Paginator(list_init_search_terms, self.paginate_by)

    # page = self.request.GET.get('page')

    # try:
    #     file_dataPage = paginator.page(page)
    # except PageNotAnInteger:
    #     file_dataPage = paginator.page(1)
    # except EmptyPage:
    #     file_dataPage = paginator.page(paginator.num_pages)

    # context['list_init_search_terms'] = list_init_search_terms
    # #file_dataPage
    context = {}

    context['list_init_search_terms'] = list_init_search_terms
    context['form'] = form

    #print("-------------list_init_search_terms-------------------",list_init_search_terms)
    print("     "*90)

    #return context ### Context is a DICTIONARY - can have Multiple KEY Value pairs
    return render(request, 'dc_dash/init_search_1.html', context)


"""
Newspaper ListView
"""

class data_ListView_index(ListView):
    
    model =  news_startup_1                                 #----------------------- CHANGE MODEL NAME HERE 
    template_name = 'dc_dash/index_1.html'                  #----------------------- TEMPLATE to be Created
    
    
    paginate_by = 200 ## Actual pagination managed with dataTable - JS , not Django
        
    def get_context_data(self, **kwargs):
        searchTerm = 'FINANCIAL'
        context = super(data_ListView_index, self).get_context_data(**kwargs)   #----------------------- CHANGE ListView NAME HERE 
        list_mod_4 = news_startup_1.objects.all()                         #----------------------- CHANGE MODEL NAME HERE 
        #list_targetSearchTerm = news_startup_1.objects.filter(ORG_URL__icontains=searchTerm) # to use Filters
        list_targetSearchTerm = model_SearchTracxn.objects.filter(initSearchStr__icontains=searchTerm) # to use Filters
        paginator = Paginator(list_mod_4, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_dataPage = paginator.page(page)
        except PageNotAnInteger:
            file_dataPage = paginator.page(1)
        except EmptyPage:
            file_dataPage = paginator.page(paginator.num_pages)

        context['list_mod_4'] = file_dataPage
        #context['list_targetSearchTerm'] = list_targetSearchTerm ## Hold -- get TWO Toggle Buttons in NAVBAR because of this
        return context


class data_ListView_scrapTracxn_view(ListView):
    
    model =  model_ScrapeTracxn                                   #----------------------- CHANGE MODEL NAME HERE 
    template_name = 'dc_dash/init_search_2.html'                  #----------------------- TEMPLATE to be Created
    
    paginate_by = 150
        
    def get_context_data(self, **kwargs):
        #searchTerm = 'FINANCIAL'
        context = super(data_ListView_scrapTracxn_view, self).get_context_data(**kwargs)   #----------------------- CHANGE ListView NAME HERE 
        list_mod_data = model_ScrapeTracxn.objects.all()                           #----------------------- CHANGE MODEL NAME HERE 
        #list_targetSearchTerm = news_startup_1.objects.filter(ORG_URL__icontains=searchTerm) # to use Filters
        #list_targetSearchTerm = model_SearchTracxn.objects.filter(initSearchStr__icontains=searchTerm) # to use Filters
        #paginator = Paginator(list_mod_data, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_dataPage = paginator.page(page)
        except PageNotAnInteger:
            file_dataPage = paginator.page(1)
        except EmptyPage:
            file_dataPage = paginator.page(paginator.num_pages)

        context['list_mod_data'] = file_dataPage
        #context['list_targetSearchTerm'] = list_targetSearchTerm ## Hold -- get TWO Toggle Buttons in NAVBAR because of this
        return context






# class data_ListView_initSearch(ListView):
    
#     model =  news_startup_1                                        #----------------------- CHANGE MODEL NAME HERE 
#     template_name = 'dc_dash/init_search_1.html'                  #----------------------- TEMPLATE to be Created
    
    
#     paginate_by = 50
        
#     def get_context_data(self, **kwargs):
#         searchTerm = 'FINANCIAL'
#         context = super(data_ListView_index, self).get_context_data(**kwargs)   #----------------------- CHANGE ListView NAME HERE 
#         list_mod_4 = news_startup_1.objects.all()                         #----------------------- CHANGE MODEL NAME HERE 
#         #list_targetSearchTerm = news_startup_1.objects.filter(ORG_URL__icontains=searchTerm) # to use Filters
#         list_targetSearchTerm = model_SearchTracxn.objects.filter(initSearchStr__icontains=searchTerm) # to use Filters
#         paginator = Paginator(list_mod_4, self.paginate_by)

#         page = self.request.GET.get('page')

#         try:
#             file_dataPage = paginator.page(page)
#         except PageNotAnInteger:
#             file_dataPage = paginator.page(1)
#         except EmptyPage:
#             file_dataPage = paginator.page(paginator.num_pages)

#         context['list_mod_4'] = file_dataPage
#         #context['list_targetSearchTerm'] = list_targetSearchTerm ## Hold -- get TWO Toggle Buttons in NAVBAR because of this
#         return context




#/media/dhankar/Dhankar_1/a1_19/bitbucket_up/newsdjangomain/dc_dash/dcJan19_Sqlite_Queries_.py
#from .dcJan19_Sqlite_Queries_ import * ## Deprecated 
from .sql_queries_all import * 


#def deduplicate_data_view(request):
def deduplicate_data_view(response):
    """
    Right Now generic - Link it to text On a Particular List View Page and DEDUP only for that Model 
    Like this create Multiple Functions that DEDUP and REDIRECT Back to same URL's == redirect_url
    """
    model_name = news_startup_1
    col_name = 'ORG_Name'

    dups = dedupDataORM(model_name,col_name)
    #redirect_url = 'data_ListView' # URL NAME for the page == dc_dash/dhank_tables_main.html #
    # # Goes into Infinite Loop of REDIRECTS
    redirect_url = '/dashboard/data_ListView/' 
    # ACTUAL URL for the page == dc_dash/dhank_tables_main.html

    #return HttpResponse('') ## Will return a BLANK Page - Not OK 
    return HttpResponseRedirect(redirect_url)
    



# def upload_csv_page(request):
#      if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
# #            form.save()
#             csv_object = form.save()
#             obj_utily = utily_class()
#             obj_utily.model_from_csv(csv_object)
#             #summary_stats_2
#             #obj_utily.summary_stats_2(csv_object) ## for MODEL_1
            
#             #model_from_csv(csv_object) ## this is OWN - model_from_csv - FUNC from below in this "views.py" File
#             return redirect('index_1') ## upload_csv_to_model
#      else:
#         form = DocumentForm()
#      return render(request, 'dc_dash/upload_csv_page.html', {'form': form})



# get all Model Columns as LISTS of INT's
# 
######## get Data Types - when we upload CSV __________________________________HACKYJIRA_ROHIT_PendingTask
        ### use the uploaded Data Frame - for Predictions etc 
        ### for Dashboard etc use the data from Lists from Django DB 
        

def pred_df_1(request):
    mod_name = model_4
    fields_list =  ['f1','f2','f3','f4','f5','f6','f7']
    f1_list = []
    f2_list = []
    f3_list = []
    f4_list = []
    f5_list = []
    f6_list = []
    f7_list = []
        
    for field in fields_list:
        obj = pred_class() ## 
        int_ls_obj = obj.pred_1(mod_name,fields_list) # Maintain ORDER of RETURN's == int_ls_obj
        #print("type___",type(int_ls_obj))
        #print("len___",len(int_ls_obj))
        #f1_list.append(x for x in int_ls_obj)  # OK Laterz       #[x for x in int_ls_obj]
        #f2_list.append(int_ls_obj)
        #print("type___",type(f2_list))
        #print("len___",len(f2_list))
    #print("type___",type(f1_list))
    #print("len___",len(f1_list))
    #zipped_lists = zip(f1_list)
        
    #context = {
    #           'zipped_lists':zipped_lists,
               
                # for sheet name 
                #'sheet_1_mod4':sheet_names_2[0] # No Comma here 

    #           }
        
        
    return render(request, 'dc_dash/pred_1.html')#,context) ## 


"""

        lowerQ_list.append(lowerQ)
        upperQ_list.append(upperQ)
        #
        sum_obj_list.append(sum_obj)
        mean_obj_list.append(mean_obj)
        min_obj_list.append(max_obj)
        max_obj_list.append(min_obj)
        medians_list.append(median_1)
        zipped_lists = zip(col_names_2,sum_obj_list,mean_obj_list,min_obj_list,max_obj_list,medians_list,lowerQ_list,upperQ_list)
        
    context = {
               'zipped_lists':zipped_lists,
               
                # for sheet name 
                'sheet_1_mod4':sheet_names_2[0] # No Comma here 

               }

"""


"""
def dataup_1(request):
    
    obj = calc_2() ## 
    #df_1,col_names_1,len_col_names_1,sheet_names_1 = obj.xlsuponly_1()  # Uncomment Laterz 
    #print("___from Views__len_col_names_1__",len_col_names_1) # Uncomment Laterz 
    
    df_2,col_names_2,len_col_names_2,sheet_names_2 = obj.xlsuponly_2()
    print("___from Views__len_col_names_2__",len_col_names_2)
    #
    obj.fileup(col_names_2,len_col_names_2,df_2)
    #
    #list_mod_4a = model_4.objects.order_by('f1')[0:6]  #Laterz --- get objects from (ListView) below with Pagination
    list_mod_4a = model_4.objects.all()[0:10]  #Laterz --- get objects from (ListView) below with Pagination
    #
    searchTerm = 'Travel'
    #count_1 = model_4.objects.filter(f5__icontains='Travel').annotate(Count_f5=Count(f2))
    count_1 = model_4.objects.filter(f5__icontains=searchTerm).count()
    
    context = {'col_1_mod4':col_names_2[0],
               'col_2_mod4':col_names_2[1],
               'col_3_mod4':col_names_2[2],
               'col_4_mod4':col_names_2[3],
               'col_5_mod4':col_names_2[4],
               'col_6_mod4':col_names_2[5],
               'col_7_mod4':col_names_2[6],
               'col_8_mod4':col_names_2[7],
               'col_9_mod4':col_names_2[8],
               'col_10_mod4':col_names_2[9],
               'col_11_mod4':col_names_2[10],
               'col_12_mod4':col_names_2[11],
               'col_13_mod4':col_names_2[12],
               'col_14_mod4':col_names_2[13],
               'col_15_mod4':col_names_2[14],
               
               'sheet_1_mod4':sheet_names_2[0],
               
               'list_mod_4a':list_mod_4a,
               'count_1':count_1
               
               }
    
    return render(request, 'dc_dash/data_up_1.html',context) ## 
"""






def data_del_1(request):
    table_1 = "DATA_TABLE_1" ## Dummy Change - get names of Models and Tables 
    obj = calc_2() ## 
    obj.del_model_1()
    obj.del_model_1_colnames()
    print("_________MODEL_1___Deleted Data Table and Contents - Creating Data Table again ....")
    obj.create_model_1()
    obj.create_model_1_colnames()
    
    context = { 'table_1':table_1,
                }
            
    return render(request, 'dc_dash/data_del_1.html',context) ## 


def data_del_2(request):
    table_1 = "DATA_TABLE_2" ## Dummy Change - get names of Models and Tables 
    obj = calc_2() ## 
    obj.del_model_2()
    obj.del_model_2_colnames()
    print("_________MODEL_2___Deleted Data Table and Contents - Creating Data Table again ....")
    obj.create_model_2()
    obj.create_model_2_colnames()
    
    context = { 'table_1':table_1,
                }
            
    return render(request, 'dc_dash/data_del_2.html',context) ## 


def data_del_3(request):
    table_1 = "DATA_TABLE_3" ## Dummy Change - get names of Models and Tables 
    obj = calc_2() ## 
    obj.del_model_3()
    obj.del_model_3_colnames()
    print("_________MODEL_3___Deleted Data Table and Contents - Creating Data Table again ....")
    obj.create_model_3()
    obj.create_model_3_colnames()
    
    context = { 'table_1':table_1,
                }
            
    return render(request, 'dc_dash/data_del_3.html',context) ## 

def data_del_4(request):
    table_1 = "DATA_TABLE_4" ## Dummy Change - get names of Models and Tables 
    obj = calc_2() ## 
    obj.del_model_4()
    print("_________MODEL_4___Deleted Data Table and Contents - Creating Data Table again ....")
    obj.create_model_4()
    
    context = { 'table_1':table_1,
                }
            
    return render(request, 'dc_dash/data_del_4.html',context) ## get the colnames_1 and colnames_2 from calc_2.py in here...

"""
#-----Display all Objects of DB in HTML Tables----------------------

class table_mod_4(ListView):
    
    model = model_4                                                      #----------------------- CHANGE MODEL NAME HERE 
    template_name = 'dc_dash/table_mod_4.html'                           #----------------------- TEMPLATE to be Created
    
    paginate_by = 20
        
    def get_context_data(self, **kwargs):
        context = super(table_mod_4, self).get_context_data(**kwargs)   #----------------------- CHANGE ListView NAME HERE 
        list_mod_4 = model_4.objects.all()                              #----------------------- CHANGE MODEL NAME HERE 
        #list_Tweets = Tw1.objects.filter(text='') # to use Filters
        paginator = Paginator(list_mod_4, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_TweetsPage = paginator.page(page)
        except PageNotAnInteger:
            file_TweetsPage = paginator.page(1)
        except EmptyPage:
            file_TweetsPage = paginator.page(paginator.num_pages)

        context['list_mod_4'] = file_TweetsPage
        return context
    
"""



########### Flash Altert ---- 

#flash_alert_template.html


# from collections import OrderedDict 

# dict1 = OrderedDict({x: x**5 for x in (1, 5, 10)}).__class__ 
# ord_dict = OrderedDict({x: x**5 for x in (1, 5, 10)}) 
# print(ord_dict) # OrderedDict([(1, 1), (10, 100000), (5, 3125)])