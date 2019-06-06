'''
DOREE - Gabby Gantt, Jacob Lebreux, Janine Thomas

This file is main file for DOREE to run her power method

DOREE will constantly ready the voltage level of her battery. Once she has
reached either of the desired battery levels, she will send a signal to
navigation to either abort or resume the mission
'''

import constDOREE
import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the chip select
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)

# mcp cs. high -> low for device communication
board.D22.value(1)
board.D22.value(0)

# Set GPIO pin to output for ready/warning signal
board.D17.init(1) # warning level
board.D27.init(1) # critical level

# test variables until integration;
# signal has been sent or not, 1/0
critsig = 0
warnsig = 0
readysig = 0

tol = 0.5
print('Raw ADC Value: ', chan0.value)
print('ADC Voltage: ', chan0.voltage, 'V\n')

while True:
    # current val of battery
    battery = chan0.voltage

    if ((battery <= constDOREE.CRIT) and (critsig == 0)):
        print('Battery level: ', battery, 'V Critical level reached!')
        board.D17.value(0)
        board.D27.value(1)

        critsig, readysig = 1, 0
                
    # if battery has reached warning level and hasn't been acknowledged
    # send signal to navigation
    elif ((battery <= constDOREE.WARN) and (warnsig == 0)):
        print('Battery level: ', battery, 'V Warning level reached!')
        board.D17.value(1)
        board.D27.value(0)
        
        warnsig, readysig = 1, 0
        
    # if battery has reached ready level and hasn't been acknowledged
    # and was charging (not just booted up in a good state send signal
    # to navigation
    elif ((battery >= constDOREE.READY) and (readysig == 0)):
        print('Battery level: ', battery, 'V Ready level reached!')
        board.D17.value(0) # set pin low if ready level reached
        board.D27.value(0)
        critsig, warnsig, readysig = 0, 0, 1
        
    else:
        print('Battery level: ', battery, 'V')
    
    time.sleep(1)
