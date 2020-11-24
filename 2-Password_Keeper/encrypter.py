from Crypto.Cipher import AES
from json import loads as to_dict
from json import dumps as to_string


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
