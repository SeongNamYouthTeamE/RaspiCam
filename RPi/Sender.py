import requests
import time
from os import path

def postToServer(count, filePath):
    sendURL = "http://3.138.86.213:8000/images/"

    with open(filePath, 'rb') as f1:
        files = [
            ('{}'.format(count), f1)
        ]
        try:
            requests.post(sendURL, files=files)
            print("post clear")
        except:
            print("post failed")
    # print("working test")
    # print(count)
