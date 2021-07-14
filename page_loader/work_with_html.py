from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os
from page_loader.transformation_url import make_file_name


def get_resources_and_change_html(url, page, dir_path):
    list_links = []
    tag_attrs = {'img': 'src', 'link': 'href', 'script': 'src'}
    soup = BeautifulSoup(page.content, "html.parser")
    tag_list = soup.find_all(tag_attrs.keys())
    for tag in tag_list:
        source_link = tag.get(tag_attrs[tag.name])
        if not source_link:
            continue
        if (
            not urlparse(source_link).netloc
            or urlparse(source_link).netloc == urlparse(url).netloc
        ):
            source_link = urljoin(url, source_link)
            list_links.append(source_link)
            tag[tag_attrs[tag.name]] = os.path.join(dir_path, make_file_name(source_link))
    html_with_local_links = soup.prettify(formatter="html5")
    return list_links, html_with_local_links
