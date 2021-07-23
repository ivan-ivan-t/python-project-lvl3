import os
import re


MAX_LEN_NAME = 50


def cut_scheme(url):
    return re.sub('http[s]?://', '', url)


def make_kebab_case(name):
    name = re.sub('\W|_', '-', name)
    if len(name) > MAX_LEN_NAME:
        return name[:MAX_LEN_NAME]
    return name


def make_file_name(url):
    without_scheme = cut_scheme(url)
    path, extension = os.path.splitext(without_scheme)
    if not extension:
        extension = '.html'
    return make_kebab_case(path) + extension 


def make_dir_name(url):
    without_scheme = cut_scheme(url)
    return make_kebab_case(without_scheme) + '_files'
