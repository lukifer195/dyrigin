#!/usr/bin/python
# -*- coding:utf-8 -*-

import cv2
import numpy as np
from subprocess import Popen


class imagesearch():
    '''imagesearch('screen.png', 'template.png', threahold= float , showpos=False)
                threadhold từ 0-1
                showpos=TRue trả về list vị trí x.y
                exam: [(32,425),(43,443),...]

            .find(showpos= bool) là func trả về kết quả '''

    def __init__(self, pathscreencap, imagesearch, threshhold=0.8, showpos=False):
        self.pathscreencap = pathscreencap
        self.imagesearch = imagesearch
        self.threshhold = threshhold
        self.showpos = showpos

    def find(self, showpos=False):
        """ 
            trả về int lần bắt dc ảnh\n
            showpos=True trả về tuple vị trí ảnh bắt dc [(44,234),...]
        """
        # Popen('adb shell mount -o rw,remount /system',shell=True)
        # Popen('adb shell mount -o rw,remount /mnt/shared/App/',shell = True)
        try:
            rgb = cv2.imread(self.pathscreencap)
            grayimg = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
            # viewgray = cv2.imshow('dddd',grayimg)
            # cv2.waitKey(10000)
            imagesearch = cv2.imread(self.imagesearch, 0)

            res = cv2.matchTemplate(grayimg, imagesearch, cv2.TM_CCOEFF_NORMED)
            threshhold = self.threshhold
            loc = np.where(res >= threshhold)
            countmatch = 0
            if showpos == False:
                for pt in zip(*loc):
                    pt != None
                    countmatch += 1
                if showpos == False:
                    return countmatch
            elif showpos == True:
                listpt = []
                for pt in zip(*loc):
                    listpt.append(pt)
                return listpt
        except cv2.error:
            raise
# imp=  imagesearch(r'E:/PyProjec/Pydctq/scr/nor.png',r'E:/PyProject/Pydctq/scr/temp.png'
#                         ,threshhold = 0.5, showpos=True)
# print(imp.find(False))
