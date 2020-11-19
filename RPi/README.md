# Raspberry Pi

### Hardware
* Raspberry pi 3B+/Zero W, Raspbian Buster  
* PiCamera 5MP  
(If you want to use Zero W, you should use camera connector for Zero model)  
![Pi-Image](https://user-images.githubusercontent.com/48985445/99684708-1c7fe600-2ac5-11eb-98be-1dd26c42292c.png)  

> MAKE SURE YOU CONNECT THE CABLE RIGHT WAY!!

### Software
* OpenCV 4.4.0.44
* Python 3.7.3

### Installation
1. pip3 install virtualenv
2. virtualenv opencvEnv --python=python3.7.3
3. . opencvEnv/bin/activate
If you don't want to set a virtual environment, skip step 1~3
4. pip install opencv-contrib-python
5. pip install matplotlib

### Execution
```
python main.py
```

### TroubleShooting
* Camera doesn't work  
  * check raspi-config enable setting
  ```
  sudo raspi-config
  Interfaces > Camera > Enabled
  sudo reboot
  ```
  * check ribbon cable's connection  
    1. connect it right direction
    2. connect it tightly
    3. change the camera module
* Cannot import cv2
  * reinstall opencv library
