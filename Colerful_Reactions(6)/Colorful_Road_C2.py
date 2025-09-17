from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

LastColor = 0

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

def check_color(color_name, color_read, tolerance):
  r_cn, g_cn, b_cn = color_name
  r_cr, g_cr, b_cr = color_read
  r_match, g_match, b_match = False, False, False

  if r_cr >= (r_cn - (r_cn * tolerance)) and r_cr <= (r_cn + (r_cn * tolerance)):
    r_match = True
  if g_cr >= (g_cn - (g_cn * tolerance)) and g_cr <= (g_cn + (g_cn * tolerance)):
    g_match = True
  if b_cr >= (b_cn - (b_cn * tolerance)) and b_cr <= (b_cn + (b_cn * tolerance)):
    b_match = True

  if r_match and g_match and b_match:
    return True
  else:
    return False

def setup():
  alvik.begin()
  delay(1000)
  
  # Save as many different colors as you like to unique variables
  global color_1
  print("Ready to scan Color 1")
  color_1 = save_color()   # ✅ call with module prefix

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
  global LastColor
  delay(1000)
  get_color = alvik.get_color_raw()

  is_color_1 = check_color(color_1, get_color, 0.19)
  is_color_2 = check_color(color_2, get_color, 0.10)
  is_color_3 = check_color(color_3, get_color, 0.10)
  is_color_4 = check_color(color_4, get_color, 0.10)

  if is_color_1 and LastColor != 1:
    print("It is Color 1!")
    alvik.set_wheels_speed(50, 50)
    LastColor = 1
  elif is_color_1:
    print("Again")
  elif is_color_2 and LastColor != 2:
    print("It is Color 2!")
    alvik.set_wheels_speed(30, 0)
    delay(3000)
    alvik.set_wheels_speed(50, 50)
    LastColor = 2
  elif is_color_2:
    print("Again")
  elif is_color_3 and LastColor != 3:
    print("It is Color 3!")
    alvik.set_wheels_speed(0, 30)
    delay(3000)
    alvik.set_wheels_speed(50, 50)
    LastColor = 3
  elif is_color_3:
    print("Again")
  elif is_color_4 and LastColor != 4:
    print("It is Color 4!")
    alvik.set_wheels_speed(0, 0)
    LastColor = 4
  elif is_color_4:
    print("Again")
  else:
    print("Unknown Color")
    LastColor = 0
    delay(500)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)