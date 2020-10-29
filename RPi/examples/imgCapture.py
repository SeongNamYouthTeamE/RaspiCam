from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
# edit the file path
camera.capture('/home/pi/opencvTest/image.jpg')
camera.start_recording('/home/pi/opencvTest/video.mp4')
sleep(5)
camera.stop_recording()
camera.stop_preview()
