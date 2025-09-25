# Test der seriellen Kommunikation mit dem ESP32
# Einfacher Ping-Pong Test
# Tress Constantin September 2025

import serial
import time

# der Port ist da, als was der ESP erkannt wird

esp = serial.Serial(
    port="/dev/ttyUSB0", baudrate=115200, timeout=1
)  # COM-Port anpassen
time.sleep(2)  # ESP32 braucht etwas Zeit zum Starten

esp.write(b"Ping\n")
print("Befehl gesendet: Ping")
antwort = esp.readline().decode().strip()
print("Antwort vom ESP32:", antwort)

