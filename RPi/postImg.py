import requests
import time
from os import path
from picamera import PiCamera

def takePicture():
    # could be delayed according to time for setting camera
    curTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    filePath = path.abspath("./images") + "/"+ curTime + ".jpg"

    camera = PiCamera()
    camera.start_preview()
    camera.capture(filePath)
    time.sleep(2)
    camera.stop_preview()
    postImage(filePath)

def postImage(filePath):
    sendURL = "http://IP:Port/web_dir/"

    with open(filePath, 'rb') as f1:
        files = [
            ('send', f1)
        ]
        try:
            requests.post(sendURL, files=files)
            print("post clear")
        except:
            print("post failed")


if __name__ == '__main__':
    takePicture()
