# coding:utf-8

import urllib.request

response = urllib.request

url = input('URL:')

urlopen = response.urlopen(url)

print(urlopen.read())

headers = urlopen.info()
headers['content-type']

