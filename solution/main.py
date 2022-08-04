#!python3

import json
import pandas as pd
from tabulate import tabulate
import os

import warnings
warnings.filterwarnings('ignore')

def read_json_data(data_directories_list):
    """
    Read all over json data from folder
    """
    list_file = os.listdir(f"./data/{data_directories_list}")
    
    #create empty list
    json_list = []
    #itteration all file over the directory
    for i in list_file:
        #Load JSON: json_data
        with open (f'./data/{data_directories_list}/{i}', "r") as json_file:
            json_data = json.load(json_file)
        #add the data in to the list    
        json_list.append(json_data)
    
    #convert json into pandas data frame
    df = pd.json_normalize(json_list)\
            .set_index('ts').sort_index() #set index for historical table
    return df

def remove_prefix(df):
    """
    Remove get and set profix from column name
    """
    df.columns = df.columns.str.replace("data.", "")
    df.columns = df.columns.str.replace("set.", "")
    return df
    
if __name__ == '__main__':
    #get list of directory data
    data_directories_list = ['accounts','cards','savings_accounts']
    
    dfs= []
    #itteration all directories in data directory
    for i in data_directories_list:
        x= read_json_data(i)
        dfs.append(x)
    
    
    #visualize historical table of accounts    
    dfs[0]['data.phone_number'].update(dfs[0].pop('set.phone_number'))
    dfs[0]['data.email'].update(dfs[0].pop('set.email'))
    dfs[0]['data.address'].update(dfs[0].pop('set.address'))
    df_accounts = remove_prefix(dfs[0])
    df_accounts = df_accounts.ffill()
    print('\n[Task 1] Historical accounts table view')
    print(tabulate(df_accounts, headers = 'keys', tablefmt = 'psql'))
    
    #visualize historical table of cards
    dfs[1]['data.status'].update(dfs[1].pop('set.status'))
    dfs[1]['data.credit_used'].update(dfs[1].pop('set.credit_used'))
    df_cards = remove_prefix(dfs[1])
    col_1  = ['credit_used']
    df_cards.loc[:,col_1] = df_cards.loc[:,col_1].fillna(0)
    df_cards = df_cards.ffill()
    print('\n[Task 1] Historical cards table view')
    print(tabulate(df_cards, headers = 'keys', tablefmt = 'psql'))
    
    #visualize historical table of saving_accounts
    dfs[2]['data.balance'].update(dfs[2].pop('set.balance'))
    dfs[2]['data.interest_rate_percent'].update(dfs[2].pop('set.interest_rate_percent'))
    df_savings_accounts = remove_prefix(dfs[2])
    df_savings_accounts = df_savings_accounts.ffill()
    print('\n[Task 1] Historical savings_accounts table view')
    print(tabulate(df_savings_accounts, headers = 'keys', tablefmt = 'psql'))
    
    # task 2
    df_merged=pd.merge_ordered(df_accounts,df_savings_accounts,on='ts')
    col = ['ts','account_id','savings_account_id_x','name','address','phone_number',
           'email','balance','interest_rate_percent','status']
    df_merged = df_merged[col]
    df_merged=pd.merge_ordered(df_merged,df_cards,on='ts')
    col = ['ts','account_id','savings_account_id_x','card_id','name','address','phone_number',
           'email','balance','interest_rate_percent','status_x','card_number','credit_used',
           'monthly_limit','status_y']
    df_merged = df_merged[col]
    df_merged = df_merged.rename(columns={'savings_account_id_x':'savings_account_id',
                              'status_x' : 'sa_status',
                              'status_y' : 'c_status'})
    df_merged.loc[:,col_1] = df_merged.loc[:,col_1].fillna(0)
    df_merged = df_merged.ffill()
    print('\n[Task 2] Historical denormalize table view')
    print(tabulate(df_merged, headers = 'keys', tablefmt = 'psql'))
    
    
    # task 3
    df_merged['balance_difference'] = df_merged['balance'].diff()
    df_merged['balance_difference'] = df_merged['balance_difference'].fillna(0)
    count_transaction_credit_used = (df_merged['credit_used'] !=0).sum()
    count_transaction_change_balance = (df_merged['balance_difference'] !=0).sum()
    transaction_count = count_transaction_credit_used + count_transaction_change_balance
    print(f'\n[Task 3] Number of Transaction: {transaction_count}, {count_transaction_change_balance} balance changes, {count_transaction_credit_used} credit used')
    col_2 = ['ts','credit_used','balance_difference']
    df_merged = df_merged [col_2]
    subset_df_merged = df_merged[(df_merged['balance_difference'] != 0) | (df_merged['credit_used'] != 0)]
    subset_df_merged['date'] = pd.to_datetime(subset_df_merged['ts'])
    print(f'\n[Task 3] Table of transaction and time of accurence')
    print(tabulate(subset_df_merged, headers = 'keys', tablefmt = 'psql'))
    