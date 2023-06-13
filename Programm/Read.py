#!/usr/bin/python3
#coding utf-8
#Robert Pressl
#V1

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import datetime
import Passwort


GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)
filename = datetime.datetime.now().strftime("%d_%m_%Y")
reader = SimpleMFRC522()

try:
        with open("Door_surveillance_" + filename + ".cvs", "a") as file:
                        file.write("|------------|------------------------------------------------|-------------------|-------------|\n")
                        file.write("|     ID     |                     NAME                       |        TIME       |  AUTHORITY  |\n")
                        file.write("|------------|------------------------------------------------|-------------------|-------------|\n")

        while True:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(17, GPIO.OUT)
                GPIO.setup(22, GPIO.OUT)
                id, text = reader.read()
                if text == "^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@":
                        text = "0" * 48
                timestamp = datetime.datetime.now().strftime("%d.%m.%Y %X")
                print(str(id) + " " + str(text) + " " + str(timestamp))
                

                if id in Passwort.Liste_Berechtigung:
                        with open("Door_surveillance_" + filename + ".cvs", "a") as file:
                                file.write("|"+str(id) + "|" + str(text) + "|" + str(timestamp) + "|" + "     yes     |" +  "\n")
                        
                        GPIO.output(17, GPIO.HIGH)
                        GPIO.output(22, GPIO.LOW)
                        time.sleep(3)
                        GPIO.output(17, GPIO.LOW)
                        GPIO.output(22, GPIO.HIGH)
                        GPIO.cleanup()
                else:
                        time.sleep(2)
                        with open("Door_surveillance_" + filename + ".cvs", "a") as file:
                                file.write("|"+str(id) + "|" + str(text) + "|" + str(timestamp) + "|" + "      no     |" +  "\n")
except KeyboardInterrupt:
        GPIO.output(22, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        GPIO.cleanup()
        with open("Door_surveillance_" + filename + ".cvs", "a") as file1:
                file1.write("\n")

