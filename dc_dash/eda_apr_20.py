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
