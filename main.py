#!/usr/bin/env python3

import os
import sys

from argparse import ArgumentParser as ap

def clean():
    raise NotImplementedError

def confirm_deletion(junk: list) -> bool:
    print('The following was found in your downloads folder: ')
    for index, item in enumerate(junk):
        print(f'{index}. {item}\n')
    choice = input('[?]Are you sure that you want to delete these items?: y/n')
    if choice == 'y':
        return True
    elif choice == 'n':
        print('exiting')
        return False
    print('exiting')
    return False

def main():
    parser = ap()
    parser.add_argument('dir')

    if sys.platform == 'win32':
        raise NotImplementedError

    home = os.environ['HOME']
    path = f'{home}/Downloads'
    junk = os.listdir(path)

    if confirm_deletion(junk) == True:
        for item in junk:
            print(f'[-]removing {item}')
            try:
                os.remove(f'{path}/{item}')
            except IsADirectoryError:
                print(f'[!]{item} is a Directory... Skipping!')
                pass
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
