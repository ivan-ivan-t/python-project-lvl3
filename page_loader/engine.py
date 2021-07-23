import requests
import os

from page_loader.transformation_url import make_dir_name, make_file_name
from page_loader.saves import save_file, download_resources
from page_loader.work_with_html import get_resources_and_change_html


def download(url, path):
    response = requests.get(url)
    file_name = make_file_name(url)
    file_path = os.path.join(path, file_name)
    dir_name = make_dir_name(url)
    dir_path = os.path.join(path, dir_name)
    resources, html_with_local_links = get_resources_and_change_html(url, response, dir_path)
    save_file(html_with_local_links, file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    download_resources(resources, dir_path)
    return file_path
