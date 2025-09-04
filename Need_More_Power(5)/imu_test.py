from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
  
def loop():
  roll, pitch, yaw = alvik.get_orientation()
  # Uncomment next line for rounded readout values
  # roll, pitch, yaw = round(roll, 2), round(pitch, 2), round(yaw, 2)
  print(roll, "|", pitch, "|", yaw)
  delay(500)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)