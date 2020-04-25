from datetime import datetime
import pandas as pd 

def extract_date(data, year=True, month=True, day=True, hour=True, minute=True, second=True):
    """
    Extract date from a given data; if no date found returns NA

    Input:
    	data(String): The value from which date needs to be extracted
    	year(Boolean): If year is required
    	month(Boolean): If month is required  
    	day(Boolean): If date is required 
    	hour(Boolean): If hour is required 
    	minute(Boolean): If minute is required 
    	second(Boolean): If seciond is required 
    Returns: 
    	String: Extracted date in YYYY-MM-DD HH:MM:SS fromat as a string; if no date found tthen "NA"
    """
    if not pd.isna(data):
        for fmt in ('%d/%m/%y %H:%M %p','%d/%m/%y %H:%M','%Y/%m/%d %H:%M','%m/%d/%Y %H:%M %p','%Y/%B/%d %H:%M',
                    '%d-%b-%y', '%b-%d-%Y', '%B-%d-%Y', '%m/%d/%y', '%d:%m:%Y', '%d.%m.%Y', '%d/%m/%Y'):
            try:
                date = datetime.strptime(data, fmt)
                final_date_time = "" 
                if year:
                    d_year = date.year
                    final_date_time += f'{d_year:04}'
                if month:
                    d_month = date.month
                    final_date_time += '-' + f'{d_month:02}'
                if day:
                    d_day = date.day
                    final_date_time += '-' + f'{d_day:02}'
                if hour:
                    d_hour = date.hour
                    final_date_time += ' ' + f'{d_hour:02}'
                if minute:
                    d_minute = date.minute
                    final_date_time += ':' + f'{d_minute:02}'
                if second:
                    d_second = date.second
                    final_date_time += ':' + f'{d_second:02}'
                return final_date_time
            except ValueError:
                pass
        raise ValueError('no valid date format found')
    else:
        return "NA"

def extract_date_col(df, col_idx, year=True, month=True, day=True, hour=True, minute=True, second=True, inPlace=False):
	"""
	Extract date from a given column of a dataframe and create a new column with extracted date in it. 
	It support modification of input dataframe or creation of a new one. 
	If the modification of the input dataframe is choose it returns None and adds a new column to the dataframe; it 
	returns a new datafrane with the added column otherwise.

	Input:
    	df(DataFrame): The pandas DataFrame for which we need to do the date extraction
    	col_idx(int): Index of the column we want to extract date from
    	year(Boolean): If year is required
    	month(Boolean): If month is required  
    	day(Boolean): If date is required 
    	hour(Boolean): If hour is required 
    	minute(Boolean): If minute is required 
    	second(Boolean): If seciond is required 
    	inPlace(Boolean): If true the same dateframe which was input is modified, a new dataframe is created otherwise 
    Returns: 
    	DataFrame: New dataframe with added column if inPlace is False, None otherwise
	"""
	try:
    	col_name = df.columns[col_idx]
    except IndexError:
    	raise IndexError('index must be in the range between 0 and no. of columns-1 (both inclusive)')
    new_col_name = col_name + '_DateExtracted'
    while new_col_name in df.columns:
    	new_col_name += '_new'
    if inPlace:
        df[new_col_name] = df[col_name].apply(extract_date)
        return None
    else:
        new_df = df.copy()
        new_df[new_col_name] = df[col_name].apply(extract_date)
        return new_df

