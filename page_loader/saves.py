import requests
import os
from page_loader.transformation_url import make_file_name


def save_file(source, path):
    mode = 'w' if isinstance(source, str) else 'wb'
    with open(path, mode) as f:
        f.write(source)


def download_resources(resources, path):
    for link in resources:
        content = requests.get(link).content
        save_file(content, os.path.join(path, make_file_name(link)))
