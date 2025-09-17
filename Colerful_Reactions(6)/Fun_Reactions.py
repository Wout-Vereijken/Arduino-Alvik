from arduino import *
from arduino_alvik import ArduinoAlvik
import color_functions  # Ohh la la, nice module import!

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

  # Save as many different colors as you like to unique variables
  global color_1
  print("Ready to scan Color 1")
  color_1 = save_color()

  global color_2
  print("Ready to scan Color 2")
  color_2 = save_color()

def loop():
  delay(1000)
  get_color = alvik.get_color_raw()

  is_color_1 = check_color(color_1, get_color, 0.05)
  is_color_2 = check_color(color_2, get_color, 0.05)

  if is_color_1:
    print("It is Color 1!")
  elif is_color_2:
    print("It is Color 2!")
  else:
    print("Unknown Color")

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)