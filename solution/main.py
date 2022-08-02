#!python3

import json
import pandas as pd
from tabulate import tabulate
import os

def visualize_table(data_directories_list):
    """
    Visualize the complete historical table view of each tables in tabular format in stdout (hint: print your table)
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
        
    # print(json_list)
    
    #convert json into pandas data frame
    df = pd.json_normalize(json_list)\
            .set_index('ts').sort_index() #set index for historical table
    #print data in terminal
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    #print data shape
    print(df.shape)

if __name__ == '__main__':
    #get list of directory data
    data_directories_list = os.listdir("./data")
    # print(data_directories_list)
    
    #itteration all directories in data directory
    for i in data_directories_list:
        #Visualize each table
        print(f"[Visualize Table] data {i} directory ")
        visualize_table(i)
        print("\n")
    