"""
Navigation Proof Of Concept Code
    -Will trigger an LED light when power is needed
    -Will trigger LED lights to show where soemthing is detected
"""

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) #fixed dumb warning

#Inputs
PIN_POWER_WARNING = 26 #yellow
PIN_POWER_CRITICAL = 19 #Red
PIN_DETECTION = 13 #Blue

#Outputs
PIN_SHUTDOWN_DETECTION = 5


GPIO.setup(PIN_POWER_WARNING, GPIO.IN)
GPIO.setup(PIN_POWER_CRITICAL, GPIO.IN)
GPIO.setup(PIN_DETECTION, GPIO.IN)
GPIO.setup(PIN_SHUTDOWN_DETECTION, GPIO.OUT)

GPIO.output(PIN_SHUTDOWN_DETECTION, 0)

timeUp = 1

while(1):

    if(GPIO.input(PIN_POWER_WARNING) == 1):
        #print(GPIO.input(PIN_POWER_WARNING))
        print("Warning signal detected\n")

        if(timeUp ==1):
            print("Timer started")

        timeUp += 1
        print(timeUp)
        #print("Timer started")



        if(timeUp == 10):
            GPIO.output(PIN_SHUTDOWN_DETECTION, 1)
            print("Timer signal sent")
            timeUp = 1

        elif(timeUp > 10):
            timeUp = 1


    if(GPIO.input(PIN_POWER_CRITICAL) == 1):
        #print(GPIO.input(PIN_POWER_CRITICAL))
        print("Critical signal detected\n")

        #dont start timer - send robot up
        #check for detection off (for loop - if noting at end go up anyway)

    if(GPIO.input(PIN_POWER_WARNING) == 0 and GPIO.input(PIN_POWER_CRITICAL) == 0):
        GPIO.output(PIN_SHUTDOWN_DETECTION, 0)



    if(GPIO.input(PIN_DETECTION) == 1):
        print(GPIO.input(PIN_DETECTION))
        print("Detected Object\n")

    time.sleep(1)
