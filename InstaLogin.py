import json
from cryptography.fernet import Fernet


def load_key():
    return open(".dfbec.key", "rb").read()

def login_data(username):
    with open("logindata.json", "rb") as file:
        #Start of the decryption process
        oldkey = load_key()
        tokendata = file.read()
        oldfernet = Fernet(oldkey)
        decrypt = oldfernet.decrypt(tokendata)
        data = json.loads(decrypt.decode())
        
    #This is where the actual data is sorted

        dic = data
        if username not in dic.keys():
            password = input("Input password: ")
            dic.update({username : password})
            print(f"{username} has been added to the database")
        else:
            password = dic.get(username)
            print(f"{username} | {password}")
    with open("logindata.json", "w") as file:
        json.dump(dic, file, indent = 6)
     
    #This is where the encryption starts

    with open("logindata.json", "rb") as file:
        data = file.read()
        key = Fernet.generate_key()
        with open(".dfbec.key", "wb") as file:
            file.write(key)
        newfernet = Fernet(key)
        encrypted = newfernet.encrypt(data)
    with open("logindata.json", "wb") as file:
        file.write(encrypted)

username = input("username = ")
login_data(username)