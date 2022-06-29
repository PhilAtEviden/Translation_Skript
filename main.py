from os.path import exists
import init
import menu
import pandas as pd


__name__ == '__main__'
init.check_directories()

if exists('CSV/master.xlsx'):
    master = pd.read_excel('CSV/master.xlsx', index_col='key')
    master.to_csv('CSV/master.csv')

print("Welcome to the ScreenFlox Translator, this is a Python script, that  automatically generates CSV documents "
      "for translating your application in to different languages. For further information's pleas contact "
      "philipp.buesgen@atos.net")
print()
print()

menu.main_menu()


