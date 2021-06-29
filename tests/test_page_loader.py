import tempfile
from page_loader.engine import download, make_page_file_name
import requests_mock 


def test_download():
    with tempfile.TemporaryDirectory() as test_dir:
        with requests_mock.Mocker() as m:
            m.get('https://ru.hexlet.io/courses', text='resp')
            file_path = download('https://ru.hexlet.io/courses', test_dir)
            with open(file_path) as file:
                assert 'resp' == file.read()


def test_make_file_name():
    expected = 'ru-hexlet-io-courses.html'
    file_name = make_page_file_name('https://ru.hexlet.io/courses')
    assert expected == file_name
