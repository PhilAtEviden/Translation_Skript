import sys
import pandas as pd

import initUt

def check_directories():
    print("Startup.....")
    if not initUt.check_if_CSV_directory_exists():
        print("Missing Directory: /CSV")
        print("Do you want to create this Directory?")
        if input("[y/n]") == "y":
            initUt.create_CSV_file()
            print("Done!")
            print()
        else:
            print("Canceled!")
            sys.exit()
    else:
        print("CSV directory:\t\t\t\t\tOK!")

    if not initUt.check_if_JSON_directory_exists():
        print("Missing Directory: /JSON")
        print("Do you want to create this Directory?")
        if input("[y/n]") == "y":
            initUt.create_JSON_file()
            print("Done!")
            print()
        else:
            print("Canceled!")
            sys.exit()
    else:
        print("JSON directory:\t\t\t\t\tOK!")

    if not  initUt.check_if_applications_match():
        print("Error: Directories in '/JSON/imp' an '/JSON/exp' has to match!")
        sys.exit()
    else:
        print("Application files match:\t\tOK!")

    if not initUt.check_if_application_exists():
        print("No Application detected!")
        print("Do you want to create a new application now?")
        if input("[y/n]") == "y":
            application_name = input("Enter Name:")
            initUt.add_application(application_name)
            print("Done!")
            print()
        else:
            print("Canceled!")
            sys.exit()
    else:
        print("Application files exists:\t\tOK!")

    if not initUt.check_if_master_csv_exists():
        if initUt.check_if_master_xlsx_exists():
            print("No CSV version of your master table detected!")
            print("Do you want to create a csv file out of your xslx version of the master table?")
            if input("[y/n]") == "y":
                master = pd.read_excel('CSV/master.xlsx', index_col='key')
                master.to_csv('CSV/master.csv')
                print("Done!")
                print()
            else:
                print("Do you want to create a new master csv file?")
                if input("[y/n]") == "y":
                    initUt.create_master_table()
                    print("Done!")
                    print()
                else:
                    print("Canceled!")
                    sys.exit()
        else:
            print("Do you want to create a new master csv file?")
            if input("[y/n]") == "y":
                initUt.create_master_table()
                print("Done!")
                print()
            else:
                print("Canceled!")
                sys.exit()
    else:
        print("Master files:\t\t\t\t\tOK!")



