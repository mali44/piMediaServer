import json
import urllib


def download(url):
    print('dosya  indiriliyor...')
    urllib.request.urlretrieve(url,'/a.jpg')
