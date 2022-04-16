import pandas as pd
from datetime import datetime as dt

def preview_data(df): 
    print('First Five Rows of Data: \n')
    display(df.head())
    print('\n Shape: \n')
    print(df.shape)
    print('\n Info: \n')
    print(df.info())
    
def get_missing_counts(df):
    '''Function that retrieves percentage of missing values in each column of the dataframe'''
    data_dict = dict(df.isna().sum())
    print('Missing Value Percentages by Column: \n')
    for k,v in data_dict.items():
        print('{} -----> {} -----> {}{}'.format(k, ## Gets the name of the column
                                                v,
                                                str(round((v /len(df))*100,2)), ## Retrieves percentage of missing values. 
                                                '%')) 
        
def fill_missing_values(df,cols_mean,cols_median,cols_mode,cols_zero):
    '''Function that fills missing values with respective strategy to the column. : '''
    ## Fill NAs with mean of respective column. 
    df[cols_mean] = df[cols_mean].apply(lambda x: x.fillna(x.mean())) 

    ## Fill NAs with median of the respective column. 
    df[cols_median] = df[cols_median].apply(lambda x: x.fillna(x.median())) 
    
    ## Fill NAs with mode of the respective column. 
    df[cols_mode] = df[cols_mode].apply(lambda x: x.fillna(x.mode())) 

    ## Fill NAs with zeros. 
    df[cols_zero] = df[cols_zero].apply(lambda x: x.fillna(0)) 
    
def drop_null_values(df,cols):
    '''Function that drops null values from certain columns'''
    df.dropna(subset = cols, inplace = True)
    

def get_unique_column_count(df):
    ''' Function that returns object columns and their distinct count'''
    print('Unique values in each object column: \n')
    for column in df.select_dtypes('object').columns:
        print('{}{}{}'.format(column,': ',df[column].nunique()))

def get_value_counts(df):
    ''' Function that returns object columns and their distinct count'''
    print('Unique values in each object column: \n')
    for column in df.select_dtypes('object').columns:
        print('{}{}{}{{}}'.format(column,'\n',df[column].value_counts(),'\n'))
        print('\n')

def get_datetimes(df,date_cols, date_col): 
    from datetime import datetime as dt
    '''Add Details to function later'''
    df[date_cols] =df[date_cols].apply(pd.to_datetime)
    df['Month'] = df[date_col].dt.month
    df['Day'] = df[date_col].dt.day
    df['Day_of_Week'] = df[date_col].dt.weekday
    df['Year'] = df[date_col].dt.year
    print('Range of Dates in this DataFrame are between {} & {}'.format(df[date_cols[0]].min(),
                                                                        df[date_cols[0]].max()))