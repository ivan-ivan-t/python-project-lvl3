import os
import re



def cut_scheme(url):
    return re.sub('http[s]?://', '', url)


def make_kebab_case(name):
    return re.sub('\W|_', '-', name)


def make_page_file_name(url):
    without_scheme = cut_scheme(url)
    if os.path.splitext(without_scheme)[1] == '.html':
        return make_kebab_case(os.path.splitext(without_scheme)[0]) + '.html'
    else:
        return make_kebab_case(without_scheme) + '.html'


def make_dir_name(url):
    without_scheme = cut_scheme(url)
    return make_kebab_case(without_scheme) + '_files'


def make_file_name(url):
    without_scheme = cut_scheme(url)
    if os.path.splitext(url)[1] == '.png':
        return make_kebab_case(os.path.splitext(without_scheme)[0]) + '.png'
    else:
        return make_kebab_case(without_scheme) + '.png'


def make_path(root_dir, name):
    path = os.path.join(root_dir, name)
    return path    
