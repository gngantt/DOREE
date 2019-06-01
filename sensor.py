import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

x = 0

camera = PiCamera()
camera.rotation = 180

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

for i in range(0,1000):
    x+=1

    if (GPIO.input(4) == 1):
        print(GPIO.input(4))
        camera.capture("/home/pi/Desktop/" + str(x) + ".jpg")
        
        
    elif(GPIO.input(4) == 0):
        print(GPIO.input(4))
