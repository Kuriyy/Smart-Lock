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

```python
#!/usr/bin/python3
#coding utf-8
#Robert Pressl
#V1

# Importiere benötigte Bibliotheken
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import datetime
import Passwort
```

```python
# GPIO-Pins konfigurieren
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)
# Dateiname basierend auf dem aktuellen Datum und Uhrzeit erstellen
# RFID-Reader initialisieren
filename = datetime.datetime.now().strftime("%d_%m_%Y")
reader = SimpleMFRC522()
```

```python
try:
        # Datei öffnen und Tabellenkopf schreiben
        with open("Door_surveillance_" + filename + ".cvs", "a") as file:
                        file.write("|------------|------------------------------------------------|-------------------|-------------|\n")
                        file.write("|     ID     |                     NAME                       |        TIME       |  AUTHORITY  |\n")
                        file.write("|------------|------------------------------------------------|-------------------|-------------|\n")
```

```python
         # Endlosschleife, die die Türüberwachung durchführt
        while True:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(17, GPIO.OUT)
                GPIO.setup(22, GPIO.OUT)
```
