#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
# Author: Santillan Garcia Josue
# Codigo modificado de blink.py

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Initializes virtual board (comment out for hardware deploy)
import virtualboard
# importamos sleep
from time import sleep

# Disable warnings
# GPIO.setwarnings(False)
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up pin no. 32 as output and default it to low
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
# configuracion de los pines a utilizar
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
# Inicializacion del array de los pines
pines = [32, 26, 24, 22, 18, 16, 12, 10]
i = 0 # Indice para seleccionar un pin
direccionIzquierda = True # Condicion para evaluar la direccion de los leds

while True:
    sleep(0.5) # Esperamos 500 ms
    GPIO.output(pines[i], GPIO.HIGH) # Asignamos un 1 logico en el pin segun el valor del indice
    sleep(0.5) # Esperamos otros 500 ms
    GPIO.output(pines[i], GPIO.LOW) # Asignamos un 0 logico en el pin segun el valor del indice
    # Condicion para evaluar si el indice esta en los limites del arreglo de pines
    if i >= 7:
        direccionIzquierda = False
    elif i <= 0:
        direccionIzquierda = True
    # Condicion para evaluar si el conteo del indice debe ser positivo o negativo
    if direccionIzquierda:
        i += 1
    else:
        i -= 1
        
