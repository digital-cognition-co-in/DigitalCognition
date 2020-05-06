from django.db import models

# Create your models here.
from django.conf import settings
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.db import models
import datetime
from django.forms import ValidationError

MEDIA_ROOT = settings.MEDIA_ROOT

"""
Creating a FORM with a FIELD which can have an EMPTY VALUE 
For the Related MODEL need to ensure --- 
If field has blank=True, form validation will allow entry of an empty value.
If field has blank=False, the field will be required.
SO == https://stackoverflow.com/questions/34954631/django-empty-form-field-validation-is-not-working-with-clean-method
"""

#
class temp_ceil_floor_params(models.Model):
    """
    JIRA_ROHIT = https://github.com/digital-cognition-co-in/DigitalCognition/issues/17
    
    """
    single_col = models.IntegerField()
    col_index = models.IntegerField()
    ceil_mode = models.IntegerField()
    


class temp_tableName_forMerge(models.Model):
    temp_tableName = models.CharField(max_length=255, blank=True)
    temp_tableName1 = models.CharField(max_length=255, blank=True)
    new_merged_tableName = models.CharField(max_length=255, blank=True)
    #counter_for_temp_tableName = models.IntegerField(default=0,blank=True) ## Not used maybe required

class temp_dataSetName_dfFromEDA(models.Model):
    temp_dataset_name = models.CharField(max_length=255, blank=True)
    counter_for_dfFromEDA = models.IntegerField(default=0,blank=True)

class temp_dataSetName_for_EDALanding(models.Model):
    dataset_name = models.CharField(max_length=255, blank=True)
    pvBondsTempDataSetName = models.CharField(max_length=255, blank=True)

class temp_colIndex_for_Eda(models.Model):
    """
    In Views.py = def eda_landing_view(request,unq_id_nameField=None):
    This Model and related TABLE gets Created and Deleted using SCHEMA Editor
    """
    column_index_from_dataTables_js = models.CharField(max_length=255, blank=True) 
    colIndx_js_to_py_pvBonds = models.CharField(max_length=255, blank=True)
    col_SAIR_Value = models.CharField(max_length=255, blank=True)
    col_couponValue = models.CharField(max_length=255, blank=True)

class eda_inputs_MatchSimilarText(models.Model):
    fuzziness = models.CharField(max_length=255, blank=True) ## Need a JS Validated INT laterz ...
    str_to_compare_with = models.CharField(max_length=255, blank=True)
    #operation_type = models.CharField(max_length=255, blank=True) #
    # Original use_with == COL or VALUE - were doing only Values NOW
    #column_index_from_dataTables_js = models.CharField(max_length=255, blank=True) 
    ### Not used --- Created another Model == temp_colIndex_for_Eda
    


class eda_inputs_search_and_replace(models.Model):
    dataset_name = models.CharField(max_length=255, blank=True)
    form_input_new_column = models.CharField(max_length=255, blank=True)
    django_form_input_operation_type = models.CharField(max_length=255, blank=True)
    column_name = models.CharField(max_length=255, blank=True)
    #column_index_from_dataTables_js = models.CharField(max_length=255, blank=True) 
    ### Not used --- Created another Model == temp_colIndex_for_Eda
    str_search = models.CharField(max_length=255, blank=True)
    str_replace = models.CharField(max_length=255, blank=True)

class pvbonds_csv_document(models.Model):
    """
    JIRA_ROHIT_PendingTask -- change this and the below - class csv_document(models.Model):
    make the CSV's upload in mySQL or PSQL directly as files without Django 
    then make CSV to PSQL in Utily.py read those CSV files and populate - PSQL or mySQL 
    """
    print("------HIT in DC_DASH_MODEL.py --class pvbonds_csv_document(models.Model):----------")
    print("      "*90)

    #csvfile = models.FileField(upload_to='documents/csv/%Y/%m/%d')
    #csvfile = models.FileField(upload_to='_DataBaseFile___/%Y/%m/%d___')
    pvBonds_csv_file = models.FileField(upload_to='_DataBaseFile_')
    pvBonds_csv_file_name = models.CharField(max_length=255, blank=True)
    
    pvBonds_dataset_name = models.CharField(max_length=255, blank=True)
    pvBonds_uploaded_at = models.DateTimeField(auto_now_add=True)
    # Unique Field with ID and name 
    pvBonds_unq_id_nameField = models.CharField(max_length=255, blank=True)
    
    
    def __str__(self):
        return self.pvBonds_csv_file_name    
        ## In the ADMIN Model Table - we get FILE -- Descriptions as FILE NAMES
        ## print("===========FROM===MODEL.py ==========",pvBonds_csv_file_name)
        ## If we give -- return self.csv_file -- we only get csvfile_OBJECTS

    def path_to_pvBonds_csv_file(self):
        path_of_file_pvBonds = str(MEDIA_ROOT)+"/"+str(self.pvBonds_csv_file)  ## this path is as seen below :--- 
        print("___FROM MODELS.py MEDIA_ROOT Path to CSV File_______",path_of_file_pvBonds)

        return path_of_file_pvBonds
        ### /home/dhankar/Desktop/dc_own/static_in_env/media_root/_DataBaseFile_/
        ### the MEDIA_ROOT as defined in setting.py and "csvfile" separated by a forward slash 
    
    def get_absolute_url(self):
        return reverse("call_pvbonds_landing_view",kwargs ={"pvBonds_unq_id_nameField" : self.pvBonds_unq_id_nameField})   ### JIRA_ROHIT_PendingTask Main TBD  
        #return reverse("call_eda_landing_view",kwargs ={"dataset_name" : self.dataset_name }) ## dataset_name - can be DUPLICATES
        #return "someurl/%s/" %(self.id)

    # def get_absolute_url_for_DROP_Table(self):
    #     return reverse("call_drop_table_psql_view",kwargs ={"unq_id_nameField" : self.unq_id_nameField })   ### JIRA_ROHIT_PendingTask Main TBD  
    
    # # def get_absolute_url_for_DELETE_Table(self):
    #     return reverse("call_eda_landing_view",kwargs ={"unq_id_nameField" : self.unq_id_nameField })   ### JIRA_ROHIT_PendingTask Main TBD  
    



class csv_document(models.Model):
    """
    This Model just stores STRINGS for CSV FileName and DataSetName --- its not the REAL DATASETS.
    The actual PSQL - those are going directly to PSQL 
    If we delete RECORDS here - we need to Delete DataSets in the PSQL using commands below- 
    #
    $ sudo su - postgres
    postgres=# \connect dc_dash_newspaper
    dc_dash_newspaper=# \list+
    dc_dash_newspaper=# SELECT * FROM dataset_name;
    #
    """
    #csvfile = models.FileField(upload_to='documents/csv/%Y/%m/%d')
    #csvfile = models.FileField(upload_to='_DataBaseFile___/%Y/%m/%d___')
    csv_file = models.FileField(upload_to='_DataBaseFile_')
    csv_file_name = models.CharField(max_length=255, blank=True)
    dataset_name = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Unique Field with ID and name 
    unq_id_nameField = models.CharField(max_length=255, blank=True)
    
    
    def __str__(self):
        return self.csv_file_name    
        ## In the ADMIN Model Table - we get FILE -- Descriptions as FILE NAMES
        ## If we give -- return self.csv_file -- we only get csvfile_OBJECTS

    def path_to_csv_file(self):
        path_of_file= str(MEDIA_ROOT)+"/"+str(self.csv_file)  ## this path is as seen below :--- 
        #print("___FROM MODELS.py MEDIA_ROOT Path to CSV File_______",path_of_file)
        return path_of_file
        ### /home/dhankar/Desktop/dc_own/static_in_env/media_root/_DataBaseFile_/
        ### the MEDIA_ROOT as defined in setting.py and "csvfile" separated by a forward slash 
    
    def get_absolute_url(self):
        return reverse("call_eda_landing_view",kwargs ={"unq_id_nameField" : self.unq_id_nameField })   ### JIRA_ROHIT_PendingTask Main TBD  
        #return reverse("call_eda_landing_view",kwargs ={"dataset_name" : self.dataset_name }) ## dataset_name - can be DUPLICATES
        #return "someurl/%s/" %(self.id)

    def get_absolute_url_for_DROP_Table(self):
        """
        JIRA_ROHIT_PendingTask -- Check if this method still works 
        """
        return reverse("call_drop_table_psql_view",kwargs ={"unq_id_nameField" : self.unq_id_nameField })   ### JIRA_ROHIT_PendingTask Main TBD  
    
    # def get_absolute_url_for_DELETE_Table(self):
    #     return reverse("call_eda_landing_view",kwargs ={"unq_id_nameField" : self.unq_id_nameField })   ### JIRA_ROHIT_PendingTask Main TBD  
    

    


class SqlQueryStr(models.Model):
    limit_records = models.TextField(blank=True)
    table_name = models.TextField(blank=True)
    new_table_name = models.TextField(blank=True)
    table_col1_name = models.TextField(blank=True)
    table_col1_type = models.TextField(blank=True)
    table_col2_name = models.TextField(blank=True)
    table_col2_type = models.TextField(blank=True)
    table_col3_name = models.TextField(blank=True)
    table_col3_type = models.TextField(blank=True)
    table_col4_name = models.TextField(blank=True)
    table_col4_type = models.TextField(blank=True)
    table_col5_name = models.TextField(blank=True)
    table_col5_type = models.TextField(blank=True)
    table_col6_name = models.TextField(blank=True)
    table_col6_type = models.TextField(blank=True)
    sql_query_input = models.TextField(blank=True)

    def clean(self):
        # MAIN -- SOURCE -- https://stackoverflow.com/questions/2151966/conditionally-require-only-one-field-in-django-model-form
        if self.table_name == '':
            self.table_name = self.new_table_name
            self.limit_records = "100"
            print("FROM MODELS ------------if self.table_name == EMPTY")
            #raise ValidationError('Display Table Name empty-- using == new_table_name.')
        
        
    
    #







## Getting this from == python manage.py inspectdb
#### THIS DOESNT WORK AS --- PANDAS --- dataFrame.to_sql == FAILS 
## the Data Ingress using --- dataFrame.to_sql --- requires Migrations etc and the DB Table gets created in SCHEMA Public 
## But the Corresponding MODEL in the MODELS.py does not get created. 


# class NameDfPandas2(models.Model):
#     #index = models.BigIntegerField(unique=True , primary_key=True)
#     index = models.BigIntegerField(primary_key=True)
#     col11 = models.BigIntegerField(db_column='Col11', blank=True, null=True)  # Field name made lowercase.
#     col21 = models.BigIntegerField(db_column='Col21', blank=True, null=True)  # Field name made lowercase.
#     col31 = models.BigIntegerField(db_column='Col31', blank=True, null=True)  # Field name made lowercase.
#     col41 = models.BigIntegerField(db_column='Col41', blank=True, null=True)  # Field name made lowercase.
#     col51 = models.BigIntegerField(db_column='Col51', blank=True, null=True)  # Field name made lowercase.
#     col61 = models.BigIntegerField(db_column='Col61', blank=True, null=True)  # Field name made lowercase.
#     col71 = models.BigIntegerField(db_column='Col71', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = True ## This comes in a FALSE when created by df.to_sql using psycopg2 
#         db_table = 'name_df_pandas2'

"""
Defaults to True, meaning Django will create the appropriate database tables in migrate or as part of 
migrations and remove them as part of a flush management command.
That is, Django manages the database tables’ lifecycles.

If False, no database table creation or deletion operations will be performed for this model. 
This is useful if the model represents an existing table or a database view that has been created by some other means.
"""


class model_init_lnkd(models.Model):
    designation = models.TextField(blank=True)
    Org_Name = models.TextField(blank=True)
    Geo_City = models.TextField(blank=True)
    Geo_Country = models.TextField(blank=True)
    college = models.TextField(blank=True)
    university = models.TextField(blank=True)
    createdStr_lnkd = models.TextField(blank=True) ## Concat String from Above. 
    SearchPortal = models.TextField(blank=True) 
    TimeStamp = models.TextField(blank=True)
    
    def __unicode__(self): #def __str__(self): ## https://docs.djangoproject.com/en/1.11/topics/python3/
        return self.createdStr_lnkd
        
class model_scrape_lnkd(models.Model):
    #First_Name':frst_nam_ls,'Middle_Name':mid_nam_ls,'Last_Name':last_nam_ls,'LinkdeIn':lnkd_profile_urls_ls})  
    First_Name = models.TextField(blank=True)
    Middle_Name = models.TextField(blank=True)
    Last_Name = models.TextField(blank=True)
    LinkdeIn = models.TextField(blank=True)
    Organization = models.TextField(blank=True)
    designation = models.TextField(blank=True)
    college = models.TextField(blank=True)
    university = models.TextField(blank=True)
    City = models.TextField(blank=True)
    Country = models.TextField(blank=True)
    TimeStamp = models.TextField(blank=True)
    
    def __unicode__(self): #def __str__(self): ## https://docs.djangoproject.com/en/1.11/topics/python3/
        return self.First_Name




class model_ScrapeTracxn(models.Model):
    Org_NAME = models.TextField(blank=True) 
    Org_URL = models.TextField(blank=True) 
    Org_NAME_Others = models.TextField(blank=True) 
    Org_URL_Others = models.TextField(blank=True)
            
    #Org_YEAR = models.TextField(blank=True) 
    #Org_CITY = models.TextField(blank=True) 
    #Org_COUNTRY = models.TextField(blank=True) 
    #Org_NEWS = models.TextField(blank=True) 
    TimeStamp = models.TextField(blank=True) 

    def __unicode__(self): #def __str__(self): ## https://docs.djangoproject.com/en/1.11/topics/python3/
        return self.Org_NAME
    

class model_SearchTracxn(models.Model):
    initSearchStr = models.TextField(blank=True) #
    initSearchStrTracxn = models.TextField(blank=True) #
    SearchPortal = models.TextField(blank=True) #
    TimeStamp = models.TextField(blank=True) #

    def __unicode__(self): #def __str__(self): ## https://docs.djangoproject.com/en/1.11/topics/python3/
        return self.initSearchStrTracxn
        #return self.initSearchStr

class news_startup_1(models.Model):  #
    ORG_Name = models.TextField(blank=True) ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    ORG_URL = models.TextField(blank=True) 
    ENG_Levl = models.TextField(blank=True)
    LinkedIn_URL = models.TextField(blank=True) 
    ORG_Image = models.TextField(blank=True) 
    REG_Coy = models.TextField(blank=True) 
    COY_Stage = models.TextField(blank=True) 
    ORG_Industry = models.TextField(blank=True) 
    ORG_Sector = models.TextField(blank=True) 
    ORG_loca = models.TextField(blank=True) 
    ORG_AboutMe = models.TextField(blank=True) 
    TimeStamp = models.TextField(blank=True) 

    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    #objects = ProductManager()

    def __unicode__(self): #def __str__(self):
        return self.ORG_Name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD


    
    
    
    
    
    
    
    
    
    
    
"""    
    def get_absolute_url(self):
        return reverse("address-update", kwargs={"slug": self.slug})
    
    def path_to_csv_file(self):
        return str(self.csvfile)   ## Here -- csvfile -- is the Model Field from above. 
        
    def __unicode__(self): #def __str__(self):
        return self.csvfile
"""
    
"""
class Document(models.Model):
    csvfile = models.FileField(upload_to='documents/csv/%Y/%m/%d')
    description = models.CharField(max_length=255, blank=True)
    #uploaded_at = models.DateTimeField(auto_now_add=True,default=2017,12,21)
    uploaded_at = models.DateTimeField(auto_now_add=True,default=datetime.date.today())
"""


class model_1b_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name

    
class data_table_1b(models.Model):  ## 1 to 7 Columns
    f1 = models.TextField(blank=True) ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField(blank=True) ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    # f3 = models.TextField(blank=True)
    # f4 = models.TextField(blank=True) 
    # f5 = models.TextField(blank=True) 
    
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    #objects = ProductManager()

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD




from django.contrib.postgres.fields import ArrayField ## Not yet being used -- TBD 

class model_1_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    f2 = models.CharField(max_length=200,blank=True)
    f3 = models.CharField(max_length=200,blank=True)
    f4 = models.CharField(max_length=200,blank=True)
    f5 = models.CharField(max_length=200,blank=True)
    f6 = models.CharField(max_length=200,blank=True)
    f7 = models.CharField(max_length=200,blank=True)
    f8 = models.CharField(max_length=200,blank=True)

    
    def __unicode__(self): #def __str__(self):
        return self.name

    
class data_table_1a(models.Model):  ## 1 to 7 Columns
    f1 = models.TextField(blank=True) ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField(blank=True) ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f3 = models.TextField(blank=True)
    f4 = models.TextField(blank=True) 
    f5 = models.TextField(blank=True) 
    f6 = models.TextField(blank=True) 
    f7 = models.TextField(blank=True) 
    #f11 = ArrayField(models.CharField(max_length=200),default=list) ### default=[] OR default = list ?? 
    ## https://www.reddit.com/r/django/comments/4v7jpy/django_orm_arrayfield/
    
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    #objects = ProductManager()

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD

        
        
        
        
        
        
class model_2_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
        
        
class data_table_2(models.Model):  ## 1 to 8 Columns
    f1 = models.TextField(blank=True)   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField(blank=True) 
    f3 = models.TextField(blank=True) 
    f4 = models.TextField(blank=True) 
    f5 = models.TextField(blank=True) 
    f6 = models.TextField(blank=True) 
    f7 = models.TextField(blank=True) 
    f8 = models.TextField(blank=True) 
    
    
    active = models.BooleanField(default=True)

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_2", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD


        
class model_3_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_3(models.Model):  ## 1 to 9 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    

    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_3", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD

        
        
        
class model_4_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_4(models.Model):  ## 1 to 10 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS     
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    
    
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_4", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD



        
class model_5_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_5(models.Model):  ## 1 to 11 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        
        

        
        
        
class model_6_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_6(models.Model):  ## 12 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        


class model_7_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_7(models.Model):  ## 13 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        
        


class model_8_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_8(models.Model):  ## 14 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD

        

class model_9_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_9(models.Model):  ## 15 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD

        
        
               
class model_10_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_10(models.Model):  ## 16 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        
        
               
class model_11_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_11(models.Model):  ## 17 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    f17 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        
        
        
        
class model_12_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_12(models.Model):  ## 18 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    f17 = models.TextField() 
    f18 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        
        
        
        
        
class model_13_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_13(models.Model):  ## 19 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    f17 = models.TextField() 
    f18 = models.TextField() 
    f19 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        
        
        
        
        
class model_14_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_14(models.Model):  ## 20 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    f17 = models.TextField() 
    f18 = models.TextField() 
    f19 = models.TextField() 
    f20 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        
        
        
        
        
class model_15_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_15(models.Model):  ## 21 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    f17 = models.TextField() 
    f18 = models.TextField() 
    f19 = models.TextField() 
    f20 = models.TextField() 
    f21 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
      
    
class model_16_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_16(models.Model):  ## 22 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    f17 = models.TextField() 
    f18 = models.TextField() 
    f19 = models.TextField() 
    f20 = models.TextField() 
    f21 = models.TextField() 
    f22 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        
    
        
        
class model_17_col_names(models.Model):  ## for storing COLUMN Names from XLS Uploads
    
    f1 = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self): #def __str__(self):
        return self.name
        
class data_table_17(models.Model):  ## 23 Columns
    f1 = models.TextField()   ## to have MAX Length -- keep TEXT FIELD with NO OPTIONS 
    f2 = models.TextField() 
    f3 = models.TextField() 
    f4 = models.TextField() 
    f5 = models.TextField() 
    f6 = models.TextField() 
    f7 = models.TextField() 
    f8 = models.TextField() 
    f9 = models.TextField() 
    f10 = models.TextField()
    f11 = models.TextField()
    f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    f17 = models.TextField() 
    f18 = models.TextField() 
    f19 = models.TextField() 
    f20 = models.TextField() 
    f21 = models.TextField() 
    f23 = models.TextField() 
    
        
    active = models.BooleanField(default=True)     ## ACTIVE MIGRATED SUCCESS 

    def __unicode__(self): #def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse("dhank_reverse_url_5", kwargs={"pk": self.pk}) # Call Back - dhank_reverse_url ## TBD
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
"""
f12 = models.TextField() 
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    f17 = models.TextField() 
    f18 = models.TextField() 
    f19 = models.TextField() 
    f20 = models.TextField()
    f21 = models.TextField()
    f22 = models.TextField()
    f23 = models.TextField() 
    f24 = models.TextField() 
    f25 = models.TextField() 
    f26 = models.TextField() 
    f27 = models.TextField() 
    f28 = models.TextField() 
    f29 = models.TextField() 
    f30 = models.TextField() 
    
    
    f13 = models.TextField() 
    f14 = models.TextField() 
    f15 = models.TextField() 
    f16 = models.TextField() 
    f17 = models.TextField() 
    f18 = models.TextField() 
    f19 = models.TextField() 
    f20 = models.TextField()
    f21 = models.TextField()
    f22 = models.TextField()
    f23 = models.TextField() 
    f24 = models.TextField() 
    f25 = models.TextField() 
    f26 = models.TextField() 
    f27 = models.TextField() 
    f28 = models.TextField() 
    f29 = models.TextField() 
    f30 = models.TextField() 
    f31 = models.TextField()
    f32 = models.TextField()
    f33 = models.TextField()
    f34 = models.TextField() 
    f35 = models.TextField() 
    f36 = models.TextField() 
    f37 = models.TextField() 
    f38 = models.TextField() 
    f39 = models.TextField() 
    f40 = models.TextField() 
    
    

"""