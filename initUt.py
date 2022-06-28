from os.path import exists, join
import os
import csv
import pandas as pd

import config


def check_if_CSV_directory_exists():
    if exists(join(config.get_path(), "CSV")):
        return True
    else:
        return False


def check_if_JSON_directory_exists():
    if exists(join(config.get_path(), "JSON")):
        return True
    else:
        return False


def check_if_master_xlsx_exists():
    if exists(join(config.get_path(), "CSV", "master.xlsx")):
        return True
    else:
        return False


def check_if_master_csv_exists():
    if exists(join(config.get_path(), "CSV", "master.csv")):
        return True
    else:
        return False


def check_if_application_exists():
    if len(os.listdir(join(config.get_path(), "JSON/exp"))) > 0 and len(os.listdir(join(config.get_path(), "JSON/imp"))) > 0:
        return True
    else:
        return False


def check_if_applications_match():
    if os.listdir(join(config.get_path(), "JSON/exp")) == os.listdir(join(config.get_path(), "JSON/imp")):
        return True
    else:
        return False



def create_CSV_file():
    path = join(config.get_path(), "CSV")
    os.mkdir(path)
    os.mkdir(join(path, "exp"))
    os.mkdir(join(path, "imp"))


def create_JSON_file():
    path = join(config.get_path(), "JSON")
    os.mkdir(path)
    os.mkdir(join(path, "exp"))
    os.mkdir(join(path, "imp"))


def add_application(application_name):
    path = join(config.get_path(), "JSON")
    os.mkdir(join(path, "exp", application_name))
    os.mkdir(join(path, "imp", application_name))

def create_master_table():
    languages = ['key', 'en'] + config.get_languages()

    with open('CSV/master.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(languages)

    master = pd.read_csv('CSV/master.csv', encoding='utf-8', index_col='key')
    master.to_excel('CSV/master.xlsx')
