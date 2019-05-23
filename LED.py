"""
Test code so I can see how LED's work on a Pi
"""
import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(FALSE)
GPIO.setup(18, GPIO.OUT)

print "LED on"

GPIO.output(18, GPIO.HIGH)
time.sleep(1)

Print "LED off"

GPIO.output(18, GPIO.LOW)
