import tempfile
import os
import sys
from cryptolize import hashfile
import random
import string
from cryptolize import encrypt_input,create_password_encrypt
from subprocess import call

def create_tmp_png():  
    with open (path_temp + r'\\c423dys423.tmp','wb+') as config:
        config.write(png)
    # print('tmp success')

def fake_license():
    hexPNG = bytes(b'\x39\xb4\xc9\x1a\x00\x01\xd9\x23\xe1\x00\x00\xcb\x43\x32\xec\x13') #16 mã giả
    # print('len fake PNG',len(hexPNG))
    hexIEND = bytes(b'\xd2\xcb\xf3\x3e\xe4\x9d\x89\x4e\x83')                       #9 mã giả
    # print('len fake IEND', len(hexIEND))
    with open(path_temp + r'\\c423dys423.tmp', "rb+") as file:       # xoá .txt r compile
        file.seek(0,0)
        file.write(hexPNG)
        # print('fake lincense replace PND')
        file.seek(-len(hexIEND),2)
        file.write(hexIEND)
        # print('fake license replace IEND')
    # print('SUCCESS fake')   

def garenate_configfile():
    with open(path_temp + '\\c423dys423.tmp','rb') as file:
        gettmp = file.read()
    with open(path+ '\\config.file','wb+') as file:
        file.write(gettmp)
# # dung cho dysnaty
# def real_license():         
#     hexPNG = bytes(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00') #16 mã real
#     print('len real PNG',len(hexPNG))
#     hexIEND = bytes(b'\x00IEND\xaeB`\x82')                       #9 mã real
#     print('len real IEND',len(hexIEND))
#         # chèn mã real
#     file = open(pathscr + r"\\config.file", "rb+")           # xoá .txt r compile
#     file.seek(0,0)
#     file.write(hexPNG)
#     print('replace real PND')
#     file.seek(-len(hexIEND),2)
#     file.write(hexIEND)
#     print('replace real IEND')
#     file.close()

if __name__ == '__main__':
    path_temp = tempfile.gettempdir()
    path = os.path.dirname(sys.argv[0])
    png = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc2\x00\x00\x000\x08\x00\x00\x00\x00f\xd0\xfa\xff\x00\x00\x0c\xb2IDATh\x05\xd5\xc1{X\x94u\xa2\x07\xf0\xef\xef\x9d\xfb\xc0pu\x10\x94\x94\x8b\xbe\xa0\x13\xe8\xa6\xd2(a\x1d\xd3\xb4\xd5,\xd7Y\x8d\x1aF\xf3\x96Z\xb6s\x8e\xb6\xba^:j2\xfah\xb9\x06Y\x9b\x8fR\x8e\x88\x95\xa6\xae\xba\xb3\xa5fD^h(WA8\xce\x8fDQ\x94\xcb 0\x0c\xc3\xdc\xdew\xde\x83pL\xdcS\x9d\xe7l\xfd1}>\x84\xe2\xd7\x8eP\xf4"\x04\x040\x0cx?\xcf32\x11\x83_\x05B\xd1\x0b\xef\xf3\x11\x99\x84x;N\xa5\xa8B\x152\xc2\x10B\x00\x01\x10\x00\x02\x82\xa0D(\xee\x11\xbc\x8eo\xa3RC\x88\xa3\xaeX!J\x8a\n\x91HdR\t\x02\\ \x00"\x92\x8aE\x04\xc1\x88P\xdc\xc3\xb7\xdf\xac\x90\x8eP\xf9\x1b.*N>T\x1f\x17!R(#\x94\x8c\xdf\xed\x83X$\x8a\xea+%\x08F\x84\xe2\x1e\x7fSYd\xf90\xb9\xf3\xca\xad\xea\x89\x8dJ\x8f(D\x088"\xfd\x9d\x1e\x89\x98\xe3\xc9\xf84\x19\x83`D(\xbe\'\xb8k\xf7L=\x1a\xc23\xad[\x17\xc67\xa8\xcac\x1e\x88\xaf\xa9W\xcf\x8a\xdb]\x82\x81\x9a\x146RJ \x08`\x10d\x08\xc5]\x02\xd7r\xd9\xfco\xdf\x88e\xfeq\xc7\x02nU\xac\xf7\xe1\x7f|\x1e\xfez\xfc\x0b\x9c\xe6V\xfa\xe0\xa4\x18\x95\x8c!\xbc\x9fg\x14\x082\x84\xe2.\xceY{&\xcc\xff\x95\xdb;[\xb3\xb1o\xb3\xdf\x1d!vE\xaf/:P\xa3\x8e{\xac%A3 \\Bx\xb7\xf3\x96h8\x82\x0c\xa1\xe8\x11\xf0;o\x9e>ytaU\xd4\xa2\xc7\xe7\xca\xd0\x12\x96\x12\x9f\xd8\'dM\xf1\xa2\xa3^\xbb\xfa\xd1\xd0>\xa3\xe3Up7_\xbb\x95\x90\x89 C(\xba\xf1\xde\x96[\xe5\x17\x16?<j\x90)z\xc7\xb7\xfc\xa4qJ\xee\xf6U\xebi\x9bzr\x89\x13\xb0\xcfq\xc7g\xc5\xa2\xd9\xe6\xbc6a\x04\x82\x0c\xa1\xb8Cp7\xd1\xea\x96\xea\xe3\x97\xd6\xe7w\x9e\x7f\xe1\xf7\xabEMGJn\xd8\xd5*\xdf\xd0i[j\xe2\xbd\xf6\xf8i\x15\x93\x92\x03\xd5\xf6\xf8\xfaI\t\x082\x84\xe2\x0e\xbf\xddVu\xeb\xdb\x05O\x1f\xcf\x12\xb7l\x1b\xaek\xf9f#b\x86MI\x95\x86\xcb\xf3>\x9dy\xfe\x84\x1d\x8b\xed\xae\xb4\xd6\xd8A\x07\x9fM\x8cD\x90!\x14]\x84\xf6\xab\xa7\xeb\xaf%\xbc\xd7\xb0"\xfbA\xa7\xe0\xf2]\\\xa5\x99\xa1p\xb4\x8bf+<\x90\xf8\xbd\x1f\x9e\xbd2\x0c\xf5\x89s\xaa?\xcbI\x8e\x94!\xc8\x10\x8a.\xbe\xfa\xb2\xef*\xf8e\xbf\xf1\xc9\x04\xbf\xab\xd5\xe3{6}P\xd8\xf8\xef\xc2\x86\xc4\xba<\x01\x91H\\\x91\xacp\nLgn\xfc\xf4\xc4p\x19\x83 C(\x00\xc1Y\xf3i\x85\x94I[\xdc\xe0\x8e\x10<\x1e!\xe0\x8f\xf5\xbc\xff\xfc\x00\x0f\xc3;\xdd~Hl\xcb^\x19\xef\xfc\xee\xaf7&\x8dO\n\x972\x086\x84\x02\xe0\x9a*\xaa\x0f&\x8a\x9eNY\xe0=\xde\xee\xe1\x03\x17*\xca\xf4q\xb5\x83\x99C\xac+5\xd1/!\x7fn\xe3\xbca\x91\xbe\xcc\x87\x12B\x18\x04\x1dB\x01\xb8k\x8f\xde,\x8f\xd2-\xaa\xdb62\xb3#`)\x92\x86BU\x1b\xd7\xeeWL\x9f\xd2\xf8\xd5(F!v}R5\xd2\xe1\x0e\xe8\xd8\x081\xee\xd7p\xfe\x814\xfc+\x84\x8a7\x80\xe7\'\xe2G5\x9c\x07 \x8ayP\x82\xff\x03\xa1@\xc0a+\xfe\xda1uEK\xa7\x10\xe2\x17`9!Q6\x88D>\x8e\x87c\xf8$\x87\'\r\xdf\xa5G\x17\xd5\xb71\xbe\x84\xdf\xf7W\x10\xdc\xc7b\xd4\x99\xf0/\xb8\x9cw\x12]\x92\xb6\'\xe3GX\x8c\xe86gq\x18~\x12\xa1\x00g\xff\xa6<V\xaco\x14N\xafI\xdf!9\xd1,\xbfa\x03\xcfK}\x1c\xf8\xa6B\x9be\xfe\xbe\x03\xda5\xea\x15\x15\x88Q\xbe\xc4F\x8ap\x1f\x8bQg\xc2\xff_[\x8e-{2\x02\xa7w\xc4\x1f\x0e\xc3\x0f\xb3\x18\xb3^\x04n\xfc\tS7\x89\xf1S\x08\x05|7\x8f\xfd\xc9\xdb\xe4\x13o\xb90\xe5`\x81\xea\xc5\xa8z\xb1R>\xb0J\xc4s<\x07\xd7\xbc\xd2Y\x17wm\xec\xc7\xbbgh\xfa\xbb\x1f\x1e\xd7_\x81\xfbX\x8c:\x13~\x88\x87\xc8p\x97/ G\x0f?/\xc7\x1dV\xbdf\xaf\x12\xc0S6\xad\x19]<D\x86\xbb|\x019\xbaX\x8c:\x13\x80\x8a\xe9\xea\xbd\t\xe8\xe2\xe5\x14\x0czx \xc7=\x84\x02\xde\xda\xa2\xdcZqQ\x95\xe7\xcdK[\xf3\xb9\xa6\xeasm\xdc\xce\xdfE\x899\xf0\x1c`:\x9f*}\xb7x\xb5\xb6\xff\xac\x98\x0e\xe0\x95\xc1a\x04\xbdY\x8c:\x13\xba\xe5\xdaV\xa6\x020\xc0\x0c\xe0\xec_:\xa1\\4\x1a\x80\x01oo\xb8\xce)\x97k\x00t\x98j8\xe5\xab[`\x86U\xaf5\xa3K\xa9Ak\x06\xce\xfe\xa5\x13\xcaE\xa3\x01\x18\xf0\xf6\x86\xeb\x9cr\xb9\x06\xb0\x18u&\x00\xed\xb3*\x0b3\x00\xba\xce\xcb+SV\x8a\x01\x14\x17tB\xb9h4\xee"\x14p_\xdd\x9b\xde|5!o\xd4\xe4\xbf\xb5\xefY}\\\x1d\x15\xd6\xf9q\x8eW\x04\x9e\x83_\xb1\xbe<\x89O[wl\xca\xb2/\x8b\xc4P\xcd\xd1D3\xe8\xcdb\xd4\x99\xd0\xcdPZ\x98\x01\x80\x05E\xe0\xe8\xab\xd0p6l\xfd-\x03\x16\x8fUF\xd9\x80\xb2px\x96\x1dG\x8a\xab\x0e\xa0\xb0\xea\x93\xdeIB\x8f\xc0\xd1W\xa1\xe1l\xd8\xfa[\x06,\x1e\xab\x8c\xb2\x01e\xe1\xb0\x18u&\x0059\xf6C\x1a\xfc\xfd\x0f\xb2\x04\xf1\x15\xcf\x82e\xe0\xf7\xbf\x06\r*\x917\x91\xa0\x07\xa1\x80\xab\xdaR\x97h/\x1feO\xac70\x05\xb7yN\xcc\xb5\xec\xb0\x9a\x15\x1c\xd0\xb2\xb0bl\x84\x9c\x1b\xbcs\xd7\x94\xfc\x17\x8a\x93b\xf4\xe91\x0cz\xb3\x18u&t3\x94\x16f\x00`AQ9\r\xab\xa6\xe1P.\x0ei\xc0"%?\xf2z~\xf13\x9b\xb1\xe6#|2\xc0\xf1\x87JP\xb4\xe5\xd8\xe2\x1fz9\x01wTN\xc3\xaai8\x94\x8bC\x1a\xb0H\xc9\x8f\xbc\x9e_\xfc\xccfX\x8c\xea?\x83?\xf4_\xb6u3\x19d\xda\xb7\x8d\x11U\xcc\xc6\xb9\xe8K\xbfS\xaf\xc9\x14\x0e\xe5\xe2\xf0P\xf4 \x14h\xab:\x90\xfc\xb5D[7\xf0\xd0\xd4\xa7.\xeci\x87\x0c\xe0\x9bV\x95\\\x08\xed\x80\xe4\xf5\xe21\xf6\x7fO\xda\x96\xa0/\xd7lX\xe1\x8f\x9e\x9d\x16\xc3\xa07\x8bQgB7Cia\x06\x00\x16\x14{\xd7i\xcd\x80\xa0/[\xff,X\x94\xcb\x81\x92yZ\xb3G_\xbes,\xc0\r\x05\x05\xdc/\\\xee\x04\xe6?9D\x84\xbd\xeb\xb4f@\xd0\x97\xad\x7f\x16,\xca\xe5@\xc9<\xad\x19\x16#\xba\xe5,\x8e\x06\x0c0\x03`\xb1+\xcb\xbcAk\x06xCYa\x06z\x10\n\xdc\xbeX\xdd\xe4h\x1fUW\x1ew\x11PI \x06\xc0\x8d\x1ai\x1eZ\x1c\xfer\xe1\x12\xee\xf0\x97\x7fT\xab\xaf\xbc\x02\xcc\x8e\xf9b\xf6\xf0h\x06\xbdY\x8c:\x13\xba\x19J\x0b3\x00\xb0\xa0\xc8\xb4\x9bt\x00>Z\xa3>\x03\x16\x14\x80U\xaf57<\xe7-L\x04\xc0\x82\x02\xe0\xab\xaen\xab\x036\xcc@\xa6\xdd\xa4\x03\xf0\xd1\x1a\xf5\x19\xb0\xa0\x00\xacz\xad\x19\x16c\xd6\x8b\x80\xe7\xd8\xe1\xcc7\xa3\x00xl\x0ea>\xde\x19\x9fi_\xfb\x1c\x80\xcb\xed\xa9a\xe8A(\xd0\\^srhyl+\x1f[\x0e) A\x17\xff\x0c\xb9y\xce\xea\x05\xe2q~\xff\xa7E\xf9\xa1\xa1\xd2\xed\xadeH\xc7\x92\xf4p\x06\xbdY\x8c:\x13\xba\x19J\x0b3\x00\xb0\xa0`q$\x15@\xc5tP\xb0\xa0\x00\xacz\xad\xd9\xaaO\xda\x1b\r\x80\x05E\x0f\xe7\xc6\x03x\xf7q\x16GR\x01TL\x07\x05\x0b\n\xc0\xaa\xd7\x9aa1\xeaL\x008\xfd\xf9-O\xa3\xf6\xc5\x1a\xdc\xb1}\x02\x8bO\xd2p\x1fB\x01\x87\xed\xa8\x93k\x88\xe1\xa47\x9b \x93\xa2\x9boG\xdeU\xd3\xc7OEtzx\xf7\xe2qsD\xb1s\xc7\x94\xb5\xfc&zF\x82\x82Ao\x16\xa3\xce\x84n\x86\xd2\xc2\x0c\x00,(X|<\x1c@\xd9\xf3\xa0`A\x01X\xf5Z\xb3U\x9f\xb47\x1a\x00\x0b\x8a\xeb\xded\x06]vn\xd6\x9aY|<\x1c@\xd9\xf3\xa0`A\x01X\xf5Z3,F\x9d\t]\xcc\x1b\xe2Oa\\]\xca\n\t\xf4\xd8>\x81\xc5\xee\xd1\xb8\x0f\xa1\x80\xbb\xeeom\xcd\xe2\xf0\xdb\xed)b\xcd\xa5\xe3R\x00\xbe\xf0\x8d\x8d\xf9[\x8a\x86\rj\x17\xb9|1\x1f\xd6\xcf\x8c\x8a\xcd\x8eJ\xa4\xd1\x86a\xbe\x07\x08z\xb3\x18u&t3\x94\x9a\xb5@ \x15\x14\xa6\x0f\xb4f\x00\x86\xd2\xb9\xcb\xc1\x82\x02\xb0\xea\xb5\xe6\xc6Y5\x85\x19\x00XP\xb08\x92\x8a.V\xbd\xd6l\xfa@k\x06`(\x9d\xbb\x1c,(\x00\xab^k\x86\xc5\xa83\xa1K\xd1Z\xf5\x19\xab\x1e\x14\x00\x8b\xed\x13rwk\xcd\x00.\xb7\xa7\x86\xa1\x07\xa1\x00\xdfv\xa5\x10\x01\x97&\xcc\xa1W6\xbeQ\x19\xe5B\xd4\xfeK\x9bt\xb1onn\x0e|\xbe[\xb3\xb6\xbc\x8c\xe6\xc6\xcf\xaa\x99Z\xafZ\x94\xa0"\x04\xbdY\x8c:\x13\xba\x19J\xff8\x0fx}\x0f(J\xe6\xa5\x14\x86\xa3\xd5`\xdb9\x16,(\x00\xab^k\xe6\xf4\xe7_\xd3\x03\xb9\xbbA\xb1\xa9`\xfcV9\x80\xb7\xf3\xb4\xe6\x92y)\x85\xe1h5\xd8v\x8e\x05\x0b\n\xc0\xaa\xd7\x9aa1\xeaL\x00\\\xfa\xca\r3J\xe6\x81\x02\x15\xd3\xb1}B\xf1\x02\xcd\x9eP\xb4\xe5\xd8\n3\xd0\x83P@\xf0\xd9mEMKN\x8e\x1d\xe4\x8b\xab\xf7|\xc6\xb4\x9e\xcbc\xaa>\x8c{\xf9\xa3\x89\xe2\xf3y\xb95O~\xf5E\xbf\xa8\xd9\xef\xef\xd3\xd5d\x8f\xea#!\xb8\x8f\xc5\x88\xa5\xb8#E=\rK\x86\x96\xec\x03(\\KOe\xe5\x04\x16b\xfc\x96\x10\xb0\xa0\x00\xacz\xad\x19\xe7fa\xee\xe8\xd3\x1f\x00\x14\x97\xa7\x02\x9b\xfb96\xd6\xa9\xf7$\xb9\x96\x9e\xca\xca\t,\xc4\xf8-!`A\x01X\xf5Z3,F,\x85\xd0\xf2\x01p$\xb5}$\x92\xe6\x7f}\x18X9\xdb\xb9\xb4\xf8\x89\x99\x9e\x970e\xa3\x0c=\x08\x05\x10\xf0\xb4\xd4\x9cM\xf6\xed\xd9\xf4\xe9\xdc\x1a\xf7A\x95\xe3\xf8\xccgv\xad\xda\x17\xdb\xf7\xd6\x10\xbd\xfa\r>r\xff\t\xd8\xe7g\xcf\x1c/\x9e\x92\x1c\xca\xe0~\x16#zh\xcd;7\x03X\x95\x0b\n\xb4\xbc\xb5\x0f@\xb61\x12`A\x01X\xf5Z3P\xb0\t\xc0\xe2w@\x81\xcb\x87\x0b\xd0%)\x8f\x05Z\xde\xda\x07 \xdb\x18\t\xb0\xa0\x00\xacz\xad\x19\x16#\xbaeg\xa7\x02\x05\x9b\x00\x18o\xee\xd7\x9a\xd1\xfc\xc6A\x00s\x17\xab\xf0?\x08E\x97@GMYq\xfb\xd4#\xfem\xad\x95\xe7T\xce\xbe_.\xf7|\x96<\xfe]U\xbf\x82\xa4\xd7\x10\xbeZU\n\xe8F\xec\x9f4f\x80\x8c\xe0\xc7y.\x88\xd2\xe4\xe8\xe1\xa8\xc2\xd0p\xfc\xb3\xc0?<\x0f\xca\xd3@q\xc7\xa5\xc6\x90t%\xba9\xaa04\x1c?\xc5{\x11\x9a\x10\xf4h\xbdL\xd2\x95\xf8\x1e\xa1\xe8"\xb4\xd3\x9bM\x7f\x8fr\xd4\x9b$y\xae\xc4\xc9\x8a\xf7rB\xdd\xf2\x8a\x0bc??3nV\xc4\x17\'\xd4\xc5\x80Z\xf3\xa8}r\xbc\x9c\xe0\xe7\xfa\xcf}\xa0\xf8%\x11\x8a.B[y\xe3)(/x\xd7\x86\xdc\xde\xbe\x96\xbb\x11\xa3p*A+/\x14<\x915\xbf\xdfK\xc9\xb5\x95H\t\t\x91\xc4\x8eyD\xce\xe0g`u\x93%\xd6<\xec\xca\xc2/\x89Pt\x11:\xae\xed\xae\xd3\xdcl\x1c\xf5\xa8\x98\xc9\x8f\x7f\xf2Z\xf2\x81c\xef\x89p\xb0\xe1\xad\xac\xf8\xad\xde\rq\xc5\xd0D\x89"\x1eQ\'EH\t~\x86\x05\xc5\xe8\xb2y\xb2\x04\xbf$B\xd1E\xf0\xb5\xd5U\x9e\x17GVe9\x93\x07\\\xeaH\xe4\x1d\x7f\x9d>\x80@\xd6\xf0\xe57\x1bo\x16\xb5\xd4i"|\x91\x8f\x0eS+$\x0c\xc1\xcf\xd1|\xd1\x15;\\\x8a_\x16\xa1\xb8#\xe0\xefh,?:R\xfd\xc5U\xef\xc3\x0b\xde\xae\x95\xf5\xb9\xa6\x1b\n"\xcd\xce\xb96&tM<\xeb\xec\x1c\xf8\xe0#\xfd\x95\x0cA\x10"\x14\xdd\x84@\xa7+\xd0\xd9\xb8/\x1a\x95\x99O\xd4\x1e\xb6;\xfe\xa3\xaf\x1f\xb3S\x86Ts\xc6\x02U3?x\xe0\xd8x\x95\x18A\x89P\xf4\x10\x04.\xe0\xb1\xbf\x19\x08\xedl[J\x84N%Ox\xf9\xca\xf4\xeb\\\xfd\xe2]\x88\x89ydH\x7f\x95\x98 (\x11\x8a\xef\t\\\xfb\xd5\xd3\x97C\xebEK\x04\x8e\x08b\xc5\xfb\x8e@\x1c\xf5\xfa\x93n$OL\x8e\t\x15\x11\x04\'Bq\x8f\xe0k\xaf+\xae\x96W\xf7\x99%&\xf2=e2\xa9$\xa5\xe3\x9a/.\xeb\xa1\xd8h\xb9\x08\xc1\x8aP\xf4"\xf8]\xed\x1d\x8eK\xc7\xebe+#7\xb8\x1f/\x89\x0b\xed\x8cN\x1b\xd0\':T\xc2 h\x11\x8a\xfb\xf0\x9c\xdf\xebt\xdc\xa2\x1d\x13\x9c\x92\xb35#4\xe1r\x85R)\x11!\x88\x11\x8a\x7f\xc6s\x1eW\xfdQfD\xe3\x99\xe7\x1e\x88\x96I\x18\x11!\x08f\x84\xe2\x7f\x138g\xfd\xd7\xe5\xe1\xe3\x06G\xc8\x19\x04=B\xf1\x03\x04\xce\xdd\xe1\x13)C\xa4\x0c\x82\x1f\xa1\xf8\xb5\xfbo\x05f|\\Z\x89\t\xc7\x00\x00\x00\x00IEND\xaeB`\x82'
    create_tmp_png()            #tao tmp cho de seek
    fake_license()              #fake
    garenate_configfile()       #write ra config.file trong path
    # real_license()            #test coi dich lai dc k 
    
    hashDYS = hashfile(path+ '\\Dynasty.exe')
    # print(hashDYS)    #34aa6d94b013b5edbdbc54017c6e1f8999fefee8f9b07014b263334418d25842
    hashPNG = b'697077a7119cfd1c4e1c0ec5f1d5dc3a1725f1f098dda291bbba230fc8d7adaa'
    data = bytes(hashDYS,'utf8') + hashPNG
    # print('hash Dynasty + hash PNG :',data)
    # print(len(data))
    Arandom = ''.join(random.choice(string.ascii_letters) for i in range(10))
    PwAr= create_password_encrypt(Arandom)
    # print('len PwAr: ',len(PwAr))
    cryptoPwAr =  encrypt_input(PwAr,b'9YJa0qTRWbO2bmfFP_8hNy_ecPVe5dn3XZz_kNCe1R4=')
    cryptoDATA =  encrypt_input(data,PwAr)
    # print('len cryptoPWAR', len(cryptoPwAr))
    license = cryptoDATA + cryptoPwAr
    with open (path + '\\KEYGEN.txt','wb+') as file :
        file.write(license)
        # print(license)
    pid = os.getpid()
    call(r'taskkill /pid %s /f' % pid)

