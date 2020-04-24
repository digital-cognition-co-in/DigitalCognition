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

def pattern_matching(data,column,filter_choice,filter_value=''):
    '''
    The function here is going to apply pattern matching using regex on the selected
    dataframe and returns the dataframe without any null values based on the given predetermined
    conditions
    1)Manual Regular Expression
    2)Regular Expression from start
    3)Regular Expression from end
    4)Regular Expression from between

    :param data:A dataframe needs to be passed
    :type data:pandas.core.frame.dataframe
    :param column:A column name needs to be passed
    :type column:str
    :param filter_choice:A option number needs to be passed
    :type filter_choice:int
    :param filter_value:A value for the regex engine
    :type filter_value:str



    :returns:return_df:A dataframe after the applied expressions
    :rtype:pandas.core.frame.dataframe
    '''
    if filter_choice==1:
        return_df=data[column].str.extract(r'({})'.format(filter_value)).dropna()
    elif filter_choice==2:
        return_df=data[column].str.extract(r'(^{}.+)'.format(filter_value)).dropna()
    elif filter_choice==3:
        return_df=data[column].str.extract(r'(.+{}$)'.format(filter_value)).dropna()
    elif filter_choice==4:
        return_df=data[column].str.extract(r'(.+{}.+)'.format(filter_value)).dropna()

    return return_df
