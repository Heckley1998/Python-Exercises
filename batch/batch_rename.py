#!/usr/bin/env python

# batch_rename.py
# Created: 8th Dec 2020

""" Script renames chosen group of files in given directory """

__author__ = "Radek Warowny"

__license__ = "MIT"
__version__ = '1.1'
__maintainer__ = "Radek Warowny"
__email__ = "radekwarownydev@gmail.com"

import glob
import os
import sys
from pathlib import Path

home_dir = str(Path.home())
current_dir = str(os.getcwd())
path = home_dir


def interface(home, curr):

    os.system('cls')  # clear terminal screen

    # with open('logo.txt', 'r', encoding='utf-8') as file:
    #     print()
    #     for line in file:
    #         line = line.strip()
    #         print('\t',line)

    print("\n\t\t\tBATCH FILE RENAME")
    print("\t\t\t PRESS Q TO QUIT\n")
    print("\tHOME DIR: ", home)
    print("\tCURRENT DIR: ", curr)


def logic(home, curr):
    directory = input("\n\tWORK FROM (C)URRENT OR (H)OME DIR: ")
    if curr != home:
        if directory.upper() == 'Q':
            sys.exit()
        elif directory.upper() == 'C':
            os.chdir(curr)
            contents()
        elif directory.upper() == 'H':
            os.chdir(home)
            contents()
        else:
            print("INPUT ERROR")
            logic(home, curr)


def contents():
    content = input("\n\tDIRECTORY CONTENT (Y/N): ")
    if content.upper() == 'Q':
        os.system('cls')
        logic(home_dir, current_dir)

    elif content.upper() == 'Y':
        os.system('cls')
        print("\nCURRENT DIR: ", str(os.getcwd()))
        contents = sorted([f for f in os.listdir('./') if not f.startswith('.')], key=str.lower)
        print()
        for item in contents:
            if os.path.isfile(item):
                print('file: ',item)
            else:
                print("dir : ../ " + item)
    elif content.upper() == "N":
        pass
    else:
        try:
            interface(home_dir, current_dir)
        except TypeError:
            print("INPUT ERROR")
            os.system('cls')
            logic(home_dir, current_dir)

    path = os.getcwd()

    while not os.path.isfile(path):

        path = input("\nIF FILE PRESENT TYPE FILE EXT e.g.(.py)\n"
                     "OTHERWISE TYPE FOLDER NAME: ../")
        if path.upper() == 'Q':
            os.system('cls')
            logic(home_dir, current_dir)
        if '.' in path:
            file_name = ''
            for file in glob.glob("*.{}".format(path)):
                print(file)
                file_name = file
            change = input("CHANGE FILE NAME TO e.g.(file.txt): ")
            file_split = file_name.split(".")
            extension = str(file_split[1])
            n = 1
            for file in glob.glob("*.{}".format(extension)):
                os.rename(file, "{}_{}.{}".format(change, n, extension))
                n += 1
            print("FILES RENAMED")
            sys.exit()

        elif os.path.isfile(path):

            #extension = input("FILE EXT TO RENAME: ")
            file_name = ''
            for file in glob.glob("*.{}".format(extension)):
                print(file)
                file_name = file
            change = input("CHANGE FILE NAME TO: ")
            file_split = file_name.split(".")

            extension = str(file_split[1])
            n = 1
            for file in glob.glob("*.{}".format(extension)):
                os.rename(file,"{}_{}.{}".format(change, n, extension))
                n += 1
            print("FILES RENAMED")
            sys.exit()
        try:
            os.chdir(os.getcwd() + "/{}".format(path))
        except FileNotFoundError:
            print("INPUT ERROR")

        if content == 'file':
            extension = input("FILE EXT TO RENAME: ")
            for file in glob.glob("*.{}".format(extension)):
                print(file)
        elif content == 'y':
            os.system('cls')
            contents = sorted([f for f in os.listdir('./') if not f.startswith('.')], key=str.lower)
            for item in contents:
                if os.path.isfile(item):
                    print(item)
                else:
                    print("...../" + item)


interface(home_dir, current_dir)
logic(home_dir, current_dir)