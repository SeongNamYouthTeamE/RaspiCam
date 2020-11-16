import numpy as np
import cv2
import time
from os import path
from picamera import PiCamera
import threading

class Camera():
    def __init__(self):
        print("Load Camera")
        self.originImg = None
        self.capturedImg = None

    def startRecording(self):
        print("Start recording")
        try:
            cap = cv2.VideoCapture(0)
            # cap.set(3,640)
            # cap.set(4,480)

            ret, origin = cap.read()
            print("read")
            origin = cv2.flip(origin, -1)
            origin = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
            origin = cv2.GaussianBlur(origin, (11, 11), 2, 2)
            res = 0.05 * origin
            res = res.astype(np.float64)
            fgbg = cv2.createBackgroundSubtractorMOG2(history=1, varThreshold=100,
                                                      detectShadows=True)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))
            print("before while")
            while(True):
                ret, frame = cap.read()
                self.originImg = frame

                fgmask = fgbg.apply(frame, None, 0.01)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                gray = cv2.GaussianBlur(gray, (11, 11), 2, 2)
                gray = gray.astype(np.float64)
                fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
                fgmask = fgmask.astype(np.float64)
                # error occurred
                # operands could not be broadcast together with shapes (480,640,3) (480,640) (480,640,3)
                res += (40 * fgmask + gray) * 0.01
                res_show = res / res.max()
                res_show = np.floor(res_show * 255)
                res_show = res_show.astype(np.uint8)
                res_show = cv2.applyColorMap(res_show, cv2.COLORMAP_JET)

                self.capturedImg= res_show
                # cv2.imwrite('frame.jpg', res_show)
                # cv2.imshow('hitmap', res_show)

        except Exception as e:
            print("Something Error:", e)


    def detectPeople(self,img):
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cascade = cv2.data.haarcascades + 'haarcascade_fullbody.xml'
        bodyCascade = cv2.CascadeClassifier(cascade)

        bodies = bodyCascade.detectMultiScale(grayImg)
        for (x,y,w,h) in bodies:
            center = (x + w//2, y + h//2)
            frame = cv2.ellipse(img, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
            faceROI = grayImg[y:y+h,x:x+w]
        return len(bodies)

    def captureFrame(self):
        curTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        filePath = path.abspath("./images") + "/"+ curTime + ".jpg"
        if not self.capturedImg is None:
            cv2.imwrite(filePath, self.capturedImg)
            return self.originImg, None
        return self.originImg, filePath
