from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os
from page_loader.transformation_url import make_file_name, make_dir_name


TAG_ATTRS = {'img': 'src', 'link': 'href', 'script': 'src'}


def get_resources_and_change_html(url, page, dir_path):
    list_links = []
    soup = BeautifulSoup(page.content, "html.parser")
    tag_list = soup.find_all(TAG_ATTRS.keys())
    for tag in tag_list:
        source_link = tag.get(TAG_ATTRS[tag.name])
        if not source_link:
            continue
        if (
            not urlparse(source_link).netloc
            or urlparse(source_link).netloc == urlparse(url).netloc
        ):
            source_link = urljoin(url, source_link)
            list_links.append(source_link)
            tag[TAG_ATTRS[tag.name]] = os.path.join(make_dir_name(url), make_file_name(source_link))
    html_with_local_links = soup.prettify(formatter="html5")
    return list_links, html_with_local_links
