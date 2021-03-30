#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ################################
# Author: Santillan Garcia Josue
# Codigo modificado de bcd.py
# ################################
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Initializes virtual board (comment for hardware deploy)
import virtualboard

# Disable warnings
# GPIO.setwarnings(False)
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up pins 36, 38, 40 and 37 as output and default them to low
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
# Configuramos los pines correspondientes a los 4 leds
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

def bcd7(num):
	"""Converts num to a BCD representation"""
	GPIO.output(36, GPIO.HIGH if (num & 0x00000001) > 0 else GPIO.LOW )
	GPIO.output(38, GPIO.HIGH if (num & 0x00000002) > 0 else GPIO.LOW )
	GPIO.output(40, GPIO.HIGH if (num & 0x00000004) > 0 else GPIO.LOW )
	GPIO.output(37, GPIO.HIGH if (num & 0x00000008) > 0 else GPIO.LOW )

# Declaramos esta funcion para mostrar los ultimos cuatro leds, mostrando 
def numToBin(num):
    GPIO.output(18, GPIO.HIGH if (num & 0x00000001) > 0 else GPIO.LOW)
    GPIO.output(16, GPIO.HIGH if (num & 0x00000002) > 0 else GPIO.LOW)
    GPIO.output(12, GPIO.HIGH if (num & 0x00000004) > 0 else GPIO.LOW)
    GPIO.output(10, GPIO.HIGH if (num & 0x00000008) > 0 else GPIO.LOW)

flag = True

while flag:
    try:
        numero = int(input("Dame un numero del 0 al 15: ")) # pedimos un numero entre 0 y 15
        bcd7(numero) # Llamamos a la funcion que controla los pines correspondientes al controlador TTL 74LS47
        numToBin(numero) # Llamamos a la funcion que controla los ultimos 4 pines que muestran el numero a codigo binario
    except:
        flag = False

GPIO.cleanup()
