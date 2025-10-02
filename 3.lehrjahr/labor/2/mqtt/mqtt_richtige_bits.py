# Test der seriellen Kommunikation mit dem ESP32
# Einfacher Ping-Pong Test
# Tress Constantin September 2025

import serial
import time
import random

# ersetut serial am Ende
import paho.mqtt.client as mqtt

# connecte den Clinet

def on_connect(client, userdata, flags, rc):
    client.subscribe("test/topic")
    client.subscribe("fvs/e3fi/geisler/switches") # Topic mit meinem Namen abonnieren



def on_message(clinet, userdata, msg):
    data = msg.payload.decode().strip()
    print(data)
    print(f"{msg.topic} {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client()

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to a broker (public test broker here)
client.connect("mqtt01.pn.steinbeis.schule", 1883,60) # Broker verbinden

# Publish a message
client.publish("fvs/e3fi/geisler/response", "Hallo Welt") # Nachricht senden

# Blocking call that processes network traffic, dispatches callbacks
client.loop_forever()

def create_random_digit() -> str:
    random_digit = str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1))
    print(random_digit)

