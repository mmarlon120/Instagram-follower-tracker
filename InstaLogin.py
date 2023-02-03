import json
from cryptography.fernet import Fernet


def load_key():
    return open(".dfbec.key", "rb").read()

    #The file is file.read() not the raw file
def encryption(file):
    newkey = Fernet.generate_key()
    with open(".dfbec.key", "wb") as key:
        key.write(newkey)
    fernet = Fernet(newkey)
    encrypted = fernet.encrypt(file)
    return encrypted

def decryption(token):
    key = load_key()
    fernet = Fernet(key)
    decrypt = fernet.decrypt(token)
    data = json.loads(decrypt.decode())
    return data


def login_data(username):
    with open("logindata.json", "rb") as file:
        token = file.read()
        data = decryption(token)
        if username not in data.keys():
            password = input("Input password: ")
            data.update({username : password})
            print(f"{username} has been added to the database")
        else:
            password = data.get(username)
            print(f"{username} | {password}")
    with open("logindata.json", "w") as file:
        json.dump(data, file, indent = 6)
    #This is where the encryption starts

    with open("logindata.json", "rb") as file:
        data = file.read()
        encrypted = encryption(data)
    with open("logindata.json", "wb") as file:
        file.write(encrypted)

username = input("username = ")
login_data(username)
