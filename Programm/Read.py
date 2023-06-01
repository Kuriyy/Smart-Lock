#!/usr/bin/python3
#coding utf-8
#Robert Pressl
#V1

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import datetime


reader = SimpleMFRC522()
while True:
        try:
                id, text = reader.read()
                timestamp = datetime.datetime.now()
                print(str(id) + " " + str(text) + " " + str(timestamp))
        finally:
                time.sleep(2)
                GPIO.cleanup()
