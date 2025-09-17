from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

c1 = 0
c2 = 0
c3 = 0
c4 = 0

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
  global c1, c2, c3, c4   # ✅ allow modification of these globals
  
  delay(1000)
  get_color = alvik.get_color_raw()

  if c1 >= 2 and c2 >= 2 and c3 >= 2 and c4 >= 2:
    print("Stop")
    alvik.set_wheels_speed(0, 0)
  else:
    is_color_1 = check_color(color_1, get_color, 0.19)
    is_color_2 = check_color(color_2, get_color, 0.10)
    is_color_3 = check_color(color_3, get_color, 0.10)
    is_color_4 = check_color(color_4, get_color, 0.10)

    if is_color_1:
      print("It is Color 1!")
      c1 += 1
    elif is_color_2:
      print("It is Color 2!")
      c2 += 1
    elif is_color_3:
      print("It is Color 3!")
      c3 += 1
    elif is_color_4:
      print("It is Color 4!")
      c4 += 1
    else:
      print("Unknown Color")

    # keep moving until all colors are detected twice
    alvik.set_wheels_speed(50, 50)

  print(c1, c2, c3, c4)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)