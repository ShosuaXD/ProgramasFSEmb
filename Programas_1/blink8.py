#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# #################################################
# Author: Santillan Garcia Josue
# Codigo modificado de blink.py
# ###############################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Initializes virtual board (comment out for hardware deploy)
import virtualboard

# Disable warnings
# GPIO.setwarnings(False)
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Set up pin no. 32 as output and default it to low
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
# Configuracion de los pines asociados con los leds
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

# Blink the led
while True: # Forever
    sleep(0.5) # Esperamos 500 ms
    GPIO.output(32, GPIO.HIGH) # Funcion que manda un 1 logico al pin 32
    GPIO.output(26, GPIO.HIGH) # Funcion que manda un 1 logico al pin 26
    GPIO.output(24, GPIO.HIGH) # Funcion que manda un 1 logico al pin 24
    GPIO.output(22, GPIO.HIGH) # Funcion que manda un 1 logico al pin 22
    GPIO.output(18, GPIO.HIGH) # Funcion que manda un 1 logico al pin 18
    GPIO.output(16, GPIO.HIGH) # Funcion que manda un 1 logico al pin 16
    GPIO.output(12, GPIO.HIGH) # Funcion que manda un 1 logico al pin 12
    GPIO.output(10, GPIO.HIGH) # Funcion que manda un 1 logico al pin 10
    sleep(0.5) # Esperamoss otros 500 ms
    GPIO.output(32, GPIO.LOW) # Funcion que manda un 0 logico al pin 32
    GPIO.output(26, GPIO.LOW) # Funcion que manda un 0 logico al pin 26
    GPIO.output(24, GPIO.LOW) # Funcion que manda un 0 logico al pin 24
    GPIO.output(22, GPIO.LOW) # Funcion que manda un 0 logico al pin 22
    GPIO.output(18, GPIO.LOW) # Funcion que manda un 0 logico al pin 18
    GPIO.output(16, GPIO.LOW) # Funcion que manda un 0 logico al pin 16
    GPIO.output(12, GPIO.LOW) # Funcion que manda un 0 logico al pin 12
    GPIO.output(10, GPIO.LOW) # Funcion que manda un 0 logico al pin 10