import codecs
import re
import numpy as np
import pandas as pd
import math
from django.conf import settings
from django.http import JsonResponse ### DHANK ---FEB19
from collections import OrderedDict
from sqlalchemy import create_engine
import psycopg2
import io , os 
from .models import *

from django.db import connection, DatabaseError, IntegrityError, OperationalError

import datetime
dt_now = str(datetime.datetime.now())
dt_all_now = datetime.datetime.now()
minute_now = dt_all_now.minute
second_now = dt_all_now.second




def createDuplicate_Col(df,colNameFromJS): #
    """
    Used in JS Funcs as Listed Below == 
    a/ eda_action_MatchSimilarText_Fuzz.html
    b/ eda_action_SearchAndReplace.html

    Not of use in JS Funcs as Listed Below == 
    a/ eda_SideBar.html = <table id="dataTable_psqlTables_merge"
    b/ eda_SideBar.html =  <table id="dataTable_PSQL_ConnStatus"
    
    """
    old_col_name = str(colNameFromJS)
    # Not DONE == Check if newColName generated as a dupColName = Already Exists - Not required in DC, we generate newColName with TimeStamps
    newColName = old_col_name + "_" + str(dt_now) + str(minute_now) + str(second_now)
    df[newColName] = df[old_col_name] # this here Adds OldCol with New name as a New Col
    return df

def convert_col_dType(df_col_dType_str):
    """
    # Own FUNC == convert_col_dType== in dc_eda_funcs.py File 
    Converts Python dTypes of CSV to DF - to PSQL dTypes. 
    With converted dTypes CSV Data saved in PSQL Tables.
    1/ Prefer int32 for Unsigned INT's , in place of int64 , for memory optimization. 
    2/ Avoid defaulting to FLOATS if INT in Columns
    """
    float64 = "float64"
    int64 = "int64"
    int32 = "int32" ## TBD -- not sure what we call bigint in - PSQL terms. 
    bigint = "bigint"
    varchar = "varchar"
    #object = "object"  ## Not required as == df_col_dType_str - has been converted to STRING in utily.py  
    object_str = "object"
    #
    ## JIRA_ROHIT_PendingTask #Further Reading Required ---  Own code for - python OBJECT to be called an - object_str - which is a STRING
    if "obj" in df_col_dType_str:
        df_col_dType_str == object_str

    dict_faster = {
        float64:"float",
        int64:"bigint",
        object_str:"varchar"
    }
    #dict_faster ---- Last ELEMENT no CLOSING COMMA.
    #
    try:
        col_dtype = dict_faster.get(str(df_col_dType_str))
        #print("--AAAAAAAAAAAAAAAAAAAAA========-FILE == dc_eda_funcs.py ----col_1_dtype------CODED for PSQL ----",col_dtype)
        #print("    "*90)
    except Exception as e:
            print("EXCEPTION from --FILE ==-dc_eda_funcs.py--FUNC==- convert_col_dType",e)
            print("    "*90)
    return col_dtype

def del_model_temp_dataSetName_dfFromEDA(): ## NO ARGS ?? NO KWARGS ?? No SELF ?? 
    """
    DELETE == temp_dataSetName_dfFromEDA
    as and when we CREATE == temp_dataSetName_for_EDALanding
    """
    with connection.schema_editor() as schema_editor:
        schema_editor.delete_model(temp_dataSetName_dfFromEDA)
    
def create_model_temp_dataSetName_dfFromEDA():
    """
    CREATE == temp_dataSetName_dfFromEDA
    """
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(temp_dataSetName_dfFromEDA)

def del_model_temp_colIndex_for_Eda(): ## NO ARGS ?? NO KWARGS ?? No SELF ?? 
    """
    DELETE == temp_colIndex_for_Eda
    as and when we CREATE == temp_dataSetName_for_EDALanding
    """
    with connection.schema_editor() as schema_editor:
        schema_editor.delete_model(temp_colIndex_for_Eda)
    
def create_model_temp_colIndex_for_Eda():
    """
    CREATE == temp_colIndex_for_Eda
    """
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(temp_colIndex_for_Eda)

def save_postEdaDataSet(df_from_eda,current_dataset_name):
    """
    AutoSave DF after every EDA_Action 
    """
    psql_user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']

    database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
        user=psql_user,
        password=password,
        database_name=database_name,
    )
    engine = create_engine(database_url, echo=False) ##
    ## echo=True --- To Print DB Actions etc.
    # # JIRA_ROHIT_PendingTask --- this  Print DB Actions etc. actually happens after the ENGINE is called below 
    ## df_from_eda.to_sql(temp_dataset_name,conn,
    ## Need to change to ECHO == TRUE -- to check things like LowerCased TABLE names etc etc ERRORS
    ## SO Source Main -- https://stackoverflow.com/questions/695289/cannot-simply-use-postgresql-table-name-relation-does-not-exist
    #
    #
    
    conn = engine.connect() 
    ## Source == https://docs.sqlalchemy.org/en/latest/core/connections.html
    schema_default_public = "public"
    temp_dataset_name = current_dataset_name + str("_n_")
    df_from_eda.to_sql(temp_dataset_name,conn,str(schema_default_public),if_exists='replace',index=False) ## OK ?? 
    print("--DB Actions Printed below with -- engine echo == TRUE --- to see if New TABLE Created or NOT --temp_dataset_name==-",temp_dataset_name)
    print("        "*90)
    #2019-03-02 18:31:45,831 INFO sqlalchemy.engine.base.Engine INSERT INTO public."csv_Modal_1_zeus1"
    #csv_Modal_1_zeus1



    #df_from_eda.to_sql(temp_dataset_name,conn,str(schema_default_public), if_exists='replace',index=True) 
    # PANDAS ERROR -- Starts Creating same iNDEX Records again ..
    #ValueError: duplicate name in index/columns: cannot insert level_0, already exists
    """
    File "/home/dhankar/anaconda2/envs/dc_info_venv/lib/python3.5/site-packages/pandas/core/internals.py", line 4338, in insert
    raise ValueError('cannot insert {}, already exists'.format(item))
    ValueError: cannot insert level_0, already exists
    """
    #
    ## Source --- http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
    
    return temp_dataset_name

def tableAuReports_Metrics(df):
    """
    tableAuReports_Metrics
    Returns 
    """
    print("=========IN HERE =========ZZZ=====ZAAAAAAA=======")
    ls_ColTableAuReports_Metrics = []
    ls_ColTableAuReports_Dimensions = []
    ls_Col_Lens = []

    dfColNames = list(df.columns.values)
    #print(dfColNames)
    len_dfColNames = len(dfColNames)
    myDtypeList = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

    for k in range(len_dfColNames):
        getCol_df = df[df.columns[k]]
        #print("=TYPE===getCol_df=========",type(getCol_df)) ## OK == <class 'pandas.core.series.Series'>
        #print("=TYPE===getCol_df======NAME===",getCol_df.name) #
        # # Getting each SERIES Name == https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.name.html#pandas-series-name
        
        col_dtype = getCol_df.dtype
        #print(col_dtype)

        if col_dtype in myDtypeList:
            ls_ColTableAuReports_Metrics.append(str(getCol_df.name))
            #print("-========AAAAA==========ls_ColTableAuReports_Metrics====",ls_ColTableAuReports_Metrics)
        else:
            ls_ColTableAuReports_Dimensions.append(str(getCol_df.name))
            #print("-========AAAAA==========ls_ColTableAuReports_Dimensions====",ls_ColTableAuReports_Dimensions)
            
    #print("-========AAAAA="*90)

    return ls_ColTableAuReports_Metrics , ls_ColTableAuReports_Dimensions
    






def eda_modal_summary_stats(df):
    """
    Method gets called in file >> utily.py >> def modal_data_summary_stats(self):
    Actual path to method = nginx_demo_django/dc_dash/dc_eda_funcs.py
    Returns DF with == Mean , Median , Mode for each Column 
    """
    ls_Col_Dtypes = []
    ls_Col_Lens = []
    ls_Col_means = []
    ls_Col_median = []
    ls_max_val = []
    ls_min_val = []
    ls_quantile_val_25 = []
    ls_quantile_val_50 = []
    ls_quantile_val_75 = []


    # get all DF Column Names 
    dfColNames = list(df.columns.values)
    #print("===dc_eda_funcs.py ===eda_modal_summary_stats=====dfColNames==========",dfColNames)

    # get Len of all DF Column Names 
    len_dfColNames = len(dfColNames)
    #print("--==dc_eda_funcs.py ===eda_modal_summary_stats------len_dfColNames----",len_dfColNames)

    # for each DF Column get Summary Stats 
    

    for k in range(len_dfColNames):
        #getCol = df.iloc[:,[k]] ## Not Reqd
        #print(type(getCol)) ## <class 'pandas.core.frame.DataFrame'>
        #getCola = df.loc[:,k] ## Using .loc with == k == which is INT Index - Not OK . 
        #print(type(getCola))
        # ERROR == TypeError: cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [0] of <class 'int'>
        #
        getCol_df = df[df.columns[k]]
        #print(type(getCol_df)) ## <class 'pandas.core.series.Series'>
        #print(getCol_df.shape) ## TUPLE == (length_of_column,)
        #print(getCol_df.size) ## OK Size is LENGTH of COLUMN 
        ls_Col_Lens.append(getCol_df.size)
        #print("    "*90)
        #print(getCol_df) ## OK - Each Column as SERIES with INDEX 

        col_dtype = getCol_df.dtype
        #print("----------SELECTED COLUMN Dtype is -----------",col_dtype)
        ls_Col_Dtypes.append(str(col_dtype))
        #
        myDtypeList = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        
        
        if col_dtype in myDtypeList:
            # print(getCol_df.mean()) ## OK Size is LENGTH of COLUMN 
            # print("    "*90)
            ls_Col_means.append(round(getCol_df.mean(),2))
            ls_Col_median.append(round(getCol_df.median(),2))
            ls_max_val.append(round(getCol_df.max(),2))
            ls_min_val.append(round(getCol_df.min(),2))
            ls_quantile_val_25.append(round(getCol_df.quantile(q=0.25),2))
            ls_quantile_val_50.append(round(getCol_df.quantile(q=0.50),2))
            ls_quantile_val_75.append(round(getCol_df.quantile(q=0.75),2))
        else:
            ls_Col_means.append("Non Numeric - No MEAN")
            ls_Col_median.append("Non Numeric - No MEDIAN")
            ls_max_val.append("Non Numeric - No MAX Value")
            ls_min_val.append("Non Numeric - No MIN Value")
            ls_quantile_val_25.append("No Quantiles")
            ls_quantile_val_50.append("No Quantiles")
            ls_quantile_val_75.append("No Quantiles")


        #JIRA_ROHIT_PendingTask -- TBD -- Unique Count etc ...
        # col_unq_cnt = len(getCol.unique())
        #print("---------col_unq_cnt------------",col_unq_cnt)
    
    ## Below MAINTAINS ORDER of COLUMNS --- COL Names to be SAME as Given in DICT part of below line of Code.
    summaryStats_df = pd.DataFrame({'Col. Name':dfColNames,'Col. MAX.':ls_max_val,'Col. MIN.':ls_min_val,'25%':ls_quantile_val_25,'50%':ls_quantile_val_50,'75%':ls_quantile_val_75,  'Col. Mean':ls_Col_means,'Col. Median':ls_Col_median,'Col. Length':ls_Col_Lens,'Col. DataType':ls_Col_Dtypes} , \
    columns=['Col. Name','Col. MAX.','Col. MIN.','25%','50%','75%', 'Col. Mean','Col. Median','Col. Length','Col. DataType'])  
    
    ## This below DOESNT Maintain ORDER of COLUMNS 
    #summaryStats_df = pd.DataFrame({'Column Mean':ls_Col_means,'Column Length':ls_Col_Lens,'Column DataTypes':ls_Col_Dtypes})  
    
    
    #     # #df_xls = pd.DataFrame(OrderedDict({'ZaaCol_A':ls_col_1,'MCol_B':ls_col_2,'BCol_C':ls_col_3,'XCol_3':ls_col_4,'Col_E':ls_col_5,'Col_F':ls_col_6},index=[1]))
    #     #df_xls = pd.DataFrame(data=[ls_col_1,ls_col_2,ls_col_3,ls_col_4,ls_col_5,ls_col_6],columns=['ZaaCol_A','MCol_B','BCol_C','XCol_3','Col_E','Col_F'])

    #     #df_xls = pd.DataFrame(data=[ls_col_1,ls_col_2,ls_col_3],columns=['ZaaCol_A','MCol_B','BCol_C'])
    #     df_xls = pd.DataFrame(data=[ls_col_1,ls_col_2,ls_col_4],columns=['MCol_B','BCol_MM','ZaaCol_A'],index=["Row_1","Row_2","Row_3"])
    

    return summaryStats_df


#def groupby_categorical_cols(df):
"""
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
"""








def showCategoricalCols(df):
    df_only_bool = df.select_dtypes(include='bool')
    df_only_float64 = df.select_dtypes(include='float64')
    df_only_float32 = df.select_dtypes(include='float32')
    df_only_int32 = df.select_dtypes(include='int32')
    df_only_int64 = df.select_dtypes(include='int64')
    df_only_category = df.select_dtypes(include=['category'])
    # print("----df_only_bool---------",df_only_bool)
    # print("     "*90)
    # print("-------df_only_category------",df_only_category)
    # print("     "*90)
    # print("-------df_only_float64------",df_only_float64)
    return df_only_category


def matchSimilarText(df,fuzziness,str_to_compare_with,column_index): #
    """
    Fuzzy String Matching ---- Match Similar Text --- Dhankar - Feb 19
    eda_action_MatchSimilarText_Fuzz.html

    Name : matchSimilarText
        Description : Fuzzy distance string matching . 
    Args:
        Param1: cell_value :- cell value of dataFrame. 
        Param2: parms :- 
                    fuzziness :- Its the Levenshtein distance value , it represents the number of insertions, 
                                deletions, and subsititutions required to change one word to another.
                    use_with :- Column [selected_column] or Value [Cell Value] . 
                    reference :- The String to be compared with. 
                    selected_column :- The Column chosen whose Cells need to be compared with. 
     Returns: 
        The object which is result of computation. 
    Raises:
        ValueError: As and when there is an Exception.

    Inner Function -1 :
        Function Name: match_similar_textData 
            Function Parameter: cell_value,fuzziness,use_with,reference,selected_column. 
            Return Output :

    Inner Function -2 : ## JIRA_ROHIT_PendingTask --- TBD 
        Function Name: match_similar_textCol
            Function Parameter: df,params
            Return Output :
                   
    """

    """
    IMPORTANT --- OLD BUGGGY CODE ??
    #print("______parms___",parms)

    ## ______parms___ {'reference': '', 'selected_column': 'col_2', 'column_name': 'col_2', 
    # 'use_with': 'other_column', 'fuzziness': '2'}
    ##### Rohit - Need to change -- cant have both same = 'selected_column': 'col_2', 'column_name': 'col_2',

    ## ______parms___ {'selected_column': None, 'fuzziness': '1', 'reference': 'DATE', 
    # 'column_name': 'col_4', 'use_with': 'value'}
    ##### Rohit - Need to change -- cant have  'selected_column': None,
    """

    str_to_compare_with = str(str_to_compare_with) ## From - Django FORM
    fuzziness = int(fuzziness) ## From - Django FORM
    location_col = int(column_index) ## From JS onClick
    idx = location_col + 1 
    dfColNames = list(df.columns.values)
    col_name = str(dfColNames[location_col])
    #
    dt_all_now = datetime.datetime.now()
    minute_now = dt_all_now.minute
    print("----------minute_now-------------",minute_now)
    second_now = dt_all_now.second
    print("----------second_now-------------",second_now)
    #
    #new_col_name = str(col_name) + "_MST_#Col" + str(idx) + "_" +str(minute_now) +str(second_now)
    new_col_name = str(col_name) + "_MST#" +str(minute_now) +str(second_now)
    new_col  = df[col_name].apply(lambda x: match_similar_textData(x,fuzziness,str_to_compare_with))
    df.insert(loc=idx, column=new_col_name, value=new_col)
    #print("----------df-----FROM MATCH SIMILAR TEXT-------",df)
    return df


def match_similar_textData(cell_value,fuzziness,str_to_compare_with):
    """
    Name : match_similar_textData
        Description : Fuzzy distance string matching . 
    
    Args:
        Param1: cell_value :- Cell value of dataFrame. 
        Param2: fuzziness  :- Its the Levenshtein distance value , it represents the number of insertions, 
                             deletions, and subsititutions required to change one word to another.
        Param3: use_with   :- Column or Value . 
        Param4: reference  :- The String to be compared with. 
        Param5: selected_column :- The Column chosen whose Cells need to be compared with. 
        
     Returns: 
        The object which is result of computation. 

    Raises:
        ValueError: As and when there is an Exception.

    Inner Function:
        Function Name: text_distance
            Function Parameter: 
            Return Output :
    """
    fuzz = int(fuzziness)
    out_put_code = " "

    try:
        if((cell_value != '' or cell_value != None)):
            leven_dist = math.floor(text_distance(cell_value,str_to_compare_with))

            if leven_dist == 0:
                if fuzz >= 0:
                    out_put_code = "TRUE"

            elif(leven_dist):
                if fuzz >= int(leven_dist):
                    out_put_code = "TRUE"
                elif fuzz < int(leven_dist):
                    out_put_code = "FALSE"     
            else:
                out_put_code = "FALSE"
        return out_put_code
    except Exception as e:
        print(e)
        raise e


import numpy as np

def text_distance(seq1, seq2):  
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1

    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x): 
        matrix [x, 0] = x

    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:

                matrix [x,y] = min(
                    matrix[x-1, y] + 1,

                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(matrix[x-1,y] + 1, matrix[x-1,y-1] + 1, matrix[x,y-1] + 1 )
    leven_dist = matrix[size_x - 1, size_y - 1]
    return leven_dist

def match_similar_textCol(selected_column,col):
    """
    Name : match_similar_textCol
        Description : Fuzzy distance string matching . 
    
    Args:
        Param1: df :- DataFrame 
        Param2: params :- 
                    df_col_to_match_with :- Column whose Cells are "Target" of matching values.
                    df_col_to_match :- Column whose Cells are "Source" of matching values. 
       
    Returns: 
        The object which is result of computation. 

    Raises:
        ValueError: As and when there is an Exception.

    Inner Function:
        Function Name: NONE
            Function Parameter: 
            Return Output :
    """
    try:
        if(selected_column != None):
            print("__to be done ==",selected_column)
            print("__to be done ==",col)
            return col
    except Exception as e:
        print(e)
        #raise e



def searchAndReplace(df,new_column,column_index,operation_type,str_search,str_replace):
    """
    searchAndReplace
    FOO_JIRA_ROHIT -- Add a PARAM == REGEX - where in place of str_search - we can enter a REGEX ...
    """
    #col = params['column_name']
    ### Col Names Saved in PSQL as - col_1 , col_2 etc ...
    ## Index(['srno', 'col_1', 'col_2', 'col_3', 'col_4'], dtype='object')

    # col = str(column_name).lower()
    # location_col = df.columns.get_loc(col)

    location_col = int(column_index)
    idx = location_col + 1 
    dfColNames = list(df.columns.values)
    col_name = str(dfColNames[location_col])
    #print("---------dfColNames[location_col]----------",dfColNames[location_col])
    #getColumn = df.iloc[:,[location_col]] ## All ROWS of Location_col ??
    # print("------------JIRA_ROHIT_PendingTask TBD ----------getColumn------------",getColumn)
    # print("       "*90)
    #
    # getType = getColumn.dtype
    # print("----------SELECTED COLUMN Dtype is -----------",getType)
    # dTypesArray = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    # dfColNames = list(df.columns.values)

    counter_for_new_col_name = 0

    if new_column == "new_col":
        new_colmn  = df[col_name].apply(lambda x: search_replace_data(str(x),operation_type,str_search,str_replace))
        #new_colmn = pd.to_numeric(new_col, errors='ignore') ## Coerce New COL Dtype == to_numeric
        #new_col_name = str(col_name) + "_" + str(idx)
        
        #if new_colmn != None: ### ERROR --- ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
        #if not new_colmn.empty: #
        counter_for_new_col_name += 1
        print("-----------counter_for_new_col_name---------",counter_for_new_col_name)
        
        #dt_now = str(datetime.datetime.now())
        dt_all_now = datetime.datetime.now()
        minute_now = dt_all_now.minute
        print("----------minute_now-------------",minute_now)
        second_now = dt_all_now.second
        print("----------second_now-------------",second_now)

        new_col_name = str(col_name) + "_SR#" +str(minute_now)+str(second_now)+str(counter_for_new_col_name)
        print("-----------new_col_name-----------",new_col_name)
        print("   "*90)

        df.insert(loc=idx, column=new_col_name, value=new_colmn)
        #print("-----------df---NEW_COL--------",df)
        return df , new_col_name
    else:
        df[col_name] = df[col_name].apply(lambda x: search_replace_data(str(x), operation_type,str_search,str_replace))
        #df[col] = pd.to_numeric(df[col], errors='ignore')
        #print("-----------df---NO_NEW_COL------",df)
        new_col_name = "No New Column Created"
        return df , new_col_name

def search_replace_data(record_in_df,operation_type,user_input_str_to_search,user_input_str_to_replace): #
    """
    #def search_replace_data(record_in_df,operation_type,overwrite_entire_cell,user_input_str_to_search,user_input_str_to_replace): #
    """
    try:
        if((record_in_df != '' or record_in_df != None)):
            typ_rec_in_df = str(type(record_in_df))
            if "Timestamp" in typ_rec_in_df: 
                #raise EdaUserMessageException("  Got TimeStamp's in Column") ### TBD 
                print("----------EDA --search_replace_data- GOT Timestamp")
                pass
            
            if (operation_type == 'equals'):
                if (user_input_str_to_search == str(record_in_df)):
                    record_in_df = str(record_in_df).replace(str(user_input_str_to_search),str(user_input_str_to_replace))
                    return record_in_df
                else:
                    return record_in_df
            if (operation_type == 'contains'):
                if (user_input_str_to_search in str(record_in_df)):
                    record_in_df = record_in_df.replace(user_input_str_to_search,user_input_str_to_replace)
                    return record_in_df
                else:
                    return record_in_df
            if (operation_type == 'starts_with'):
                if(record_in_df.startswith(str(user_input_str_to_search))):
                    record_in_df = record_in_df.replace(user_input_str_to_search,user_input_str_to_replace)
                    return record_in_df
            if (operation_type == 'ends_with'):
                if(record_in_df.endswith(str(user_input_str_to_search))):
                    record_in_df = record_in_df.replace(user_input_str_to_search,user_input_str_to_replace)
                    return record_in_df

    except Exception as e: 
        print(e)
        #raise e 



######## DHANKAR --- extractStringPart

def getTextSubstrings(df,column_index,operation_type,regularExp,seperator,splitIntoPartsCount):
    #print("__________parms_____",parms)

    '''
    This method identifies the alpha-numeric part from a string and extracts the alpha-numeric data from the input string.
    Param1: data - a string object which contains a cell value of a column
    Param2: regularExp - a string object which contains the regular expression alphanumeric. This parameter is a part of user input.
    Param3: splitPart - an integer object which specifies in how many parts the input should be split. This parameter is a part of user input.
    Param4: seperator - a string object which contains a delimiter for the split string.
                        This would be used for single column output only and it is also a part of user input.
    Returns: a string object if output is single column, else returns a list of string
    '''

    #print("____AAAAAA_____parms============",parms)
    ## DHANKAR - JIRA_ROHIT_PendingTask --- FEB19 ---VALIDATION to cater for Empty Inputs like == splitIntoPartsCount == '' Django Form Submitted with NO PARTS INTEGER
    #  {'regex': '\\w+', 'separator': '__', 'column_name': 'col_1', 'extract_to': 'single', 'parts': ''}


    """
    Name : extractStringPart
    Args:
        Param1: regex :- 
        Param2: Pattern on the Frontend . 
                user_input_action_type :- 
                        contains :- 
                        equals :- 
                        strats_with :- 
                        ends_with :- 
                        regex :- 

        Param3: string_to_remove :- 
        Param4: column_name :- Column name of DataSet on which action is done.
        
     Returns: 
        The sub string returned after removing a matching value. 

    Raises:
        ValueError: As and when there is an Exception.

    Inner Function:
        Function Name: NONE
            Function Parameter: 
            Return Output :
                    
    """
    
    column_name = parms['column_name']
    extract_to = parms['extract_to']
    parts = parms['parts']
    regex = parms['regex']
    
    separator = parms['separator']
    column_name = df[column_name]

    ### MAIN -- TBD 
    # if regex or parts or separator == '':
    #     if regex == '':
    #         #
    #         # to be done 
    # #if regex | parts | separator == '':        
    #     #
    #     raise ValueError("Got a 'Blank Regex OR a Separator', enter a Valid Regex")

    
    if(extract_to == "single" ):
        df[parms['column_name']] = column_name.apply(single_extract,regex = regex,delimit =separator)
        return df

    elif(extract_to == "multiple"):
        col = parms['column_name']
        location_col = df.columns.get_loc(col)
        idy = location_col + 1
        

        try:
            result = column_name.apply(multi_extract,regex = regex,parts = parts)
            ### Check if above needs to be LAMBDA 

            mydf = pd.DataFrame(result.values.tolist(), index= result.index)
            dfcols_ls1 = df.columns.tolist()
            len_dfcols_ls1 = len(dfcols_ls1)
    
            mydf.columns = [str(column_name.name) + "_part_"+ str(i+1) for i in range(int(parts))]
            
            mydfcols_ls = mydf.columns.tolist()
            #print("______mydf.columns.tolist()_____",mydfcols_ls)
            len_mydfcols_ls = len(mydfcols_ls)
            #print("___AAAAAAA_____",type(mydf.columns)) ### pandas.core.indexes.base.Index

            df_concat = pd.concat([df,mydf],axis=1)
            #print("_____df_concat______",df_concat)

            df_concat_cols_ls = df_concat.columns.tolist()
            len_df_concat_cols_ls = len(df_concat_cols_ls)

            
            list_new_names = []

            for i in range(len_mydfcols_ls):
                new_name = getNewColName(str(df[col].name) + "_part_" + str(i+1) , dfcols_ls1) 
                list_new_names.append(new_name)
            #print("______list_new_names____",list_new_names)

            for i in range(len(list_new_names)):
            
                df_concat_cols_ls.remove(list_new_names[i])

            #print("__________df_concat_cols_ls_SEMI__FINAL ___",df_concat_cols_ls)
            for i in range(len(list_new_names)):

                df_concat_cols_ls.insert((idy+ i), list_new_names[i])

            #print("__________df_concat_cols_ls___FINAL ___",df_concat_cols_ls)

            df_concat = df_concat[df_concat_cols_ls] 

            return df_concat
        except Exception as e:
            raise e
    

    
def single_extract(text,regex,delimit = ""):
    try:
        text = str(text)

        p_list = re.findall(regex,text)
        word = delimit.join(p_list)
        return word
    except:
        return text

    
def multi_extract(text,regex,parts = None):
    
    if str(parts).isdigit() and int(parts)> 0:
        parts = int(parts)
        text = str(text)

        try:
            p_list = re.findall(regex,text)
            differene = len(p_list)-parts
            if differene == 0:
                return p_list
            elif differene < 0:
                new = [None for _ in range(abs(differene))]
                return p_list + new
            else:
                return p_list[:parts]         
        except:
            return [None for _ in range(parts)]
    else:
        raise ValueError ("parts should be in int and greater than 0")
#------------------------------------------------------------------








def extractEmailPart(df,param):
    '''
    This method identifies the email part from a string and the then splits the string on the basis of @ to separate id and domain from it.
    Param1: data - a string object which contains a cell value of a column
    Param2: regexpression - a string object which contains the regular expression for email. This parameter is part of code only, not from user input
    Returns: List of String
    '''
    try:
        col = param['column_name']
        location_col = df.columns.get_loc(col)
        idy = location_col + 1
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        result = df[col].apply(lambda x: extractEmail(x, EMAIL_REGEX)).apply(pd.Series) 
        
        mydf = pd.DataFrame(result.values.tolist(), index= result.index)
        ls_df_cols = df.columns.tolist()
        new_name = getNewColName(str(df[col].name) + "_Email_Part_1" + "_1", ls_df_cols)
        new_name1 = getNewColName(str(df[col].name) + "_Email_Part_2" + "_1", ls_df_cols)
        mydf.columns = [new_name,new_name1]
        df1 = pd.concat([df,mydf],axis=1)
        ls_df_cols.insert((idy),new_name)
        ls_df_cols.insert((idy+1),new_name1) 
        df1 = df1[ls_df_cols]
        return df1

    except Exception as e:
        raise e 

    

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


"""
Starts JIRA-DCA1-1--Extract_Email_Parts-Dinesh Chinnusamy


# def validateEmail(strEmail):
#     if re.match("(.*)@(.*).(.*)", strEmail):

#         return True
#     return False


# def writeFile(listData):
#     file = open(fileToWrite, 'w+')
#     strData = ""
#     for item in listData:
#         strData = strData + item + '\n'
#     file.write(strData)


# listEmail = []
# file = open(fileToRead, 'r')
# listLine = file.readlines()
# for itemLine in listLine:
#     item = str(itemLine)
#     for delimeter in delimiterInFile:
#         item = item.replace(str(delimeter), ' ')

#     wordList = item.split()
#     for word in wordList:
#         if (validateEmail(word)):
#             listEmail.append(word)

# if listEmail:
#     uniqEmail = set(listEmail)
#     print(len(uniqEmail), "emails collected!")
#     writeFile(uniqEmail)
# else:
#     print("No email found.")

# ns=[]

# delimiterInFile1 = [',']
# fileToRead1 = 'email.csv'
# listEmail1 = []
# file1 = open(fileToRead1, 'r')
# listLine1 = file1.readlines()
# for itemLine1 in listLine1:
#     item = str(itemLine1)
#     for delimeter in delimiterInFile1:
#         item = item.replace(str(delimeter), ' ')
#         s= item.split('@')
#         ns.append(s)


# print(ns)
# df = pd.DataFrame(ns, columns = ['Id' , 'Domain'])
# print(df)
# df.to_csv('email.txt',index=False)


ENDS-JIRA-DCA1-1--Extract_Email_Parts-Dinesh Chinnusamy
"""



"""
STARTS-JIRA-DCA1-5--Fill cells with value - fill a cell with value , which exists in any other cell -Dinesh Chinnusamy

path=('')
df = pd.read_csv(path)
def fill_cell(x):
    a=int(input('enter the row of the target cell :'))
    b=int(input('enter the column of the target cell :'))
    c=int(input('enter the row of the source cell :'))
    d=int(input('enter the column of the source cell :'))
    z=x.iloc[a,b]
    x.iloc[a,b]=x.iloc[c,d]
    print(z, 'is replaced with', x.iloc[c, d])
    #For modifying the input csv file
    #x.to_csv(path,index=False)
fill_cell(df)

ENDS-JIRA-DCA1-5--Fill cells with value - fill a cell with value , which exists in any other cell -Dinesh Chinnusamy
"""
