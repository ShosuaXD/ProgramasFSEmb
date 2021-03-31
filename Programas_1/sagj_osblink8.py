# import modules
import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# loop 5 times
for i in range(5):
    
    # flash output pin 3
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    time.sleep(1)