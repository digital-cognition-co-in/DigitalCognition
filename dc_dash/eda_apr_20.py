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

"""
JIRA_DC_Issue_17 https://github.com/digital-cognition-co-in/DigitalCognition/issues/17
Round off Floats using - Ceil and Floor Mode
Base Code written by - https://github.com/Ak-Shaw
Wrapper Methods written by - https://github.com/RohitDhankar
#
params = {}
params['single_col'] = 0 
# 0 - Boolean = All Columns 
# 1 - Boolean = Single Column 
params['col_index'] = 3
params['ceil_mode'] = 1 
# 1 - Boolean = CEIL_MODE
# 0 - Boolean = FLOOR_MODE

"""


def ceil_only_data(df,params):
    """
    called within - ceil_floor(df,params):
    """
    print("---CEIL----")
    sn_col = params['single_col']  # 0 - Boolean = Not True
    col_id = params['col_index']   # InT value
    
    sn_col_data = df.iloc[:, col_id]
    
    if sn_col == 1:
        if (np.issubdtype(sn_col_data.dtype, np.number)) :
            print(sn_col)
            print("-------")
            sn_col_data = sn_col_data.apply(np.ceil)
            return df
    else:
        all_cols = df.columns.tolist()
        for i in all_cols:
            if (np.issubdtype(df[i].dtype, np.number)) :
                df[i] = df[i].apply(np.ceil)
        return df

def floor_only_data(df,params):
    """
    called within - ceil_floor(df,params):
    """
    print("---FLOOR----")
    sn_col = params['single_col']  # 0 - Boolean = Not True
    col_id = params['col_index']   # InT value
    
    sn_col_data = df.iloc[:, col_id]
    
    if sn_col == 1:
        if (np.issubdtype(sn_col_data.dtype, np.number)) :
            sn_col_data = sn_col_data.apply(np.floor)
            return df
    else:
        all_cols = df.columns.tolist()
        for i in all_cols:
            if (np.issubdtype(df[i].dtype, np.number)) :
                df[i] = df[i].apply(np.floor)
        return df

def ceil_floor(df,params):
    ceil_m = params['ceil_mode']   # 0 - Boolean = floor_only_data
    if ceil_m == 1:
        df = ceil_only_data(df,params)
    else:
        df =  floor_only_data(df,params)
    return df
    
















def change_to_upper(df,row_p,col_p):
    '''
    JIRA-DCA1-3
    AVIRUP - Avirup Chattaraj - 12 Apr 20 
    The function here performs the function of changing the dataframe value to upper case and if its already
    upper case raises an exception
    :param df:A dataframe needs to be passed
    :type df:pandas.core.frame.DataFrame
    :param row_p:Row position[related to iloc] needs to be passed
    :type row_p:int
    :param col_p:Column position[related to iloc] needs to be passed
    :type col_p:int
    :raises: :class: 'Exception' : Already upper case element
    
    :returns:nothing:Dataframe element already updated if not upper
    :rtype:Nonetype
    
    '''
    value=df.iloc[row_p,col_p]
    upper_value=df.iloc[row_p,col_p].upper()
    if value==upper_value:
        raise Exception
    else:
        df.iloc[row_p,col_p]=upper_value

    # df=pd.DataFrame([['hello','bye','HELLO','good','devil'],['what','is','your','name','PANDAS']])
    # change_to_upper(df,1,2)
    # print(df)
