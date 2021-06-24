import tempfile
from page_loader.engine import download
import requests_mock 


def test_download():
    with tempfile.TemporaryDirectory() as test_dir:
        with requests_mock.Mocker() as m:
            m.get('https://ru.hexlet.io/courses', text='resp')
            file_path = download('https://ru.hexlet.io/courses', test_dir)
            with open(file_path) as file:
                assert 'resp' == file.read()

