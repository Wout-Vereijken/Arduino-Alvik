from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

def loop():
  alvik.set_wheels_speed(20, 20)
  delay(5000)
  alvik.set_wheels_speed(-20, -20)
  delay(5000)
  alvik.set_wheels_speed(0, 0)
  delay(10000)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)