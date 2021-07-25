import os
import requests
import tempfile
from page_loader.engine import download
from page_loader.transformation_url import make_file_name, make_dir_name
from page_loader.saves import save_file, download_resources
from page_loader.work_with_html import get_resources_and_change_html
import requests_mock
import filecmp


URL = 'https://tests'
TEST_HTML = 'tests/fixtures/test_html.html'
HTML_LOCAL_LINKS = 'tests/fixtures/html_with_local_links.html'
RESOURCE = 'https://tests/file.png'
LOCAL_RESOURCE = 'tests/fixtures/file.jpg'

HTML_URL = [
    'https://ru.hexlet.io/courses.html',
    'https://ru.hexlet.io/courses'
]


def read_file(path, mode):
    with open(path, mode) as file:
        return file.read()


def test_download():
    with tempfile.TemporaryDirectory() as test_dir:
        with requests_mock.Mocker() as mock:
            mock.get(URL, text=read_file(TEST_HTML, 'r'))
            mock.get(RESOURCE, content=read_file(LOCAL_RESOURCE, 'rb'))
            file_path = download(URL, test_dir)
            file1 = read_file(file_path, 'r')
            file2 = read_file(HTML_LOCAL_LINKS, 'r')
            assert file1 == file2
            name_file = 'tests.html'
            assert name_file == os.path.split(file_path)[1]
            dir_path = os.path.join(test_dir, 'tests_files')
            assert os.path.isdir(dir_path) == True
            path_to_file = os.path.join(dir_path, 'tests-file.png')
            assert os.path.isfile(path_to_file) == True
            assert read_file(path_to_file, 'rb') == read_file(LOCAL_RESOURCE, 'rb')
            

def test_make_file_name():
    expected = 'ru-hexlet-io-courses.html'
    for url in HTML_URL:
        assert make_file_name(url) == expected


def test_make_dir_name():
    expected = 'ru-hexlet-io-courses_files'
    assert make_dir_name('https://ru.hexlet.io/courses') == expected






