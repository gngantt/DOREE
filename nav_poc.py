"""
Navigation Proof Of Concept Code
    -Will trigger an LED light when power is needed
    -Will trigger LED lights to show where soemthing is detected
"""

#!/usr/bin/python
import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BOARD)

    PIN_POWER = input("type 1 for high power and 0 for low power") #change when actually implemented
    PIN_DETECTION = 1 #change when actually implemented

    """
    LED_POWER = 1 #change when actually implemented
    LED_LEFT_NAV = 1 #change when actually implemented
    LED_RIGHT_NAV = 1 #change when actually implemented
    """

    GPIO.setup(PIN_POWER, GPIO.IN)
    GPIO.setup(PIN_DETECTION, GPIO.IN)

#power LED
    while GPIO.input(PIN_POWER)==1:
        GPIO.output(18, GPIO.HIGH) #change pin once inplemented
   # elif GPIO.input(PIN_POWER)==0:
    #    GPIO.output(18, GPIO.LOW) #change pin once inplemented

        """
    while GPIO.input(PIN_DETECTION)==1:
        GPIO.output(1, GPIO.HIGH) #change pin once inplemented
    else GPIO.input(PIN_DETECTION)==1:
        GPIO.output(1, GPIO.LOW) #change pin once inplemented
        """


finally:
    GPIO.cleanup()
