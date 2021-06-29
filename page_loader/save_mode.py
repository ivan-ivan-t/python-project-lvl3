import requests
from bs4 import BeautifulSoup
from page_loader.make_name_and_path import make_path, make_file_name


def save_page_html(url, file_path):
    page = requests.get(url)
    with open(file_path, 'w') as f:
        f.write(page.text)


def save_list_img_link(url):
    list_link = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    img = soup.find_all('img')
    for i in img:
        list_link.append(i.get('src'))
    return list_link


def save_files(url, path):
    list_whith_link = save_list_img_link(url)
    for i in list_whith_link:
        with open(make_path(path, make_file_name(i)), 'wb') as f:
            f.write(requests.get(i).content)


            
