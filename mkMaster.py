import os
import json
import flatdict
import pandas as pd
"""
Takes all JSON files in /JSON/imp and genartes a master CSV for you. Do only use this if dont have a master CSV, or if you want to rebuild your master table. 
"""
def make_master():
    master = pd.DataFrame()

    for application in os.listdir('./JSON/imp'):
        for file in os.listdir(os.path.join('./JSON/imp', application)):
            if file.startswith('en'):
                with open(os.path.join('./JSON/imp', application, file), 'r', encoding='UTF-8') as file:
                    en = json.load(file)
                    en = flatdict.FlatDict(en, delimiter='.')
                    translations = pd.DataFrame(en.items())
                    translations.columns = ['key', 'en']
                    translations = translations.set_index('key')

        for file in os.listdir(os.path.join('./JSON/imp', application)):
            if not file.startswith('en'):
                with open(os.path.join('./JSON/imp', application, file), 'r', encoding='UTF-8') as f:
                    dict = json.load(f)

                    dict = flatdict.FlatDict(dict, delimiter='.')
                    dict = pd.DataFrame(dict.items())
                    dict.columns = ['key', file[:2]]
                    dict = dict.set_index('key')

                    translations = pd.concat([translations, dict.reindex(translations.index)], axis=1)

        master = pd.concat([master,translations])

    master = master.reset_index()
    master = master.drop_duplicates(subset='key', keep='last')
    master = master.sort_values('key')
    master = master.set_index('key')

    master.to_csv((os.path.join('./CSV/master.csv')), encoding="utf-8")

    print(master.isnull().sum(axis = 0))

    return True





