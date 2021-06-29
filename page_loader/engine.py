import requests
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from page_loader.make_name_and_path import \
    make_page_file_name, make_dir_name, make_file_name, make_path
from page_loader.save_mode import \
    save_page_html, save_list_img_link, save_files


def download(url, path):
    file_name = make_page_file_name(url)
    file_path = make_path(path, file_name)
    save_page_html(url, file_path)
    dir_name = make_dir_name(url)
    dir_path = make_path(path, dir_name)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    save_files(url, dir_path)

    return file_path
