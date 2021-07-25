import requests
import os
from page_loader.transformation_url import make_file_name
from page_loader.logger import get_logger
from progress.bar import IncrementalBar


logger = get_logger(__name__)


def save_file(source, path):
    try:
        mode = 'w' if isinstance(source, str) else 'wb'
        with open(path, mode) as f:
            f.write(source)
    except OSError as error:
        logger.critical(error)
        raise OSError()


def download_resources(resources, path):
    bar = IncrementalBar('Download resurces', max=len(resources))
    for link in resources:
        content = requests.get(link).content
        save_file(content, os.path.join(path, make_file_name(link)))
        bar.next()
    bar.finish()
