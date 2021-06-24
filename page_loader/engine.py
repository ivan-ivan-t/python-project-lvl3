import requests
import os
import re


def make_file_name(url):
    cut_scheme = re.sub('http[s]?://', '', url)
    return re.sub('\W|_', '-', cut_scheme) + '.html'


def download(url, path):
    page = requests.get(url)
    file_name = make_file_name(url)
    os.chdir(path)
    with open(file_name, 'w') as file:
        file.write(page.text) 
    full_path_to_file = os.path.join(path, file_name)
    return full_path_to_file
