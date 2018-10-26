import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
counter = 10
while counter > 0:
    GPIO.output(19,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    counter = counter - 1
