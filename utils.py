import requests
import pandas_gbq
import subprocess
from google.oauth2 import service_account

def download_from_sendgrid(url, local_filename):

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def upload_to_bq(credentials, df, table_name):

    credentials = service_account.Credentials.from_service_account_file(credentials,)
    pandas_gbq.to_gbq(df, table_name, project_id="dashbaording-all-clients", credentials=credentials, if_exists='append')

def unzip_file(file_name):
    result = subprocess.run('unzip download.zip', shell=True)

def remove_files():
    subprocess.run('rm *.csv', shell=True)
    subprocess.run('rm *.zip', shell=True)