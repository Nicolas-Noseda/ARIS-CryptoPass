import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon

from src.windows.main_window import MainWindow


def get_app():
    return QApplication.instance()


class CryptoPassApp(QApplication):

    def __init__(self, *args):
        QApplication.__init__(self, *args)
        list_user = self.retrieveListOfUser()
        self.window = MainWindow(list_user=list_user)
        self.window.show()

    def run(self):
        return self.exec_()

    def retrieveListOfUser(self):
        list_user = []
        if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "files"):
            os.makedirs(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "files")
        list_files = os.listdir(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "files")
        for file in list_files:
            if ".encrypted" in file:
                file = file.removesuffix(".encrypted")
                list_user.append(file)
        return list_user






