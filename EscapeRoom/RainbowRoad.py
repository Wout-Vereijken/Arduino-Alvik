from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

TurnedAround = False
LastColor = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0

def save_color():
  r, g, b = alvik.get_color_raw()
  color = (r, g, b)
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

def Blink_Color(Color1, Color2, Color3):
  alvik.right_led.set_color(0,0,0)
  alvik.left_led.set_color(0,0,0)
  delay(250)
  alvik.right_led.set_color(Color1, Color2, Color3)
  alvik.left_led.set_color(Color1, Color2, Color3)

def setup():
  alvik.begin()
  delay(1000)

  global color_1, color_2, color_3, color_4
  global color_5, color_6, color_7, color_8

  color_1 = 0
  color_2 = 0
  color_3 = 0
  color_4 = 0
  color_5 = 0
  color_6 = 0
  color_7 = 0
  color_8 = 0

def loop():
  global c1, c2, c3, c4, c5, c6, c7, c8
  global LastColor, TurnedAround
  global color_1, color_2, color_3, color_4, color_5, color_6, color_7, color_8
  
  left, cleft, center, cright, right = alvik.get_distance()
  get_color = alvik.get_color_raw()

  is_color_1 = check_color(color_1, get_color, 0.20) if color_1 else False
  is_color_2 = check_color(color_2, get_color, 0.20) if color_2 else False
  is_color_3 = check_color(color_3, get_color, 0.20) if color_3 else False
  is_color_4 = check_color(color_4, get_color, 0.20) if color_4 else False
  is_color_5 = check_color(color_5, get_color, 0.20) if color_5 else False
  is_color_6 = check_color(color_6, get_color, 0.20) if color_6 else False
  is_color_7 = check_color(color_7, get_color, 0.20) if color_7 else False
  is_color_8 = check_color(color_8, get_color, 0.20) if color_8 else False
  
  if center < 5 and TurnedAround == False:
    alvik.set_wheels_speed(-50, -50)
    delay(1000)
    alvik.set_wheels_speed(30, -30)
    delay(2875)
    alvik.set_wheels_speed(-50, -50)
    delay(500)
    TurnedAround = True
  elif TurnedAround == False:
    if is_color_1 and LastColor != 1:
      print("It is Color 1!")
      c1 += 1
      LastColor = 1
      Blink_Color(1,1,1)
      
    elif is_color_2 and LastColor != 2:
      print("It is Color 2!")
      c2 += 1
      LastColor = 2
      Blink_Color(21,21,21)
    
    elif is_color_3 and LastColor != 3:
      print("It is Color 3!")
      c3 += 1
      LastColor = 3
      Blink_Color(42,42,42)
      
    elif is_color_4 and LastColor != 4:
      print("It is Color 4!")
      c4 += 1
      LastColor = 4
      Blink_Color(63,63,63)

    elif is_color_5 and LastColor != 5:
      print("It is Color 5!")
      c5 += 1
      LastColor = 5
      Blink_Color(84,84,84)

    elif is_color_6 and LastColor != 6:
      print("It is Color 6!")
      c6 += 1
      LastColor = 6
      Blink_Color(105,105,105)

    elif is_color_7 and LastColor != 7:
      print("It is Color 7!")
      c7 += 1
      LastColor = 7
      Blink_Color(126,126,126)

    elif is_color_8 and LastColor != 8:
      print("It is Color 8!")
      c8 += 1
      LastColor = 8
      Blink_Color(147,147,147)
    
    if not (is_color_1 or is_color_2 or is_color_3 or is_color_4 or is_color_5 or is_color_6 or is_color_7 or is_color_8):
      LastColor = 0
      
      if color_1 == 0: 
        delay(250)
        color_1 = save_color()
        print("Color 1!")
        
      elif color_2 == 0:
        delay(250)
        color_2 = save_color()
        print("Color 2!")
        
      elif color_3 == 0:
        delay(250)
        color_3 = save_color()
        print("Color 3!")
        
      elif color_4 == 0:
        delay(250)
        color_4 = save_color()
        print("Color 4!")
      
      elif color_5 == 0:
        delay(250)
        color_5 = save_color()
        print("Color 5!")
      
      elif color_6 == 0:
        delay(250)
        color_6 = save_color()
        print("Color 6!")
      
      elif color_7 == 0:
        delay(250)
        color_7 = save_color()
        print("Color 7!")
      
      elif color_8 == 0:
        delay(250)
        color_8 = save_color()
        print("Color 8!")
         
    alvik.set_wheels_speed(50, 50)
    
  else:
    if is_color_1 and c1 == 1:
      delay(500)
      alvik.set_wheels_speed(0, 0)
    elif is_color_2 and c2 == 1:
      delay(500)
      alvik.set_wheels_speed(0, 0)
    elif is_color_3 and c3 == 1:
      delay(500)
      alvik.set_wheels_speed(0, 0)
    elif is_color_4 and c4 == 1:
      delay(500)
      alvik.set_wheels_speed(0, 0)
    elif is_color_5 and c5 == 1:
      delay(500)
      alvik.set_wheels_speed(0, 0)
    elif is_color_6 and c6 == 1:
      delay(500)
      alvik.set_wheels_speed(0, 0)
    elif is_color_7 and c7 == 1:
      delay(500)
      alvik.set_wheels_speed(0, 0)
    elif is_color_8 and c8 == 1:
      delay(500)
      alvik.set_wheels_speed(0, 0)
    else:
      alvik.set_wheels_speed(50, 50)
    
  print(c1, c2, c3, c4, c5, c6, c7, c8)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)
