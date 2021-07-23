import os
import requests
import tempfile
from page_loader.engine import download
from page_loader.transformation_url import make_file_name, make_dir_name
from page_loader.saves import save_file, download_resources
from page_loader.work_with_html import get_resources_and_change_html
import requests_mock
import filecmp


TEST_HTML = 'tests/fixtures/test_html.html'
HTML_WITH_LL = 'tests/fixtures/html_with_local_links.html'


def read_file(path, mode):
    with open(path, mode) as file:
        return file.read()


def test_download():
    with tempfile.TemporaryDirectory() as test_dir:
        with requests_mock.Mocker() as mock:
            mock.get('https://ru.hexlet.io/courses', text=read_file(TEST_HTML, 'r'))
            mock.get('https://ru.hexlet.io/courses', text=read_file('tests/fixtures/ru-hexlet-io-courses.html', 'r'))
            mock.get('https://ru.hexlet.io/lessons.rss', content=read_file('tests/fixtures/ru-hexlet-io-lessons.rss','rb'))
            file_path = download('https://ru.hexlet.io/courses', test_dir)
            with open(file_path) as file1:
                with open(HTML_WITH_LL) as file2:
                    assert file1.read() == file2.read()
            html_file = 'ru-hexlet-io-courses.html'    
            assert html_file == os.path.split(file_path)[1]
            dir_name = 'ru-hexlet-io-courses_files'
            assert os.path.isdir(test_dir + '/' + dir_name) == True
            




def test_make_file_name():
    expected = 'ru-hexlet-io-courses.html'
    file_name = make_file_name('https://ru.hexlet.io/courses')
    assert expected == file_name


def test_make_dir_name():
    expected = 'ru-hexlet-io-courses_files'
    dir_name = make_dir_name('https://ru.hexlet.io/courses')
    assert expected == dir_name


def test_save_file():
    with tempfile.TemporaryDirectory() as test_dir:
        img_file_path = os.path.join(test_dir, 'test.jpg')
        save_file('/home/mand/Загрузки/test.jpg', img_file_path)
        assert os.path.isfile(img_file_path) == True
        #assert filecmp.cmp(img_file_path, 'tests/fixtures/test_file.jpg', shallow=True)   


def test_get_resources_and_change_html():
    with tempfile.TemporaryDirectory() as test_dir:
        html = requests.get(TEST_URL2)
        path_html_whit_local_links = os.path.join(test_dir, 'test.html')
        _, html_whit_local_links = get_resources_and_change_html(TEST_URL, html, path_html_whit_local_links)
        save_file(html_whit_local_links, path_html_whit_local_links)
        assert os.path.exists(path_html_whit_local_links) == True


def test_download_resources():
    with tempfile.TemporaryDirectory() as test_dir:
        download_resources(RESOURCES, test_dir)
        assert os.path.exists(os.path.join(test_dir, make_file_name(TEST_URL))) == True
