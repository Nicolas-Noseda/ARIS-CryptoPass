import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
import src
from classes.app import CryptoPassApp


def main():

    app = CryptoPassApp(sys.argv)
    sys.exit(app.run())


if __name__ == "__main__":
    main()
