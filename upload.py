import pandas as pd
import os
from utils import upload_to_bq, unzip_file
import config

def upload_files():
    unzip_file(config.local_filename)

    file_names = [f for f in os.listdir('.') if f.endswith('.csv')]

    if len(file_names) == 0:
        print('No CSV files found')
    else:
        i = 1
        for file in file_names:
            j = 1
            print('FileName = ', file)
            table_name = "ATG_Mapping_Connected." + config.output_table_name + str(i)
            for chunk in pd.read_csv(file, chunksize=config.chunksize):
                print('chunk no', j)
                j = j+1
                upload_to_bq(config.credentials, chunk, table_name)
            i = i+1