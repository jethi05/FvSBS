import time

import gpio as GPIO

GPIO.setup(14, GPIO.OUT)

while True:
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(14, GPIO.LOW)
    time.sleep(1.0)
