import os
import re



def cut_scheme(url):
    return re.sub('http[s]?://', '', url)


def make_kebab_case(name):
    return re.sub('\W|_', '-', name)


def make_file_name(url):
    without_scheme = cut_scheme(url)
    path, extension = os.path.splitext(without_scheme)
    if not extension:
        extension = '.html'
    return make_kebab_case(path) + extension 


def make_dir_name(url):
    without_scheme = cut_scheme(url)
    return make_kebab_case(without_scheme) + '_files'    


def make_path(root_dir, name):
    path = os.path.join(root_dir, name)
    return path    
