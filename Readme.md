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

Ich verwende die digitalen Eingänge, um einen Türsensor und eine Tastatur oder ein RFID-Lesegerät anzuschließen. Mit den digitalen Ausgängen könnte ich ein elektronisches Schloss steuern(Es werden aber LED's verwendet). Ich speichere Ereignisse wie das Öffnen und Schließen der Tür oder das Entfernen von RFID-Karten in einer Datei. Mit diesen Daten kann ich nachschauen, wer wann die Tür betritt oder verlässt.

## Peripherie: 
[Planzeichnung](https://fritzing.org/), [RFID Sensor](https://www.az-delivery.de/products/rfid-set), [RFID Chips](https://www.az-delivery.de/products/13-56mhz-transponder?variant=38522275218), Raspi, Knopf, LED's

## Do-To-List:
- [x] Es soll mit einem RFID Sensor eine Tür geöffent(Statt einem Schloss sollen die LED's eingebaut werden) werden.
- [ ] Innerhalb der Tür ist ein Taster damit man die Tür von innen öffnen kann.
- [x] 2 LED's sollen anzeigen, ob die Tür offen oder geschlossen ist.
- [x] Es sollen in ein File gespeichert werden, welche Person wann die Tür geöffent hat.

## Quellen:
+ [RFID](https://edistechlab.com/rfid-reader-rc522-einfach-erklart/?v=fa868488740a)
+ [RFID](https://tutorials-raspberrypi.de/raspberry-pi-rfid-rc522-tueroeffner-nfc/)


Verkabelung:
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
