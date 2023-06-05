import os


def apk_path():
    return os.getcwd().replace('\\', '//') + "//app//base.apk"
