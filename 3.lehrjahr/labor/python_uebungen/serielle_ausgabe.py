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

esp.write(b"Daten \n")

while True:
    output = esp.readline().decode().strip()
    if output != "":
        esp.write(f"{output}\n".encode())
