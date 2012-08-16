#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import array
import os
import signal

### Functions definition

# Called on process interruption. Set all pins to "Input" default mode.
def endProcess(signalnum = None, handler = None):
    for gpioPinLed in gpioPinLedList:
        GPIO.setup(gpioPinLed, GPIO.IN)
    exit(0)

# Put pins to out mode, and switch off LED.
def switchOffLeds():
    for gpioPinLed in gpioPinLedList:
        GPIO.setup(gpioPinLed, GPIO.OUT)
        GPIO.output(gpioPinLed, GPIO.LOW)

 
### Main part

# Get current pid
pid = os.getpid()

# Save current pid for later use
try:
    fhandle = open('/var/run/raspiledchaser.pid', 'w')
except IOError:
    print ("Unable to write /var/run/raspiledchaser.pid")
    exit(1)
fhandle.write(str(pid))
fhandle.close()

gpioPinLedList = [7, 11, 12, 13, 15, 16, 18, 22]
sleeptime = 0.05

# Prepare handlers for process exit
signal.signal(signal.SIGTERM, endProcess)
signal.signal(signal.SIGINT, endProcess)

# Use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# Init output pins
switchOffLeds()

while True:

    # Alternatively light on LED
    loop = 0
    while loop < 8:
        time.sleep(sleeptime)
        if loop == 0:
            GPIO.output(gpioPinLedList[loop], GPIO.HIGH)
        else:
            GPIO.output(gpioPinLedList[loop], GPIO.HIGH)
            GPIO.output(gpioPinLedList[loop-1], GPIO.LOW)
        loop += 1

    loop = 7
    while loop > -1:
        time.sleep(sleeptime)
        if loop == 7:
            GPIO.output(gpioPinLedList[loop], GPIO.HIGH)
        else:
            GPIO.output(gpioPinLedList[loop], GPIO.HIGH)
            GPIO.output(gpioPinLedList[loop+1], GPIO.LOW)
        loop -= 1 
