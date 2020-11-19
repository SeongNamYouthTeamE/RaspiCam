# Raspberry Pi

### Hardware
* Raspberry pi 3B+/Zero W, Raspbian Buster
* PiCamera 5MP

![Pi-image](https://user-images.githubusercontent.com/48985445/99681625-af1e8600-2ac1-11eb-9650-280216b759f0.jpg)


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
> python main.py
