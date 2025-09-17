from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

def loop():
  # Option 1 - Directly print the values returned by the object
  # print(alvik.get_color_raw())

  # Option 2 - Assign values to a variable and print
  # colors = alvik.get_color_raw()
  # print(colors)

  # Option 3 - Unpack values and assign them to unique variables
  r, g, b = alvik.get_color_raw()
  # Then, print extracted values separately or together
  print(r)
  print(g)
  print(b)
  print(r, g, b)

  delay(100)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)