import requests
from urllib.parse import urlparse


def name_file(url):
    netloc = '-'.join((urlparse(url).netloc).split('.'))
    path = '-'.join((urlparse(url).path).split('/'))
    return netloc + path + '.html'


def download(url, path):
    page = requests.get(url)
    name = name_file(url)
    file = open(name, 'w')
    file.write(page.text)
    file.close()
    full_path = path + '/' + name
    return full_path
