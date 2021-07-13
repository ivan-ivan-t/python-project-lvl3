import requests
import os
import re
from urllib.parse import urlparse

from page_loader.make_name_and_path import \
     make_dir_name, make_file_name, make_path
from page_loader.save_mode import \
     save_page_html, get_resources_and_change_html, save_files, download_resources, choose_src_or_href


def download(url, path):
    response = requests.get(url)
    file_name = make_file_name(url)
    file_path = make_path(path, file_name)
    dir_name = make_dir_name(url)
    dir_path = make_path(path, dir_name)
    resources, html_with_local_links  = get_resources_and_change_html(url, response, dir_path, file_name)
    save_page_html(html_with_local_links, file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)    
    download_resources(resources, dir_path)

    return file_path
