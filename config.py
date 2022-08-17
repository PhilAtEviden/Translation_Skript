import os


def get_path():
    return "C:/Users/a764963/OneDrive - Atos/Desktop/Test"


def set_path():
    os.chdir(get_path())


def get_languages():
    return ["zh"]
