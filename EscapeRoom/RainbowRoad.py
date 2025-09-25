from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

TurnedAround = False
LastColor = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0

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

  global color_1
  color_1 = 0
  
  global color_2
  color_2 = 0

  global color_3
  color_3 = 0

  global color_4
  color_4 = 0

def loop():
  global c1, c2, c3, c4, LastColor, TurnedAround, color_1, color_2, color_3, color_4   # Ã¢ÂÂ allow modification of these globals
  left, cleft, center, cright, right = alvik.get_distance()
  get_color = alvik.get_color_raw()

  is_color_1 = check_color(color_1, get_color, 0.20) if color_1 else False
  is_color_2 = check_color(color_2, get_color, 0.20) if color_2 else False
  is_color_3 = check_color(color_3, get_color, 0.20) if color_3 else False
  is_color_4 = check_color(color_4, get_color, 0.20) if color_4 else False
  
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
      
      Color1 = 1
      Color2 = 1
      Color3 = 1
      Blink_Color(Color1, Color2, Color3)
      
    elif is_color_2 and LastColor != 2:
      print("It is Color 2!")
      c2 += 1
      LastColor = 2

      Color1 = 21
      Color2 = 21
      Color3 = 21
      Blink_Color(Color1, Color2, Color3)
    
    elif is_color_3 and LastColor != 3:
      print("It is Color 3!")
      c3 += 1
      LastColor = 3

      Color1 = 42
      Color2 = 42
      Color3 = 42
      Blink_Color(Color1, Color2, Color3)
      
    elif is_color_4 and LastColor != 4:
      print("It is Color 4!")
      c4 += 1
      LastColor = 4

      Color1 = 63
      Color2 = 63
      Color3 = 63
      Blink_Color(Color1, Color2, Color3)
    
    if is_color_1 == False and is_color_2 == False and is_color_3 == False and is_color_4 == False:
      LastColor = 0;
      
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
    else:
      alvik.set_wheels_speed(50, 50)
    
  print(c1, c2, c3, c4)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)