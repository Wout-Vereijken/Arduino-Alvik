

from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)

  global blinked
  blinked = False

def loop():
  global blinked
  roll, pitch, yaw = alvik.get_orientation()
  print(pitch)
  delay(100)
  
  BASE_SPEED = 10
  MULTIPLIER = 2  # Change multiplier to adjust extra_rpm strength
  extra_rpm = abs(pitch) * MULTIPLIER
  adapted_speed = BASE_SPEED + extra_rpm

  # Robot will only move if slope is detected within 15 and -15 pitch
  if pitch < 15 and pitch > -15:
      # Incline slope
      if pitch < -1:
          alvik.set_wheels_speed(adapted_speed, adapted_speed)
      # Decline slope
      elif pitch > 1:
          alvik.set_wheels_speed(adapted_speed, adapted_speed)
      # No slope
      elif blinked == False:
        alvik.set_wheels_speed(0, 0)
        alvik.left_led.set_color(1, 1, 1)
        alvik.right_led.set_color(1, 1, 1)
        delay(500)
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        delay(250)
        alvik.left_led.set_color(1, 1, 1)
        alvik.right_led.set_color(1, 1, 1)
        delay(500)
        alvik.left_led.set_color(0, 0, 0)
        alvik.right_led.set_color(0, 0, 0)
        delay(250)
        blinked = True
        alvik.set_wheels_speed(20, 20)
  else:
      alvik.set_wheels_speed(20, 20)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)