/*
  MQTTComESP.ino - ESP32 Code für MQTT Kommunikation
  Sendet Muster von 5 Schaltern an PC und empfängt Antwort
  Bei richtiger Antwort wird "WIN" angezeigt, sonst die Anzahl der Übereinstimmungen
  Tress Constantin September 2025
*/

#include <FVS.h>
#include <PubSubClient.h>

#define S0 25
#define S1 26
#define S2 27
#define S3 32
#define S4 33
#define T0 34

#define subscribeTopic "fvs/e3fi/geisler/response"
#define publishTopic "fvs/e3fi/geisler/switches"

const int switches[] = { 33, 32, 27, 26, 25 };  // MSB → LSB

WiFiClient espClient;            // WiFi Client für MQTT
PubSubClient client(espClient);  // MQTT Client

// Funktion für empfangene Nachrichten
void callback(char *topic, byte *payload, unsigned int length) {
  String response = "";
  for (int i = 0; i < length; i++) {
    response += (char)payload[i];
  }
  response.trim();  // Entfernt führende und nachfolgende Leerzeichen

  // Ausgabe der Nachricht auf dem Display
  if (response == "WIN") {
    Tft.println("Richtig!");
    Tft.println();
    Tft.println("neues Speil,");
    Tft.println("neues Glueck ;)");
  } else {
    Tft.print("Treffer: ");
    Tft.print(response);
  }
}

void setup() {
  // WiFi und Display initialisieren
  fvsWifi.wifiBegin();
  Tft.begin();
  Tft.println("Verbinde...");

  portMode(0, INPUT);  // alle Schalter auf Input

  // MQTT Client konfigurieren
  client.setServer(fvsWifi.mqttServer(), fvsWifi.mqttPort());
  client.setCallback(callback);

  // Mit dem MQTT Broker verbinden
  while (!client.connected()) {
    client.connect("ESP32Client");
    delay(500);
  }
  client.subscribe(subscribeTopic);

  Tft.clearDisplay();
  Tft.println("ESP32 bereit");
}

void loop() {
  // Verbindung aufbauen, wenn getrennt
  if (!client.connected()) {
    while (!client.connected()) {
      client.connect("ESP32Client");
      delay(500);
    }
    client.subscribe(subscribeTopic);  // Wieder abonnieren nach Reconnect
  }
  client.loop();  // MQTT Client verarbeiten

  if (digitalRead(T0) == LOW) {
    while (digitalRead(T0) == LOW)
      ;  // Warten bis losgelassen
    String switchPattern = "";
    for (int i = 0; i < 5; i++) {
      switchPattern += digitalRead(switches[i]) == HIGH ? "1" : "0";
    }

    client.publish(publishTopic, switchPattern.c_str());  // String in char array umwandeln
    Tft.clearDisplay();
    Tft.setCursorCharacter(1, 1);
    Tft.print("Gesendet: ");
    Tft.println(switchPattern);
    delay(500);
  }
}