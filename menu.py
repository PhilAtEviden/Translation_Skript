import csv

import pandas as pd

import impKeys
import impTrans
import mkJSON
import mkTrans


def main_menu():
    while True:

        print("Please select an option:\n")

        print("- Translation lifecycle")
        print("1: import a base language JSON in to your master table")
        print("2: import translations in to your master table")
        print("3: create new JSONs for all languages")
        print("4: create new translation tables for your customer")

        input_type = input("input:")
        print()

        if input_type == '1':
            impKeys.import_keys()
            print("Done!")
            print()

        elif input_type == '2':
            impTrans.import_trans()
            print("Done!")
            print()

        elif input_type == '3':
            mkJSON.make_json()
            print("Done!")
            print()

        elif input_type == '4':
            mkTrans.make_translations()
            print("Done!")
            print()

        master = pd.read_csv('./CSV/master.csv', encoding='utf-8', index_col='key')
        master.to_excel('./CSV/master.xlsx')