import pandas as pd
"""
Creates a excel file for every language with untranslated keys in the master CSV.
"""
def make_translations():
    master = pd.read_csv('./CSV/master.csv', encoding='utf-8', index_col='key')
    export = master[master.isnull().any(axis=1)]

    for col in export.columns:
        tab = export[['en', col]]
        tab.columns = ['enRef', col]

        tab.to_excel('./CSV/exp/' + col + '_trans.xlsx')