import os , testttt 
import re
import sys
import time
import traceback
import subprocess
from subprocess import PIPE, Popen, call
import logging
# import win_unicode_console

# libs bảo mật
# from shutil import copyfile
# import hashlib

# libs để thêm phím tắt
# from pynput.keyboard import Key, Listener , Controller
# import pynput.keyboard as keyboard
# import threading

# import ui_MainUI                        
from Imagesearch import imagesearch  # import class Imagesearch
# from cryptolize import decrypt_input, decryptize_LICENSE_to_test, hashfile, real_license



# # Input console
# cTranThang2end  = int(input('Default count win (15)                         :'))
# cTimeWar        = int(input('Time maximum in a war (45s)                    :'))
# isShutdown      = int(input('Shutdown when reach Default count win          :'))
# isCloseNox      = int(input('Close Nox when reach Default count win or error:'))
# if cTranThang2end =="":
#     cTranThang2end = 4
# if cTimeWar     ==  "":
#     cTimeWar    = 45
# if isShutdown   ==  "":
#     isShutdown  = 0
# if isCloseNox   ==  "":
#     isCloseNox  = 0

# Set cứng
isLiettruyen = 0
cTranThang2end = 15
cTimeWar    = 45
isShutdown  = 1
isCloseNox  = 1

# Initing Value
cWait10min = 0          
choseIP = 0
cTranThang = 0
cCountError = 0
posAUTO = (0, 0)
path = os.path.dirname(sys.argv[0])
path_Scr = os.path.abspath('scr')
# path = 'E:/PyProject/Pydctq/'  # set cứng
# path_Scr = 'D:\\Desktop\\PyProject\\Pydctq/scr/'  # set cứng
# get_Paths()
# win_unicode_console.enable()
logging.info('<> Path Source:        ', path_Scr)
logging.info('<> Count Win:          ', cTranThang2end)
logging.info('<> Time out:           ', cTimeWar)
logging.info('<> Shutdown when ended:', bool(isShutdown))
logging.info('<> Close Nox when fail:', bool(isCloseNox))

#=========================================Logic Auto==============================================#

def connect():
    """connect :62001"""
    logging.info(' ______________Connecting_____________')
    Pconnect = Popen('adb connect 127.0.0.1:62001', shell=True, stdout=PIPE)
    Popen('adb root ', shell=True)
    stderrConn = Pconnect.communicate()
    # logging.info(stderrConn)
    try:
        for _ in range(3):
            if stderrConn[0] == b'already connected to 127.0.0.1:62001\r\n':
                logging.info('______________Connected_______________')
                checkauto()
                if isLiettruyen == 1:
                    lietruyen()
                else:
                    dbomLinh()
                    BoquaXacthuc()
            # else:
                # time.sleep(2)
                # call(r'adb start-server')
                # time.sleep(3)
                # call(r'adb start-server')
                # time.sleep(3)
                # connect()
    
    except cv2.error:
        global cCountError
        if cCountError < 3:
            logging.info(' image not found')
            cCountError += cCountError 
            logging.info(cCountError)
            get_Paths()
            connect()
    except Exception as e:
        logging.error('Lỗi kết nối: ', exec_info = True)
        print('Error: ' , e)
        
    finally:
        time.sleep(3)
        exit_auto()


def checkauto():
    screencap()
    imgAuto = imagesearch(path_Scr + '\\screencap.png',
                          path_Scr + '\\auto.png', 0.77 )
    if imgAuto.find(showpos=True):
        global posAUTO
        posAUTO = imgAuto.find(showpos=True)[0]
        logging.info('Auto in y.x: ', posAUTO)
    else:
        logging.info('openAuto')
        openAuto()


def BoquaXacthuc():
    """    
            click giao tranh và giao tranh
    """
    # printdb('def BoquaXacthuc')
    click_giaotranh()
    giaotranh()

def lietruyen():
    logging.info('isLiettruyen')
    if isLiettruyen == 1: 
        if click_image('chinhchien.png' , 0) == "notfound":
            logging.info('Choise lietruyen and try again')
            exit_auto()
        time.sleep(0.5)
        call(['adb', 'shell', 'input', 'tap', '700', '600'])        # click xuất chiến
        time.sleep(8)
        for _ in range(5):
            screencap()
            imgthuquan = imagesearch(   path_Scr + '\\screencap.png',
                                        path_Scr + '\\thuquan.png' ,    0.8)
            if imgthuquan.find() >= 1:
                click_danh()
                time.sleep(60)
                for _ in range(10):  
                    if click_image('hoithanh.png', 0) == "Ok":
                        time.sleep(10)
                        lietruyen()
                        break
                else:
                    time.sleep(6)
                break
        else:
            time.sleep(3)
def giaotranh():
    """ sleep 8s \n
        imgnext -> danh 
                //checkloivethanh
    """
    # printdb('def giaotranh')
    time.sleep(8)
    logging.info('def giao tranh')
    for x in range(6):
        screencap()
        # thấy next thì chuyển
        imgnext = imagesearch(path_Scr + '\\screencap.png',
                              path_Scr + '\\next.png', 0.8)
        if imgnext.find() >= 1:
            # printdb('mạnh')
            danh()
            break
    else:
        if x == 5:
            check_loi_vethanh()
        else:
            time.sleep(2)


def danh():
    """ imgsearch temp  ->   next\n
                        //   danh   ->  danhtiep
    """
    # printdb('def danh')
    imgmanh = imagesearch(path_Scr + '\\screencap.png',
                          path_Scr + '\\longden.png', 0.77)
    time.sleep(1)
    # mạnh bỏ qua
    if imgmanh.find() >= 1:
        click_next()
        logging.info('Next')
        giaotranh()
    else:
        click_danh()
        #######################lỗi mạng######################
        time.sleep(30)
        screencap()
        error = imagesearch(path_Scr + '\\screencap.png',
                            path_Scr + '\\error.png', 0.88)
        # printdb('check lỗi ')
        if error.find() >= 1:  # check lỗi mạng
            check_loi_vethanh()
        else:
            time.sleep(cTimeWar)  # 40s
            # Rutlui()                  #opt1 check khiên --end (rỉa 1 khiên)
            DanhTiep()                  # opt2 check nút hồi thành --end
            # click_rutlui()            #opt3 chờ cTimeWar --End (đánh theo time chỉ định)
        #####################################################


def DanhTiep():
    """ ->  check nút hồi thành / checkloivethanh
            //nếu k lỗi thì check mua lính , số trận out -> dbomLinh / end
            //nếu k mua lính và cTranThang max -> đánh tiếp
            //nếu k có nút hồi thành thì cưỡng chế rutlui -> checkhoithanh -> boquaxacthuc
    """
    # printdb('def danh tiep')
    global cTranThang
    for x in range(0, 1):
        screencap()
        imgDanhTiep = imagesearch(path_Scr + '\\screencap.png',
                                  path_Scr + '\\hoithanh.png', 0.88)
        error = imagesearch(path_Scr + '\\screencap.png',
                            path_Scr + '\\error.png', 0.88)
        if error.find() >= 1:  # check lỗi mạng
            check_loi_vethanh()
            break
        elif imgDanhTiep.find() >= 1:
            cTranThang += 1
            logging.info('==[] Win  ', cTranThang)
            if cTranThang >= cTranThang2end:
                Exit_NOX()
                exit_auto()
            elif cTranThang in [3,8,11,16]:  # Mua lính   cách  5 thằng
                logging.info('Count: ',cTranThang)
                # nút hồi thành
                call(['adb', 'shell', 'input', 'tap', '1100', '650'])
                time.sleep(8)
                CheckHoiThanh()
                dbomLinh()
                BoquaXacthuc()
                break
            else:  # đánh tiếp
                # time.sleep(5)
                logging.info('Continue')
                call(r'adb shell input tap 85 666')  # nút đánh tiếp
                time.sleep(0.5)
                call(['adb', 'shell', 'input', 'tap', '777', '450'])  # nút ok
                giaotranh()
                break
        else:
            time.sleep(2)
            logging.info('Wait ', x)
    else:
        cTranThang += 1
        logging.info('==[] Win  :', cTranThang)
        click_rutlui()
        time.sleep(5)
        if cTranThang >= cTranThang2end:
            Exit_NOX()
            exit_auto()
        else:
            logging.info('Continue')
            call(r'adb shell input tap 85 666')  # nút đánh tiếp
            time.sleep(0.5)
            call(['adb', 'shell', 'input', 'tap', '777', '450'])  # nút ok
            giaotranh()

def CheckHoiThanh():
    """ for check quansu -> break else checkloivethanh 
    """
    logging.info('check Hồi thành')
    for _ in range(10):
        screencap()
        quansu = imagesearch(path_Scr + '\\screencap.png',
                             path_Scr + '\\quansu.png', 0.88)
        if quansu.find() >= 1:
            break
        else:
            time.sleep(2)
            logging.info('Wait to come home')
    else:
        check_loi_vethanh()

# def Rutlui():       # check 1 khiên ->  CheckHoiThanh
#     global cTranThang
#     for x in range(1,20):
#         screencap()
#         imgshield = imagesearch(path_Scr+'\\screencap.png',path_Scr+'\\shield.png',0.88)
#         if imgshield.find() >=1 :
#             logging.info('~~~~~Xong Thằng thứ :',cTranThang)
#             click_rutlui()
#             time.sleep(8)
#             CheckHoiThanh()
#             BoquaXacthuc()
#         else:
#             time.sleep(2)
#             logging.info('chờ ăn dc khiên',x)


def check_loi_vethanh():
    logging.warning('Check lỗi về thành')
    """imgerror -> click trở về -> check hồi thành\n
        /-> imgquansu -> giao tranh\n
        /-> reset ccounterror -> wait10min
    """
    global cCountError
    cCountError = cCountError + 1
    if cCountError >= 20:
        logging.info('(o>>>>>> End by 20 count Error <<<<<<o)')
        Exit_NOX()
        exit_auto()
    else:  # check mất mạng
        screencap()
        error = imagesearch(path_Scr + '\\screencap.png',
                            path_Scr + '\\error.png', 0.88)
        if error.find() == True:  # check lỗi mạng
            call(['adb', 'shell', 'input', 'tap', '632', '444'])
            logging.warning('(o>>>>>> Count Error :  %s <<<<<<o)',cCountError)
            time.sleep(8)
            CheckHoiThanh()
            BoquaXacthuc()  # ***

        else:  # check lỗi dính giao diện
            call(['adb', 'shell', 'input', 'tap', '1250', '477'])
            screencap()
            quansu = imagesearch(path_Scr + '\\screencap.png',
                                 path_Scr + '\\quansu.png', 0.88)
            # giao tranh wait >=3 lần  ->  wait10min
            if quansu.find() >= 1:
                logging.info('(o>>>>>> Fail with something', cCountError, ' <<<<<<o)')
                click_giaotranh()
                ############################################## Giống bước giaotranh() ################
                time.sleep(8)
                for _ in range(5):
                    screencap()
                    imgnext = imagesearch(path_Scr + '\\screencap.png',
                                          path_Scr + '\\next.png', 0.88)
                    # thấy next thì tới đánh
                    if imgnext.find() >= 1:
                        # printdb('lỗi dính và def đánh check mạnh yếu')
                        danh()
                        break
                    else:
                        time.sleep(2)
                        logging.info('Wait')
                else:
                    global cWait10min
                    cCountError = 0
                    logging.info('***reset count Error')
                    if cWait10min <= 3:
                        cWait10min = cWait10min + 1
                        Wait_10min()                # chết tướng
                    else:
                        Exit_NOX()
                        exit_auto()


###============================================ Tọa độ ==============================================###

def click_giaotranh():
    logging.info('go War')
    call(r'adb shell input tap 300 680')
    call(r'adb shell input tap 60 660')
    call(['adb', 'shell', 'input', 'tap', '170', '540'])
    call(['adb', 'shell', 'input', 'tap', '900', '500'])
    time.sleep(0.5)
    # checkfulltuong()
    call(['adb', 'shell', 'input', 'tap', '850', '470'])  # bỏ thời gian khiên
    time.sleep(0.5)
    call(['adb', 'shell', 'input', 'tap', '650', '600'])


def click_next():
    call(['adb', 'shell', 'input', 'tap', '1000', '500'])


def click_rutlui():
    logging.info('Come Home')
    call(['adb', 'shell', 'input', 'tap', '150', '500'])
    call(['adb', 'shell', 'input', 'tap', '800', '450'])
    # time.sleep(5)
    # call(['adb', 'shell', 'input', 'tap', '1100', '650'])


def click_danh():
    logging.info('Auto fight')
    logging.debug('#posAUTO: ' ,  ' '.join(str(x) for x in posAUTO[::-1]))
    call('adb shell input tap ' + ' '.join(str(x) for x in posAUTO[::-1]))
    
###======================================== funtion =============================================###


def exit_auto():
    """exit AUTO by pid
    """
    # def_trackback()
    pid = os.getpid()
    logging.debug('Pid auto :' , pid)
    call(r'taskkill /pid %s /f' % pid)


def Exit_NOX():
    """Exit NOX by taskkill
    """
    logging.info('o>>> Close Nox after 10s <<<o')
    if isShutdown == 1:
        logging.info('Shutdown PC')
        time.sleep(10)
        call(['shutdown', '/f', '/s', '/t', '100'])
    logging.info('Kill all Nox ')
    call(['taskkill', '/f', '/im', 'Nox.exe'])
    call(['taskkill', '/f', '/im', 'NoxVMHandle.exe'])
    call(['taskkill', '/f', '/im', 'nox_adb.exe'])
    call(['taskkill', '/f', '/im', 'NoxVMSVC.exe'])


def Wait_10min():
    logging.info(time.ctime(), ': Pause 10min ')
    time.sleep(600)
    check_loi_vethanh()

def def_trackback():
    """logging current time + trackback vào src/log.txt
    """
    with open(path_Scr + '\\log.txt', 'a' , encoding='utf8' ) as f:
        f.write('\n<<o>>' + str(time.ctime())
                + '<<o>>\n'+ traceback.format_exc()
                + '\n-->Error:' + str(cCountError) + '\tCount:' + str(cTranThang))

def dbomLinh():
    logging.info('(*)-------build TNS------(*)')
    click_image('//warhouse.png')
    time.sleep(0.5)
    click_image('//huanluyen.png')
    call(['adb', 'shell', 'input', 'tap', '1260', '50'])
    call(['adb', 'shell', 'input', 'tap', '1260', '100'])
    time.sleep(18)
    call(['adb', 'shell', 'input', 'tap', '1250', '477'])
    call(['adb', 'shell', 'input', 'tap', '1260', '50'])
    call(['adb', 'shell', 'input', 'tap', '1260', '50'])


def get_Paths():
    """ get path từ OptionRE
        nếu có thì ghi đè biến k thì dùng mặc định
    """
    list_of_lines = []
    logging.info('Get paths in OptionRE.txt')
    with open(path_Scr + '\\OptionRE.txt') as f:
        for _ in range(10):
            line = f.readline().split('\n')
            line.remove('')
            list_of_lines.append(line)
        i = 0
        for _ in list_of_lines:
            strline = ''.join(list_of_lines[i])
            # logging.info(strline)
            i = i + 1
            if re.search('cTranThang2end', strline):
                kq = strline.replace('cTranThang2end: ', '')
                if kq != None:
                    global cTranThang2end
                    cTranThang2end = int(kq)
            elif re.search('cTimeWar', strline):
                kq = strline.replace('cTimeWar:\t', '')
                if kq != None:
                    global cTimeWar
                    cTimeWar = int(kq)
            elif re.search('isShutdown', strline):
                kq = strline.replace('isShutdown:\t', '')
                if kq != None:
                    global isShutdown
                    isShutdown = int(kq)
            elif re.search('isCloseNox', strline):
                kq = strline.replace('isCloseNox:\t', '')
                if kq != None:
                    global isCloseNox
                    isCloseNox = int(kq)


def screencap():
    """chụp ảnh nox qua cmd.pipe.stdout.read lưu vào Scr/screencap.png
    """
    logging.debug('- Chụp màn hình nox')
    pipe = Popen("adb shell screencap -p", stdout=PIPE, shell=True)
    image_bytes = pipe.stdout.read().replace(b'\r\r\n', b'\n')
    with open(path_Scr + '//screencap.png', 'wb') as file:
        file.write(image_bytes)


def click_image(image,  notfound = 'check_loi_vethanh'):
    """Find image in screen and click it and return "Ok"
    // else return "notfound" and do something
    exam:   
    click_image('warhouse.png')         
    click_image('warhouse.png' , 0) if not found image do nothing
    """
    logging.info('Tìm và click image : ',image)
    position = ()
    screencap()
    imgfind = imagesearch(path_Scr + '//screencap.png',
                          path_Scr + '//' + image, 0.77 )
    logging.debug('$position : ',position)
    try:
        position = imgfind.find(showpos=True)[0]
        if position != None:
            position_to_string = ' '.join(str(x) for x in position[::-1])
            # logging.info(position_to_string)
            call('adb shell input tap ' + position_to_string)
            return "Ok"
    except (IndexError,Exception):
        logging.error('Image not found' , exec_info = True)
        if notfound == 'check_loi_vethanh':
            check_loi_vethanh()
        elif notfound == 0:
            pass
        return "notfound"
    finally:
        del position    



def openAuto():
    call('adb shell input keyevent 3')
    time.sleep(2)
    screencap()
    imgiconAUTO = imagesearch(path_Scr + '//screencap.png',
                              path_Scr + '//autoicon2.png', 0.88)
    imgicondctq = imagesearch(path_Scr + '//screencap.png',
                              path_Scr + '//dctqicon.png', 0.88)
    posiconAuto = imgiconAUTO.find(showpos=True)[0]
    posiconDCTQ = imgicondctq.find(showpos=True)[0]
    for _ in range(3):
        if posiconAuto:
            posiconAutostr = ' '.join(str(x) for x in posiconAuto[::-1])
            posiconDCTQstr = ' '.join(str(x) for x in posiconDCTQ[::-1])
            call('adb shell input tap ' + posiconAutostr)
            logging.info('$ position AUTO in x.y: ', posiconAutostr)
            time.sleep(2)
            call('adb shell input keyevent 3')
            time.sleep(1)
            call('adb shell input tap ' + posiconDCTQstr)
            time.sleep(5)
            checkauto()
            break
        else:
            checkauto()
    else:
        logging.error('Auto icon notfound' , exec_info = True)
        raise Exception('Auto icon notfound')


if __name__ == '__main__':
    # screencap()
    import logging
    logging.basicConfig(    filename = "E:/logging.log" , level=logging.DEBUG, filemode='w+', 
                            format = (  '%(levelname)s:\t'
                                        '%(filename)s:'
                                        '%(funcName)s():'
                                        '%(lineno)d\t'
                                        '%(message)s'           ))

    connect()

    