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

  # If any zone is True, an item must be in range
  if center < 20 :
    alvik.set_wheels_speed(20, 20)
  else:
      alvik.set_wheels_speed(20, -20)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)