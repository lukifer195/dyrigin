import os
from shutil import copyfile
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys
import hashlib
from cryptolize import hashfile


def create_hashDYSvCHECKER(inputstr):
    ''' ghép 2 chuỗi hash vào file KEYGEN.txt'''
    with open(path_key + '\\hashDYSvCHECKER.txt','wb+') as keygen:
        keygen.write(bytes(inputstr,'utf8'))
    print('\nĐã tạo hashDYSvCHECKER')

def encryptize_to_LICENSE(key):
    # print('KEY generate by Fernet: ',key)
    # print('x',len(key))
    with open(path_key+'\\hashDYSvCHECKER.txt','rb+') as file:
        readfile = file.read()
    f = Fernet(key) 
    encrypted = f.encrypt(readfile)
    with open(path_key + '\\LICENSE.txt','wb+') as file2:
        file2.write(encrypted)
    print('\nENCRYPT hashDYSvCHECKER: ',encrypted)
    print('len encrypt hDvC: ',len(encrypted))
    # d = f.decrypt(encrypted)
    # print('DECRYPT: ',d)
    # print('x',len(d))
    return encrypted


# def decryptize_LICENSE_to_test(key):     #dung cho dynasty
#     with open(path_key+ '\\LICENSE.txt','rb') as keyfile: 
#         decrypt_file = Fernet(key).decrypt(keyfile.read())
#     print(decrypt_file)
#     return decrypt_file

if __name__ == '__main__':
    path = 'E:\\Export_exe\\'
    # path = os.path.dirname(sys.argv[0])
    print('PATH: ',path)
    path_key = path + '\\__KEY'
        # TẠO ra LICENSE cho CHECKER(KEYGEN)
    hashDYS = hashfile(path + '\\Dynasty.exe')
    print('\nhashDYS:', hashDYS)
    print('len hashDYS:',len(hashDYS))

    hashKEYGEN = hashfile(path + '\\KEYGEN.exe')
    print('\nhashPNG :' , hashKEYGEN)
    print('len hashPNG: ',len(hashKEYGEN))


    create_hashDYSvCHECKER(hashDYS + hashKEYGEN)        # x128
    # create_password_encrypt('enol')      #dùng để tạo pass crypto
    
    pass64enol = b'9YJa0qTRWbO2bmfFP_8hNy_ecPVe5dn3XZz_kNCe1R4='   #pass là enol
    encryptize_to_LICENSE(pass64enol)                   #x268
    # decryptize_LICENSE_to_test(pass64enol)            # compare hashDYSvCHECKER
