from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def save_color():
  print("Place Alvik on a color.")
  print("Push the OK checkmark button on Alvik to read color.")
  alvik.left_led.set_color(1, 1, 1)
  alvik.right_led.set_color(1, 1, 1)
  button_ok = alvik.get_touch_ok()

  while not button_ok:
    button_ok = alvik.get_touch_ok()
    delay(100)
    if button_ok:
      r, g, b = alvik.get_color_raw()
      color = (r, g, b)
      alvik.left_led.set_color(0, 0, 0)
      alvik.right_led.set_color(0, 0, 0)
      print("R, G, B readout saved!")
      print(color)
      delay(500)
      return color

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

  global color_3
  print("Ready to scan Color 3")
  color_3 = save_color()
  
  global color_4
  print("Ready to scan Color 4")
  color_4 = save_color()

  
def loop():
  print("Results:", color_1, color_2, color_3, color_4)
  delay(15000)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)