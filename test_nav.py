import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN)
GPIO.setup(19,GPIO.IN)

while(1):

    if(GPIO.input(26) == 1):
        print(GPIO.input(26))
        print("Warning \n")
        #wait = input()
     
    elif(GPIO.input(19) == 1):
        print(GPIO.input(19))
        print("Critical \n")
        #wait = input()
    
    time.sleep(1)
    