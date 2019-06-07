import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.setup(5,GPIO.IN)

while(1):

    if(GPIO.input(23) == 1):
        print(GPIO.input(23))
        print("Crit \n")
        #wait = input()
     
    elif(GPIO.input(23) == 0):
        print(GPIO.input(23))
        print("Warn \n")
        #wait = input()
    
    time.sleep(1)
    