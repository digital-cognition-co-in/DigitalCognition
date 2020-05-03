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


def df_column_swap(_df, source_index, destination_index):
    """
    @author = abhijeet mote
    abhijeetmote@gmail.compile
    Github   :  https://github.com/abhijeetmote
    LinkedIn :  https://www.linkedin.com/in/abhijeet-mote/
    This Method Swaps the two columns.
    Parameters
    ----------
    _df               : Pandas Dataframe
    source_index      : Source Column index number to swap with 
                        destination_index
    destination_index : Destination Column number to swap with   
                        source_index
    
    example :
    df_dict = {'x': {0: 10,1: 11, 2: 12, 3: 13, 4: 14, 5: 15,},
     'y': {0: 50, 1: 51, 2: 52, 3: 53, 4: 54, 5: 55,},
     'z': {0: 100, 1: 101, 2: 102, 3: 103, 4: 104, 5: 105,}}
    df = pd.DataFrame(df_dict)
        x   y    z
    0  10  50  100
    1  11  51  101
    2  12  52  102
    3  13  53  103
    4  14  54  104
    5  15  55  105
    
    
    df_column_swap(df, 1, 2)
    
        x   y    z
    0  10  50  100
    1  11  51  101
    2  12  52  102
    3  13  53  103
    4  14  54  104
    5  15  55  105
    """
    df = _df.copy()
    df['temp'] = df.iloc[:,source_index]
    df.iloc[:,source_index] = df.iloc[:,destination_index]
    df.iloc[:,destination_index] = df['temp']
    del df['temp']
    return(df)
    
    
def drop_duplicate_rows(_df):
    """
    @author = abhijeet mote
              abhijeetmote@gmail.compile
    Github   :  https://github.com/abhijeetmote
    LinkedIn :  https://www.linkedin.com/in/abhijeet-mote/
    This Method removes the dublicate rows from dataframe
    Parameters
    ----------
    _df : Pandas Dataframe
    example
    -------
    df_dict = {'x': {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 
        6: 11, 7: 11, 8: 17},
        'y': {0: 50, 1: 51, 2: 52, 3: 53, 4: 54, 5: 55, 6: 51, 7: 51, 8: 57},
        'z': {0: 100, 1: 101, 2: 102, 3: 103, 4: 104, 5: 105, 6: 101, 7: 101, 8: 107},
        'a': {0: 200, 1: 201, 2: 202, 3: 203, 4: 204, 5: 205, 6: 201, 7: 201, 8: 207}}
       
    df = pd.DataFramerame(df_dict)
            x   y    z    a
        0  10  50  100  200
        1  11  51  101  201
        2  12  52  102  202
        3  13  53  103  203
        4  14  54  104  204
        5  15  55  105  205
        6  11  51  101  201
        7  11  51  101  201
        8  17  57  107  207
    drop_duplicate_rows(df)
            x   y    z    a
        0  10  50  100  200
        1  11  51  101  201
        2  12  52  102  202
        3  13  53  103  203
        4  14  54  104  204
        5  15  55  105  205
        6  17  57  107  207
    """
    df = _df.copy()
    return df.drop_duplicates()


