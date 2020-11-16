import time
import threading
from os import path

import Camera
import Sender

def init():
    cam = Camera.Camera()
    startTimer(cam)
    cam.startRecording()

def startTimer(cam):
    print("Timer's activating")
    originImg, finalImg = cam.captureFrame()
    if not originImg is None:
        count = cam.detectPeople(originImg)
        Sender.postToServer(count, finalImg)

    threading.Timer(5, startTimer, args=(cam, )).start()


if __name__ == '__main__':
    init()
