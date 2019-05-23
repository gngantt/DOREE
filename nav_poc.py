"""
Navigation Proof Of Concept Code
    -Will trigger an LED light when power is needed
    -Will trigger LED lights to show where soemthing is detected
"""

#!/usr/bin/python
import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BOARD)

    PIN_POWER = 1 #change when actually implemented
    PIN_DETECTION = 1 #change when actually implemented

    LED_POWER = 1 #change when actually implemented
    LED_LEFT_NAV = 1 #change when actually implemented
    LED_RIGHT_NAV = 1 #change when actually implemented

    GPIO.setup(PIN_POWER, GPIO.in)
    GPIO.setup(PIN_DETECTION, GPIO.in)


    #while GPIO.input(PIN_POWER)==1:


finally:
    GPIO.cleanup()
