import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

# Funktion, um das Lesen von Tags zu beenden
def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C erkannt. Das Lesen wird beendet")
    continue_reading = False
    GPIO.cleanup()

# Initialisierung des RFID-Readers
MIFAREReader = MFRC522.MFRC522()

# Schleife zum kontinuierlichen Lesen von Tags
print("Halte ein RFID-Tag in die Nähe des Readers...")
print("Das Lesen wird bei Drücken von Ctrl+C beendet")

# Interrupt-Handler registrieren, um das Lesen zu beenden
signal.signal(signal.SIGINT, end_read)

while continue_reading:
    # Versuche, ein Tag zu lesen
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Wenn ein Tag gefunden wurde
    if status == MIFAREReader.MI_OK:
        print("Tag gefunden")

    # UID des Tags lesen
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # Wenn UID gelesen wurde
    if status == MIFAREReader.MI_OK:
        # UID in einen String konvertieren
        uid_string = "".join([str(i) for i in uid])
        print("UID des Tags: " + uid_string)

