import os


def create_new_files(user):
    path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "files" + os.path.sep + user + ".encrypted"
    open(path, "x")