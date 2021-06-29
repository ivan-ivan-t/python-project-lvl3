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
    os.makedirs(make_path(path, dir_name))
    save_files(url, make_path(path, dir_name))

    return file_path
