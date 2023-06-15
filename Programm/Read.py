#!/usr/bin/python3
#coding utf-8
#Robert Pressl
#V1

# Importiere erforderliche Module
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import datetime
import Passwort

# Initialisiere das GPIO-Modul
GPIO.setmode(GPIO.BCM)

# Konfiguriere den Ausgangspin 22 als Ausgang und setze ihn auf HIGH
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)

# Erstelle einen Dateinamen mit dem aktuellen Datum
filename = datetime.datetime.now().strftime("%d_%m_%Y")

# Erzeuge ein SimpleMFRC522-Objekt für die RFID-Kommunikation
reader = SimpleMFRC522()

try:
    # Öffne die Datei und schreibe die Kopfzeilen
    with open("Door_surveillance_" + filename + ".cvs", "a") as file:
        file.write("|------------|------------------------------------------------|-------------------|-------------|\n")
        file.write("|     ID     |                     NAME                       |        TIME       |  AUTHORITY  |\n")
        file.write("|------------|------------------------------------------------|-------------------|-------------|\n")

    while True:
        # Initialisiere die GPIO-Pins 17 und 22 als Ausgänge
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)

        # Lese die ID und den Text vom RFID-Lesegerät
        id, text = reader.read()

        if text == "":
            text = "0" * 48

        # Aktuelle Zeitstempel erstellen
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y %X")

        # Drucke die ID, den Text und den Zeitstempel
        print(str(id) + " " + str(text) + " " + str(timestamp))

        # Überprüfe, ob die ID in der Liste der berechtigten IDs enthalten ist
        if id in Passwort.Liste_Berechtigung:
            # Öffne die Datei und schreibe die Daten der autorisierten Person
            with open("Door_surveillance_" + filename + ".cvs", "a") as file:
                file.write("|"+str(id) + "|" + str(text) + "|" + str(timestamp) + "|" + "     yes     |" +  "\n")

            # Schalte den Ausgangspin 17 auf HIGH und den Ausgangspin 22 auf LOW
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)

            # Warte für 3 Sekunden
            time.sleep(3)

            # Schalte den Ausgangspin 17 auf LOW und den Ausgangspin 22 auf HIGH
            GPIO.output(17, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)

            # Bereinige die GPIO-Pins
            GPIO.cleanup()
        else:
            # Warte für 2 Sekunden
            time.sleep(2)

            # Öffne die Datei und schreibe die Daten der nicht autorisierten Person
            with open("Door_surveillance_" + filename + ".cvs", "a") as file:
                file.write("|"+str(id) + "|" + str(text) + "|" + str(timestamp) + "|" + "      no     |" +  "\n")

except KeyboardInterrupt:
    # Schalte den Ausgangspin 22 auf LOW und den Ausgangspin 17 auf LOW
    GPIO.output(22, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)

    # Bereinige die GPIO-Pins
    GPIO.cleanup()

    # Öffne die Datei und schreibe eine neue Zeile
    with open("Door_surveillance_" + filename + ".cvs", "a") as file1:
        file1.write("\n")