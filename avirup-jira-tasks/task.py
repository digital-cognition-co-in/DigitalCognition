# Change to upper case
import pandas as pd



def change_to_upper(df,row_p,col_p):
    '''
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




def main():
    df=pd.DataFrame([['hello','bye','HELLO','good','devil'],['what','is','your','name','PANDAS']])
    change_to_upper(df,1,4)
    print(df)



if __name__=='__main__':
    main()