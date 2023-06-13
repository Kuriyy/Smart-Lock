# 4AAME FI IoT Projekt Projekt 2023

Jede Themenstellung enthält mechanische, mikroelektronische und programmiertechnische Arbeitsabschnitte.

Bei ähnlichen Arbeitsabschnitten ist die Zusammenarbeit sinnvoll und gewünscht. Die Ausarbeitung und Dokumentation erfolgt jedoch stets für das eigene Thema!

Allgemeine Anmerkungen: Alle Arbeiten werden digital abgewickelt und im originalen Urformat abgegeben. Also _.sld_, _.xlsx, _.docx, _.py, _.drawio usw.

Jeder Schüler hält den aktuellen Dateibestand auf H: bereit. Auch bei zeitweiser Teamarbeit für ähnlichen Aufgaben!
Teilaufgaben:

| Number | Aufgabe                                                                                                                                                                                                                                           |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.     | Technische Dokumentation mit kurzer Funktionsbeschreibung; Abbildung; Anschlussbelegung; Schnittstellenbeschreibung; Softwarezugriff/programmierung; Arbeitsbereich; Kennlinien; Abmessungen; max. mechanische und elektrische Arbeitsbedingungen |
| 2.     | Beispielprogramm zur Demonstration der Arbeitsweise bzw. Funktion                                                                                                                                                                                 |
| 3.     | Entwurf, Dokumentation und Produktion einer passenden Montagevorrichtung                                                                                                                                                                          |
| 4.     | Montageanleitung                                                                                                                                                                                                                                  |
| 5.     | Verkabelungs-, Anschlussanleitung                                                                                                                                                                                                                 |
| 6.     | Gegenseitige Vorstellung in Form einer Kurzpräsentation als Videoclip                                                                                                                                                                             |
| 7.     | Programm zur Auswertung/Betätigung                                                                                                                                                                                                                |


# Smart-Lock

Ich verwende als digitalen Eingang ein RFID-Lesegerät. Über den digitalen Ausgang steuere ich LEDs, um den Status des elektronischen Schlosses anzuzeigen. Alle Ereignisse, wie das Öffnen und Schließen der Tür, werden in einer Datei gespeichert. Mit diesen Daten analysiere ich, wer zu welcher Zeit die Tür betritt oder verlässt.

RFID-Chips:
Die RFID-Chips werden den Personen zugeordnet, die Zugang zum Smart-Lock haben sollen. Jeder autorisierten Person wird ein eindeutiger RFID-Chip zugewiesen, der vom RFID-Lesegerät erkannt wird. Dies ermöglicht eine zuverlässige Identifikation und Gewährleistung der Zugangskontrolle.

## Peripherie
Die benötigte Peripherie für das System umfasst ein, [RFID Sensor](https://www.az-delivery.de/products/rfid-set), [RFID Chips](https://www.az-delivery.de/products/13-56mhz-transponder?variant=38522275218), Raspi, Knopf, LED's

## Do-To-List
- [x] Es soll mit einem RFID Sensor eine Tür geöffent(Statt einem Schloss sollen die LED's eingebaut werden) werden.
- [ ] Innerhalb der Tür ist ein Taster damit man die Tür von innen öffnen kann.
- [x] 2 LED's sollen anzeigen, ob die Tür offen oder geschlossen ist.
- [x] Es sollen in ein File gespeichert werden, welche Person wann die Tür geöffent hat.

## Quellen
+ [RFID-Reader RC522](https://edistechlab.com/rfid-reader-rc522-einfach-erklart/?v=fa868488740a): In diesem Artikel wird der RFID-Reader RC522 einfach und verständlich erklärt.
+ [Tutorial: Raspberry Pi RFID-RC522 Türöffner mit NFC](https://tutorials-raspberrypi.de/raspberry-pi-rfid-rc522-tueroeffner-nfc/): Auf dieser Website gibt es ein hilfreiches Tutorial, das erklärt, wie man den RFID-RC522 mit dem Raspberry Pi verwendet, um Türen zu öffnen und die NFC-Funktionalität zu nutzen.



## Verkabelung
| RC522 Pin  | RC522 Name | Raspberry Pi Pin  | Raspberry Pi Name |  
| ------------- | ------------- | ------------- | ------------- |
| 1  | VCC  | 1  | 3.3V  |
| 2  | RST  | 22  | GPIO 25  |
| 3  | GND  | 6  | GND  |
| 4  | IRQ  | -  | -  |
| 5  | MISO  | 21  | GPIO 9  |
| 6  | MOSI  | 19  | GPIO 10  |
| 7  | SCK  | 23  | GPIO 11  |
| 8  | NSS  | 24  | GPIO 8  |

| LED | Raspberry Pi (GPIO)  | Raspberry Pi Name |  
| ------------- | ------------- | ------------- |
| ROT  | 22 | GPIO 22 |
| GRÜN  | 17  | GPIO 17  |


![Verkabelung](https://tutorials-raspberrypi.de/wp-content/uploads/2016/04/Raspberry-Pi-RFID-RC522-NFC_Steckplatine.png)

Die LED's wurden dann noch von 22 und 17 zu GND gesetzt(kann man ihm Programm umändern).

## Programm

Dieses Programm ist ein Leseprogramm für RFID-Karten oder Tags. Es liest die Daten von RFID-Karten und speichert sie in einer CSV-Datei für die Türüberwachung. Es überprüft auch, ob die Karten autorisiert sind, und ermöglicht den Zugang basierend auf einer Liste von berechtigten IDs.

### Read.py
```python
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

        if text == "^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@":
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
```
Here is a simple flow chart:

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```


### Write.py
```python
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
```