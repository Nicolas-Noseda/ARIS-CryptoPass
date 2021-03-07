import sys
from src.classes.app import CryptoPassApp


def main():

    app = CryptoPassApp(sys.argv)
    sys.exit(app.run())


if __name__ == "__main__":
    main()
