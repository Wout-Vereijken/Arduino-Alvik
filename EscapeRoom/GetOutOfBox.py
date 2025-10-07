from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
  
def loop():
  left, cleft, center, cright, right = alvik.get_distance()
  print(cleft, "|", center, "|", cright )
  delay(100)

  if cleft < 25 or center < 30 or cright < 25:
      alvik.set_wheels_speed(35, -35)   
  else:
      alvik.set_wheels_speed(20, 20)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)