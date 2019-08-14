import os.path
import os
from shutil import copyfile
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys
import hashlib




"""_________________________fake png__________________________________"""

def fake_license():
    hexPNG = bytes(b'\x39\xb4\xc9\x1a\x00\x01\xd9\x23\xe1\x00\x00\xcb\x43\x32\xec\x13') #16 mã giả
    print('len fake PNG',len(hexPNG))
    hexIEND = bytes(b'\xd2\xcb\xf3\x3e\xe4\x9d\x89\x4e\x83')                       #9 mã giả
    print('len fake IEND', len(hexIEND))
        #chèn mà fake
    with open(path_key + r"config.file", "rb+") as file:     # xoá .txt r compile
        file.seek(0,0)
        file.write(hexPNG)
        print('replace fake PND')
        file.seek(-len(hexIEND),2)
        file.write(hexIEND)
        print('replace fake IEND')
        file.close()
    print('Fake license success')


# def test_fake_ok():
#     copyfile(path_key +'config.file', path_key +'fakepng2real.png')
#     hexPNG = bytes(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00') #16 mã real
#     print('len real PNG',len(hexPNG))
#     hexIEND = bytes(b'\x00IEND\xaeB`\x82')                       #9 mã real
#     print('len real IEND',len(hexIEND))
#         # chèn mã real
#     with open(path + r"test.png", "rb+") as file:         # xoá .txt r compile
#         file.seek(0,0)
#         file.write(hexPNG)
#         print('replace real PND')
#         file.seek(-len(hexIEND),2)
#         file.write(hexIEND)
#         print('replace real IEND')
#         file.close()


def real_license(filename):
    hexPNG = bytes(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00') #16 mã real
    # print('len real PNG',len(hexPNG))
    hexIEND = bytes(b'\x00IEND\xaeB`\x82')                       #9 mã real
    # print('len real IEND',len(hexIEND))
        # chèn mã real
    with open(filename, "rb+") as file:           # xoá .txt r compile
        file.seek(0,0)
        file.write(hexPNG)
        # print('replace real PND')
        file.seek(-len(hexIEND),2)
        file.write(hexIEND)
        # print('replace real IEND')
        file.close()

"""________________________hash____________________________"""


def hashfile(filename):
    '''sha256 with enol'''
    h = hashlib.sha256()
    with open(filename,'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
           # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
            h.update(b'enol')
    return h.hexdigest()

def hashstring(inputstr):
    """sha256 string input with salt"""
    h= hashlib.sha256()
    h.update(inputstr)
    h.update('enol')
    return h.hexdigest()

###___________________________CRYPTO__________________________###



def create_password_encrypt(password_provided):   #dùng 1 lần
    """ password provided : string
        -> password base64
    """
    # password_provided = ".kImOcHi"
    password = password_provided.encode() # Convert to type bytes
    salt = b'enol' # CHANGE THIS
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10000,
        backend=default_backend()
    )
    pw = base64.urlsafe_b64encode(kdf.derive(password)) 
    # print('Pass encrypt',password_provided,'là', pw)
    return pw



def encrypt_input(input,key):
    """ messsage:   string
        passbase64:   bytes
    """
    encrypted=Fernet(key).encrypt(input)
    # print('ENCRYPT: ',encrypted)
    # print('x',len(encrypted))
    return encrypted

def decrypt_input(token,pwbase64):
    """ token: string
        pwbase64: bytes
    """
    decrypted=Fernet(pwbase64).decrypt(token)
    # print('DECRYPT: ',decrypted)
    # print('x',len(decrypted))
    return decrypted


def encryptize_to_KEYGEN(data,key):
    """
    """
    key = b'9YJa0qTRWbO2bmfFP_8hNy_ecPVe5dn3XZz_kNCe1R4='
    # print('KEY generate by Fernet: ',key)
    # print('x',len(key))
    
    keyfile = open(path+'KEYGEN.txt','rb+')
    readfile = keyfile.read()
    f = Fernet(key)
    encrypted = f.encrypt(readfile)
    keyfile.close()
    file2= open(path + 'KEYGEN2.txt','wb+')
    file2.write(encrypted)
    file2.close()
    # print('ENCRYPT: ',encrypted)
    # print('x',len(encrypted))
    # d = f.decrypt(encrypted)
    # print('DECRYPT: ',d)
    # print('x',len(d))
    return encrypted


def decryptize_LICENSE_to_test(filename):     #dung cho dynasty
    key = b'9YJa0qTRWbO2bmfFP_8hNy_ecPVe5dn3XZz_kNCe1R4='
    keyfile = open(filename,'rb')
    decrypt_file = Fernet(key).decrypt(keyfile.read())
    # print(decrypt_file)
    return decrypt_file

if __name__ == '__main__':
    s= hashfile(r'E:\PyProject\Pydctq\scr\lsb.png')
    print(s)
    print(type(s))
#     # s= '7b02ebe8996fc33e94c5f0fe467cafc9dfe6b2419e659fdd234d16697cff10d9'
#     # print(len(s))
#     file = open(r'E:\PyProject\Pydctq\scr\lsb.png', 'rb')
#     ss= file.read()
#     print(ss)
#     file.close()