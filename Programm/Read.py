#!/usr/bin/python3
#coding utf-8
#Robert Pressl
#V1

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)

reader = SimpleMFRC522()
while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        try:
                id, text = reader.read()
                timestamp = datetime.datetime.now()
                print(str(id) + " " + str(text) + " " + str(timestamp))

        finally:
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                time.sleep(4)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.cleanup()

