import os
import os.path
import wget
import zipfile

url = 'https://stepik.org/media/attachments/lesson/24465/main.zip'
filename = wget.download(url)

with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(".")

path_dir = filename[:-4]
#path_dir = "sample"
#path_dir = "main"

lst = []
for current_dir, dirs, files in os.walk(path_dir):
    for i in files:
        if i.endswith('.py'):
            lst.append(current_dir)
            break
lst.sort()
for i in lst:
    print(i)
