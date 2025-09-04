from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
  
def loop():
  left, cleft, center, cright, right = alvik.get_distance()
  print(left, "|", cleft, "|", center, "|", cright, "|", right )
  delay(100)

  # If any zone is True, an item must be in range
  if cleft < 20 or center < 20 or cright < 20 or left < 20 or right < 20:
      if(left > cleft):
        alvik.set_wheels_speed(0, 10)  # Item detected left, so turn left
      elif cleft < center:
          alvik.set_wheels_speed(5, 10)  # Item detected left, so turn left
      elif cright < center:
          alvik.set_wheels_speed(10, 5)  # Item detected right, so turn right
      elif right > cright:
        alvik.set_wheels_speed(10, 0)  # Item detected left, so turn left
      else:
          alvik.set_wheels_speed(10, 10)  # Item center, so stay straight
  else:
      alvik.set_wheels_speed(0, 0)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)