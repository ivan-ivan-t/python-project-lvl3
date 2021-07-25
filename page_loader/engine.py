import requests
import os
from page_loader.logger import get_logger

from page_loader.transformation_url import make_dir_name, make_file_name
from page_loader.saves import save_file, download_resources
from page_loader.work_with_html import get_resources_and_change_html


logger = get_logger(__name__)


def download(url, path):
    logger.info('Start app')
    if not os.path.isdir(path):
        logger.worning("An output directory doesn't exist!")
        raise NameError('Missing directory')
    response = requests.get(url)
    file_name = make_file_name(url)
    file_path = os.path.join(path, file_name)
    dir_name = make_dir_name(url)
    dir_path = os.path.join(path, dir_name)
    logger.debug('get resource and change html')
    resources, html_with_local_links = get_resources_and_change_html(url, response, dir_path)
    save_file(html_with_local_links, file_path)
    logger.debug('loading files complete')
    if not os.path.exists(dir_path):
        logger.info('making dir with files')
        try:
            os.makedirs(dir_path)
        except OSError as error:
            logger.critical(error)
            raise OSError()
    download_resources(resources, dir_path)
    logger.info(f'Page was download')
    return file_path