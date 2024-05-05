import os
import json
import flatdict
import pandas as pd

import config

"""
Takes all new keys in your base language and imports them to your master table.
"""

def import_keys():
    print(os.getcwd())
    keys = pd.DataFrame()
    for application in os.listdir('./JSON/exp'):
        for file_name in os.listdir(os.path.join('./JSON/exp', application)):
            with open(os.path.join('./JSON/exp', application, file_name), 'r', encoding='UTF-8') as file:
                file = json.load(file)
                file = flatdict.FlatDict(file, delimiter='.')

                file = pd.DataFrame(file.items())
                file.columns = ['key', file_name.split('.')[0]]
                file = file.set_index('key')

                keys = pd.concat([file, keys], axis=1)

    keys = keys.reset_index()
    keys = keys.drop_duplicates(subset='key', keep='last')
    keys = keys.sort_values('key')
    keys = keys.set_index('key')

    master = pd.read_csv('CSV/master.csv', encoding='utf-8', index_col='key')

    master = pd.concat([master, keys], ignore_index=False)
    #master = master.append(keys, ignore_index=False)

    master = master.reset_index()
    master = master.drop_duplicates(subset='key', keep='first')
    master = master.sort_values('key')
    master = master.set_index('key')

    master.to_csv('CSV/master.csv')

    print("Merge review: Missing Translations")
    print(master.isnull().sum(axis=0))
