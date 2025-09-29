# PinPong
hierbei geht es darum eine Serirelle Verbindung zwischen den beiden Geräten zu machen
```
# Test der seriellen Kommunikation mit dem ESP32
# Einfacher Ping-Pong Test
# Tress Constantin September 2025

import serial
import time

esp = serial.Serial(
    port="/dev/cu.usbserial-0001", baudrate=115200, timeout=1
)  # COM-Port anpassen
time.sleep(2)  # ESP32 braucht etwas Zeit zum Starten

esp.write(b"Ping\n")
print("Befehl gesendet: Ping")
antwort = esp.readline().decode().strip()
print("Antwort vom ESP32:", antwort)
```

```
/*
  SerialTestESP.ino - Einfacher ESP32 Code für serielle Kommunikation mit dem PC
  Empfängt "Ping" und antwortet mit "Pong"
  Tress Constantin September 2025
*/

#include <FVS.h>

void setup()
{
    Serial.begin(115200); // Serielle Verbindung starten
    Tft.begin();          // TFT Initialisieren
    while (!Serial)
        ; // Warten, bis die Verbindung steht
    Tft.println("ESP32 bereit");
}

void loop()
{
    if (Serial.available())
    {
        String eingabe = Serial.readStringUntil('\n'); // Bis zum Zeilenumbruch lesen
        eingabe.trim();                                // Leerzeichen entfernen

        // Überprüfen, ob der Befehl "Ping" empfangen wurde

        Tft.println(eingabe + " empfangen");

        if (eingabe == "Ping")
        {
            Serial.println("Pong");
            Tft.println("Pong gesendet");
        }
        else
        {
            Serial.println("Unbekannter Befehl");
            Tft.println("Unbekannter Befehl empfangen");
        }
    }
}

```



Code bekommen:
```
geisleje@c055pc08:~/FvSBS/3.lehrjahr/labor/pingpong$ python3 pong.py 
Befehl gesendet: Ping
Antwort vom ESP32: Pong
```
