import os


def get_path():
    return "C:/Users/a764963/OneDrive - Eviden/Desktop/Translation Skript"


def set_path():
    os.chdir(get_path())


def get_languages():
    return ["de","es","id","pt","th"]
