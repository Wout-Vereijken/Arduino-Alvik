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
  if center < 40 and left < 40 and cleft < 40 and cright < 40 and right < 40 :
    alvik.set_wheels_speed(20, -20)
  else:
      alvik.set_wheels_speed(20, 20)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)