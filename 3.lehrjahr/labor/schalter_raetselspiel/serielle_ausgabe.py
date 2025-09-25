# Test der seriellen Kommunikation mit dem ESP32
# Einfacher Ping-Pong Test
# Tress Constantin September 2025

import serial
import time
import random

# der Port ist da, als was der ESP erkannt wird

esp = serial.Serial(
    port="/dev/ttyUSB0", baudrate=115200, timeout=1
)  # COM-Port anpassen
time.sleep(2)  # ESP32 braucht etwas Zeit zum Starten

random_digit = str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1))
print(random_digit)

esp.write(f"Start game\n".encode())
while True:
    output = esp.readline().decode().strip()
    if output != "":
        if output == random_digit:
            esp.write(b"WIN\n")
            break
        else:
            esp.write(f"{output} FALSCH".encode())
