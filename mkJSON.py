import pandas as pd
import json
import os
import flatdict
import ut
"""Takes the JSON of your base language (/JSON/exp) as a reference to create JSONs for all languages, were there 
exists a translation in the master table. """

def make_json():
    master = pd.read_csv('./CSV/master.csv', encoding='utf-8', index_col='key')

    for application in os.listdir('./JSON/exp'):
        for file in os.listdir(os.path.join('./JSON/exp', application)):
            if file.startswith('en'):
                print(os.path.join('./JSON/exp', application, file))
                with open(os.path.join('./JSON/exp', application, file), 'r', encoding='UTF-8') as file:
                    en = json.load(file)

                en = flatdict.FlatDict(en, delimiter='.')
                trans = pd.DataFrame(en.items())
                trans.columns = ['key', 'en']

                trans = pd.merge(trans['key'], master, on='key')
                trans = trans.set_index('key')
                print(trans.shape)

                for language in master.columns:
                    dict = trans[[language]]
                    dict = dict.dropna()
                    dict = dict.to_dict()
                    dict = dict[language]
                    dict = ut.unflatten(dict)

                    with open(os.path.join('./JSON/imp', application,(language + '.json')), "w", encoding='utf-8') as outfile:
                        json.dump(dict, outfile, ensure_ascii=False)


