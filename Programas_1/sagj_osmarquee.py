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

pines = [13, 11, 12, 10, 8, 7, 5, 3]
i = 0
direccionDerecha = True
continuePwm = True

while continuePwm:
  pwm = GPIO.PWM(pines[i],1)
  pwm.start(50)
  time.sleep(2)
  if i >= 7:
    direccionDerecha = False
  elif i <= 0:
    direccionDerecha = True
  
  if direccionDerecha:
    i += 1
  else:
    i -= 1

pwm.stop()
GPIO.cleanup()