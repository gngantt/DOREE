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



PIN_TRIGGER = 7
PIN_ECHO = 11
#sets pins to input or output
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)
"""

#GPIO.setmode(GPIO.BOARD)

#initiates GPIO pins on Pi
PIN_TRIGGER = 7
PIN_ECHO = 11

#sets pins to input or output
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)

def acoustic():
    try:
            #print ("Waiting for sensor to settle")

            #time.sleep(2)

            #print ("Calculationg distance")

            GPIO.output(PIN_TRIGGER, GPIO.HIGH)

            time.sleep(0.00001)


            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
            while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            #print "Distance:", distance, "cm"
            return distance

    finally:
        GPIO.cleanup()

"""


warningAck = 0
timeUp = 0

while(1):

    if(GPIO.input(PIN_POWER_WARNING) == 1):
        #print(GPIO.input(PIN_POWER_WARNING))
        print("Warning signal detected\n")

        if(warningAck == 0):
            print("Timer started")
            warningAck = 1

        timeUp += 1
        if(timeUp <= 10):
            print(timeUp)
        #print("Timer started")


        if(timeUp == 10):
            GPIO.output(PIN_SHUTDOWN_DETECTION, 1)
            print("Timer signal sent")
            #timeUp = 1

    if(GPIO.input(PIN_POWER_CRITICAL) == 1):
        #print(GPIO.input(PIN_POWER_CRITICAL))
        print("Critical signal detected\n")

        #dont start timer - send robot up
        #check for detection off (for loop - if noting at end go up anyway)

    if(GPIO.input(PIN_POWER_WARNING) == 0 and GPIO.input(PIN_POWER_CRITICAL) == 0):
        GPIO.output(PIN_SHUTDOWN_DETECTION, 0)
        warningAck = 0
        timeUp = 0

    if(GPIO.input(PIN_DETECTION) == 1):
        print(GPIO.input(PIN_DETECTION))
        print("Detected life form\n")

    #x = acoustic()

    #if(x < 15):
        #print("Life form")






    try:
            #initiates GPIO pins on Pi


            print ("Waiting for sensor to settle")

            time.sleep(2)

            print ("Calculationg distance")

            GPIO.output(PIN_TRIGGER, GPIO.HIGH)

            time.sleep(0.00001)


            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
                print(pulse_start_time)

            print("1")
            while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()
            print("2")
            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            print "Distance:", distance, "cm"

    finally:
        GPIO.cleanup()








    time.sleep(1)
