import sys
from os.path import exists
import impKeys
import impTrans
import mkJSON
import mkMaster
import mkTrans
import pandas as pd
import csv


__name__ == '__main__'
if exists('CSV/master.xlsx'):
    master = pd.read_excel('CSV/master.xlsx', index_col='key')
    master.to_csv('CSV/master.csv')

print("Welcome to the ScreenFlox Translator, this is a Python script, that  automatically generates CSV documents "
      "for translating your application in different languages. For further information's pleas contact "
      "philipp.buesgen@atos.net")
print()
print()

if not exists('CSV/master.xlsx'):
    if not exists('CSV/master.csv'):
        print("I was not able to detect any master tables! Make sure you located your master table at "
              "'/CSV/master.xlsx', or '/CSV/master.csv'")
        print()
        print("Please select an option:")
        print("1: Create a new master table from scratch")
        print("2: Create master table from existing source")
        print("3: Cancel!")
        input_type = input("input:")
        print()

        if input_type == '1':
            print("Type the first two letters of the language you want to add, as long as you do not type 'done', "
                  "you can add as many languages as you want!")


            languages = ['key', 'en']
            language = None
            while language != "done":
                language = input()
                if language != "done":
                    languages.append(language)
                    print("Added!")

            with open('CSV/master.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(languages)

            print("Done!")
            print()

        elif input_type == '2':
            mkMaster.make_master()
            print("Done!")
            print()

        else:
            print("Canceled!")
            sys.exit()

    else:
        print("I detected a master.csv file, but no master.xlsx file! Do you want to create a master.xlsx file out of "
              "the master.csv file?")
        if input("[y/n]") == "y":
            master = pd.read_csv('CSV/master.csv', encoding='utf-8', index_col='key')
            master.to_excel('CSV/master.xlsx')
            print("Created master.xlsx!")
            print()

        else:
            print("Canceled!")
            sys.exit()

while True:

    print("Please select an option:")
    print()
    print("- Translation lifecycle")
    print("1: import a base language JSON in to your master table")
    print("2: import translations in to your master table")
    print("3: create new JSONs for all languages")
    print("4: create new translation tables for your customer")
    print()
    print("- Config")
    print("5: Create a blanco master table")
    print("6: Create a master table from existing source")

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

    elif input_type == '5':
        print("Caution this action will override any existing master tables, proceed anyways?")

        if input("[y/n]") == "y":
            print("Type the first two letters of the language you want to add, as long as you do not type 'done', "
                  "you can add as many languages as you want!")

            languages = ['key', 'en']
            language = None
            while language != "done":
                language = input()
                if language != "done":
                    languages.append(language)
                    print("Added!")

            with open('CSV/master.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(languages)

            print("Done!")
            print()
        else:
            print("Canceled!")
            print()

    elif input_type == '6':
        print("Caution this action will override any existing master tables, proceed anyways?")

        if input("[y/n]") == "y":
            mkMaster.make_master()

            print("Done!")
            print()
        else:
            print("Canceled!")
            print()

    master = pd.read_csv('CSV/master.csv', encoding='utf-8', index_col='key')
    master.to_excel('CSV/master.xlsx')
