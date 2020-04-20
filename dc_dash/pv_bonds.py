import numpy as np
import pandas as pd
import os , random , copy , math 
import datetime
dt_now = str(datetime.datetime.now())

"""
NSE URl's == https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=HDFCBANK
https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm?cat=SEC

"""

def pv_BondsSingleRecord(params):
    F = float(params['F'])
    R = float(params['R'])
    T = float(params['T'])
    #
    pv_percOfFace = "dummy"
    #pv = "dummy"
    #
    try:
        pv = F/math.pow((1+R),T)
        print(pv)
        pv_percOfFace = (pv/F)*100
        print(pv_percOfFace)
    except OverflowError:   ### OverflowError: math range error
        ## JIRA_ROHIT_PendingTask SO Code --- Change This == https://stackoverflow.com/a/36980229/4928635
        print("=======OverflowError: math range error=======")
        pv = float('inf')
    return pv,pv_percOfFace # F,R,T - we dont need to Return from here ...




def vanila_pv_paramsUI(params):
    """
    here below OK if we pass DICT named PARAMS
    """
    F = float(params['F'])
    R = float(params['R'])
    T = float(params['T'])
    pv_percOfFace = "dummy"
    #pv = "dummy"
    #
    try:
        pv = F/math.pow((1+R),T)
        print(pv)
        pv_percOfFace = (pv/F)*100
        print(pv_percOfFace)
    except OverflowError:   ### OverflowError: math range error
        ## JIRA_ROHIT_PendingTask SO Code --- Change This == https://stackoverflow.com/a/36980229/4928635
        print("=======OverflowError: math range error=======")
        pv = float('inf')

    return pv,pv_percOfFace # F,R,T - we dont need to Return from here ...

# df = "dfDummy"
# df == None

# def vanila_pv_paramsUInDF(df,params):
"""
when we pass mandatory DF - then only route from views/utils here 
"""
#     if df == None:
#         #
#         F = params['F']
#         R = params['R']
#         T = params['T']
#         #
#         pv = F/math.pow((1+R),T)
#         print(pv)
#         pv_percOfFace = (pv/F)*100
#         print(pv_percOfFace)
#         return pv,F,R,T,pv_percOfFace
#     else:
#         print("===GOT A DF ===")    

  
#

    

