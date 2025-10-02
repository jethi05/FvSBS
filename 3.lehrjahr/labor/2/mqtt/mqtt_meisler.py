#!/usr/bin/python3

import serial
import time
import random

# ersetut serial am Ende
import paho.mqtt.client as mqtt

# connecte den Clinet

def on_connect(client, userdata, flags, rc):
    client.subscribe("test/topic")
    client.subscribe("fvs/e3fi/meisler/switches") # Topic mit meinem Namen abonnieren



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
#client.publish("fvs/e3fi/meisler/switches", "10101") # Nachricht senden

# Blocking call that processes network traffic, dispatches callbacks
#client.loop_forever()

# Variable für Input
input_binary = str("Hallo")
while input_binary != "" and len(input_binary) == 5:
    input_binary = input("Gib eine 5-stellige Binärzahl an\n>> ")
    if len(input_binary) == 5:
        client.publish("fvs/e3fi/meisler/switches", input_binary)
    else:
        print("Der Schtring muss 5 Zeichen sein du Opfer")
