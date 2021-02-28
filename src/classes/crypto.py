import base64
import os
from os import path

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class CryptFile:

    path_to_files = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "files" + os.path.sep

    def __init__(self, passphrase):
        print(self.path_to_files)
        salt = b'30R8IF8fFgFnfe37'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=256,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(passphrase))
        print(self.key)

    def encrypt_file(self, password_file, user):
        file_path = self.path_to_files + user + ".encrypted"
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(password_file.encode())
        if os.path.exists(file_path):
            os.remove(file_path)
        with open(file_path, 'wb') as f:
            f.write(encrypted)

    def decrypt_file(self, user):
        file_path = self.path_to_files + user + ".encrypted"
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                data = f.read()

            fernet = Fernet(self.key)

            try:
                decrypted = fernet.decrypt(data)
                return decrypted.decode()

            except InvalidToken as e:
                print("Invalid Key - Unsuccessfully decrypted")





