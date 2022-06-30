import os

import pandas as pd

import config

"""
Takes finished translations from /CSV/imp in form of excel files and implements them in to your master CSV.
"""

def import_trans():

    trans = pd.DataFrame()

    trans[['key']] = pd.read_excel('./CSV/imp/en_trans.xlsx')[['key']]
    trans = trans.set_index('key')

    for file in os.listdir('./CSV/imp'):
        tab = pd.read_excel('./CSV/imp/'+ file)
        tab = tab.set_index('key')
        trans = pd.concat([trans, tab.reindex(trans.index)[file[:2]]], axis=1)

    trans = trans.reindex(columns=['en'] + config.get_languages())

    master = pd.read_csv('./CSV/master.csv', encoding='utf-8', index_col='key')

    master = master.append(trans, ignore_index=False)

    master = master.reset_index()
    master = master.drop_duplicates(subset='key', keep='last')
    master = master.sort_values('key')
    master = master.set_index('key')

    master.to_csv('./CSV/master.csv')

    print("Merge review: Missing Translations")
    print(master.isnull().sum(axis=0))