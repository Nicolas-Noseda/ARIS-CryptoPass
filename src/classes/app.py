from PyQt5.QtWidgets import QApplication

from src.windows.main_window import MainWindow


def get_app():
    return QApplication.instance()


class CryptoPassApp(QApplication):

    def __init__(self, *args, mode=None):
        QApplication.__init__(self, *args)
        self.window = MainWindow(mode=mode)
        self.window.show()

    def run(self):
        return self.exec_()

