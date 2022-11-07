#!/usr/bin/python

import extension, os


INITIAL_PATH = os.path.abspath(os.path.join(os.getcwd(), 'Archives'))


def discover(path):
    for dirpath, dirs, files in os.walk(path):
        for _file in files:
            absoluts_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absoluts_path.split('.')[-1]
            if ext in extension.extension:
                yield absoluts_path
