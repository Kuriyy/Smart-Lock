# Smart-Lock

Verwenden Sie die digitalen Eingänge, um einen Türsensor und eine Tastatur oder ein RFID-Lesegerät anzuschließen. Verwenden Sie die digitalen Ausgänge, um ein elektronisches Schloss zu steuern. Speichern Sie Ereignisse wie das Öffnen und Schließen der Tür oder das Entfernen von RFID-Karten in einer Datei. Verwenden Sie diese Daten, um zu analysieren, wer wann die Tür betritt oder verlässt.

Peripherie: [Planzeichnung](https://fritzing.org/), [RFID Sensor](https://www.az-delivery.de/products/rfid-set), [RFID Chips](https://www.az-delivery.de/products/13-56mhz-transponder?variant=38522275218), Raspi, Knopf, LED's

- [ ] Es soll mit einem RFID Sensor eine Tür geöffent(Statt einem Schloss sollen die LED's eingebaut werden) werden.
- [ ] Innerhalb der Tür ist ein Taster damit man die Tür von innen öffnen kann.
- [ ] 2 LED's sollen anzeigen, ob die Tür offen oder geschlossen ist.
- [ ] Es sollen in ein File gespeichert werden, welche Person wann die Tür geöffent hat.

Quellen:
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