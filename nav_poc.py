"""
Navigation Proof Of Concept Code
    -Will trigger an LED light when power is needed
    -Will trigger LED lights to show where soemthing is detected
"""

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_POWER_WARNING = 26
PIN_POWER_CRITICAL = 19
#PIN_DETECTION = 1 

   
GPIO.setup(PIN_POWER_WARNING, GPIO.IN)
GPIO.setup(PIN_POWER_CRITICAL, GPIO.IN)
#GPIO.setup(PIN_DETECTION, GPIO.IN)


while(1):
  
   if(GPIO.input(PIN_POWER_WARNING) == 1):
        print(GPIO.input(PIN_POWER_WARNING))
        print("Warning\n")
        
        #start timer for 10 mins? if noting found from detection send signalto stop
    
   if(GPIO.input(PIN_POWER_CRITICAL) == 1):
        print(GPIO.input(PIN_POWER_CRITICAL))
        print("Critical\n")
        
        #dont start timer - send robot up
        #check for detection off (for loop - if noting at end go up anyway)
   
    
        time.sleep(1)

