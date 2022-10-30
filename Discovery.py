#!/usr/bin/python

import os
import extension


def discover(initial_path):

    for dirpath, files in os.walk(initial_path):
        for _file in files:
            absoluts_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absoluts_path.split('.')[-1]
            if ext in extension.extension:
                yield absoluts_path



if __name__ == '__main__':
    folders = discover(os.getcwd())
    for folder in folders:
        print(folder)