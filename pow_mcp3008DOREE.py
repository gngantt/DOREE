# DOREE - Gabby Gantt, Jacob Lebruex, Janine Thomas
#
# This file is test the MCP3008 and analyze its outputs with batteries

# import constDOREE
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

# print ref voltage of mcp object
#print('MCP Reference Voltage: ', mcp.reference_voltage)

# uncomment these if running after boot up then comment again
# this is the chip select. needs to be set high then low for device
# communication
board.D22.value(1)
board.D22.value(0)

#while True:
    # current val of battery
    # battery_lvl = chan0.value

    # print('Battery level: ' + battery_lvl + '.')
    print('Raw ADC Value: ', chan0.value)
    print('ADC Voltage: ', chan0.voltage, 'V')
    print(' ')
    
    time.sleep(1)
