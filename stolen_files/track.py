from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
  # Drive forward
  alvik.set_wheels_speed(100,100)
  delay(6000)
  #stop
  alvik.set_wheels_speed(0,0)
  delay(500)
  # Turn right
  alvik.set_wheels_speed(100,-100)
  delay(780)
  #stop
  alvik.set_wheels_speed(0,0)
  delay(500)
  # Drive forward
  alvik.set_wheels_speed(100,100)
  delay(3750)
  #stop
  alvik.set_wheels_speed(0,0)
  delay(500)
  # Turn right
  alvik.set_wheels_speed(100,-100)
  delay(800)
  #stop
  alvik.set_wheels_speed(0,0)
  delay(500)
  # Drive forward
  alvik.set_wheels_speed(100,100)
  delay(3000)
  #turn constant right
  alvik.set_wheels_speed(100,25)
  delay(7750)
   #stop
  alvik.set_wheels_speed(0,0)
  delay(500)
  # Drive forward
  alvik.set_wheels_speed(100,100)
  delay(5000)

def loop():
  alvik.set_wheels_speed(0,0)
delay(100)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)