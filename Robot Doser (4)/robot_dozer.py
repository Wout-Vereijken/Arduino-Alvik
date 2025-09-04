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
  if cleft < 20 or center < 20 or cright < 20:
      if cleft < center:
          alvik.set_wheels_speed(5, 10)  # Item detected left, so turn left
      elif cright < center:
          alvik.set_wheels_speed(10, 5)  # Item detected right, so turn right
      else:
          alvik.set_wheels_speed(10, 10)  # Item center, so stay straight
  else:
      alvik.set_wheels_speed(0, 0)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)