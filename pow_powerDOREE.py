# DOREE - Gabby Gantt, Jacob Lebruex, Janine Thomas
#
# This file is main file for DOREE to run her power method
#
# DOREE will ocnstantly ready thevoltage level of her battery. Once she has
# reached either of the desired battery levels, she will send a signal to
# navigation to either abort or resume the mission

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

# test variables until integration
test_warn = 0
test_ready = 0
warnsig = 0
readysig = 0

tol = 0.5
print('Raw ADC Value: ', chan0.value)
print('ADC Voltage: ', + str(chan0.voltage) + 'V')

while True:
    # current val of battery
    battery_lvl = chan0.value

    if ((chan0.value <= constDOREE.WARN) and (warnsig == 0)):
        print('Battery level: ' + battery_lvl + '. Warning level reached!')
        # figure out code to send signal to navigation
        # in the mean time test w test variables
        
        test_warn, test_ready = 1, 0
        warnsig, readysig = 1, 0
        
    elif ((chan0.value >= constDOREE.READY) and (readysig == 0)):
        print('Battery level: ' + battery_lvl + '. Ready level reached!')
        # figure out code to send signal to navigation
        # in the mean time test w variable test_warn

        test_warn, test_ready = 0, 1
        warnsig, readysig = 0, 1
        
    else:
        print('Battery level: ' + battery_lvl + '.')

    
