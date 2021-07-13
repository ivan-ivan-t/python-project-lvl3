import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from page_loader.make_name_and_path import make_path, make_file_name


def save_page_html(page, file_path):
    with open(file_path, 'w') as f:
        f.write(page)

def choose_src_or_href(tag):
    if tag.get('src'):
        return 'src'
    if tag.get('href'):
        return 'href'
    else:
        False


def get_resources_and_change_html(url, page, dir_path, file_name):
    list_links = []
    soup = BeautifulSoup(page.content, "html.parser")
    tag_list = soup.find_all(['img', 'link', 'script'])
    for i in tag_list:
        src_or_href = choose_src_or_href(i)
        if not src_or_href:
            continue
        source_link = i.get(src_or_href)
        if not urlparse(source_link).netloc or urlparse(source_link).netloc == urlparse(url).netloc:
            source_link = (urlparse(url).scheme + '://'
                          + urlparse(url).netloc
                          + urlparse(source_link).path)    
            list_links.append(source_link) 
            i[src_or_href] = make_path(dir_path, file_name)
    html_with_local_links = soup.prettify(formatter="html5")        
    return list_links, html_with_local_links


def save_files(files, path):
    with open(path, 'wb') as f:
        f.write(files) 

       
def download_resources(resources, path):
    for i in resources:
        content = requests.get(i).content
        save_files(content, make_path(path, make_file_name(i)))
