```
/*
  SerialComESP.ino - ESP32 Code für serielle Kommunikation mit PC
  Sendet Muster von 5 Schaltern an PC und empfängt Antwort
  Bei richtiger Antwort wird "WIN" angezeigt, sonst die Anzahl der Übereinstimmungen
  Tress Constantin September 2025
*/

#include <FVS.h>

#define S0 25
#define S1 26
#define S2 27
#define S3 32
#define S4 33
#define T0 34 // achtung Öffner Kontakt -> invertieren

#define BAUDRATE 115200

int switches[] = {S4, S3, S2, S1, S0}; // absteigend, um Bitfolge der Schalter zu drehen MSB <-> LSB, Alternativ FOR anpassen

void setup()
{
  Serial.begin(115200); // Serielle Verbindung starten
  Tft.begin();          // TFT Verbindung initialisieren

  while (!Serial) // Warte bis serielle Verbindung bereit ist
    ;
  Tft.println("ESP32 bereit");

  portMode(0, INPUT); // Alle Eingänge (Schalter und Taster) konfigurieren
}

void loop()
{
  // Schalterzustände an PC senden
  if (!digitalRead(T0))
  {
    while (!digitalRead(T0)) // warte solange T0 gedrückt bleibt
      ;
    Tft.clearDisplay();
    Tft.setCursorCharacter(1, 1);
    String switchPattern = ""; // String für das senden vorbereiten

    for (int i = 0; i < 5; i++) // absteigend, um Bitfolge der Schalter zu drehen MSB <-> LSB, Alternativ Array anpassen
    {
      switchPattern += digitalRead(switches[i]) == HIGH ? "1" : "0";

      /* Alternative Schreibweise:
        if (digitalRead(switches[i]))
            switchPattern += "1";
        else
            switchPattern += "0";
        */
    }
    Serial.println(switchPattern); // String absenden ln fügt automatisch "\n" hinzu
    // Alternativ (kein String + "\n" machen gibt Probleme)
    // Serial.print(switchPattern);
    // Serial.print("\n");

    Tft.println(switchPattern + " gesendet");
  }

  // Antwort vom PC empfangen
  if (Serial.available())
  {
    String response = Serial.readStringUntil('\n'); // einlesen und speichern der Strings
    response.trim();                                // Sicherstellen dass keine Leerzeichen oder \n am Anfang oder Ende sind

    if (response == "WIN")
    {
      Tft.println("Richtig!"); // Ausgabe gewonnen
    }
    else
    {
      Tft.print("Treffer: "); // Ausgabe Treffer
      Tft.print(response);
    }
  }

  delay(100); // Wartezeit für bessere Kommunikation
}
```
