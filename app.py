import time
from config import download_link, local_filename
import upload
import utils

# record start time
start = time.time()

print('downloading file from SendGrid')
utils.download_from_sepndgrid(download_link, local_filename)

print('Uploading files to BQ')
upload.upload_files()

print('Removing zip and csv files from cwd')
utils.remove_files()

# record end time
end = time.time()
print("The time of execution of above program is :",
    (end-start) * 10**3, "ms")