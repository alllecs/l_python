from simplecrypt import decrypt, DecryptionException

with open("encrypted.bin", "rb") as inp:
        encrypted = inp.read()
with open('passwords.txt', 'r') as pswd:
    x = pswd.read().strip().split()
for i in x:
    try:
        mystring = decrypt(i, encrypted).decode('utf8')
    except DecryptionException:
        pass
    else:
        print(mystring)
