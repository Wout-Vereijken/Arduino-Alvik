from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
  global driveback
  driveback = True

def loop():
  global driveback
  left, cleft, center, cright, right = alvik.get_distance()
  print(center)
  delay(100)

  if center < 30:
      alvik.set_wheels_speed(35, -35) 
      driveback = True
  else:
      if driveback:
          driveback = False
          alvik.set_wheels_speed(35, -35)
          delay(50)
      alvik.set_wheels_speed(100, 100)
      delay(250)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)