#!python3

import json
import pandas as pd
import os

if __name__ == '__main__':
    #get list of directory data
    data_directory_list = os.listdir("./data")
    print(data_directory_list)