from Crypto.Cipher import AES
import json
import os
from getpass import getpass


class Passwords:
    def __init__(self, user_password, user_iv='RedRiverDevOps!'):
        password = user_password
        if len(password) > 16:
            password = user_password[0:16]
        else:
            while len(password) < 16:
                password += ' '
    
        if len(user_iv) > 32:
            iv = user_iv[0:32]
        elif len(user_iv) > 24:
            iv = user_iv[0:24]
        elif len(user_iv) > 16:
            iv = user_iv[0:16]
        else:
            iv = user_iv
            while len(iv) < 16:
              iv += ' '
        self.aes = AES.new(password, AES.MODE_CBC, iv)

    def decrypt(self, ciphertext):
        cleartext = self.aes.decrypt(ciphertext).decode()
        i = -1
        while cleartext[i] == ' ':
            i -= 1
        i += 1
        value = cleartext[0:i]
        return value

    def encrypt(self, cleartext):
        while (len(cleartext) % 16) != 0:
            cleartext += " "
        ciphertext = self.aes.encrypt(cleartext)
        return ciphertext

class Database:
    def find_by_cli(self):
        while True:
            user_input = input('Database File:  ')
            try:
                f = open(user_input,'rb')
                f.close()
                break
            except FileNotFoundError:
                continue
        self.file = user_input

    def open_db(self, password, iv="", pw_file=""):
        if pw_file == "":
            pw_file = self.file
        try:
            with open(pw_file,'rb') as file:
                ct = file.read()
        except FileNotFoundError:
            print('File Not Found')

        decrypter = Passwords(password, iv)
        pt = decrypter.decrypt(ct)
        del decrypter
        self.db = json.loads(pt)

def pager(json_dict, tab=0):
    result = ""
    if type(json_dict) == dict:
        for i in json_dict:
            print(" "*tab + i)
            pager(json_dict[i], tab+1)
    elif type(json_dict) == list:
        for i in json_dict:
            pager(i, tab+1)
    else:
        print(" "*tab + json_dict)


if __name__ == "__main__":
    db = Database()
    db.find_by_cli()
    user_password = getpass("Database Password:  ")
    user_iv = getpass("IV Key:")
    db.open_db(user_password, user_iv)
    print(db.db)

