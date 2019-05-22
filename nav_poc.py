"""
Navigation Proof Of Concept Code
    -Will trigger an LED light when power is needed
    -Will trigger LED lights to show where soemthing is detected
"""

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BOARD)

finally:
    GPIO.cleanup()
"""
Power:
if (low power)
    start ascent

else
    keep moving


Detection:
    if (detected on left)
        turn on left led
    elif (detected on right)
        turn on right led
    else
        no led
"""
