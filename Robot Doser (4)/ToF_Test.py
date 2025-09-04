from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
  
def loop():
  left_tof, cleft_tof, center_tof, cright_tof, right_tof = alvik.get_distance()

  print("Left:", left_tof)
  print("Center Left:", cleft_tof)
  print("Center:", center_tof)
  print("Center Right:", cright_tof)
  print("Right:", right_tof)

  delay(1000)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)