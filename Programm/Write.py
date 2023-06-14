#!/usr/bin/python3
#coding utf-8
#Robert Pressl
#V1

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# RFID-Leser initialisieren
reader = SimpleMFRC522()

try:
    text = input('New data:')  # Eingabeaufforderung für neue Daten
    print("Now place your tag to write")
    reader.write(text)  # RFID-Karte beschreiben
    print("Written")
finally:
    GPIO.cleanup()