from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

SPEED = 30  # Base speed

def setup():
  alvik.begin()
  delay(1000)

def loop():
  # Get distance readings from all sensors
  left, cleft, center, cright, right = alvik.get_distance()
  print(f"Left: {left}, CLeft: {cleft}, Center: {center}, CRight: {cright}, Right: {right}")
  delay(10)

  # Forward/Backward logic based on the center sensor to follow the hand
  if center <= 12:  
    forward_speed = SPEED   # Hand is close, move forward quickly
  elif center <= 30 and center > 18:
    forward_speed = SPEED // 2   # Hand is at a medium distance, move forward slowly
  else:
    forward_speed = 0       # Hand is far away or out of range, stop

  # Turning logic based on left and right sensors
  if left < cright:  # Hand is closer to the left side
    left_speed = forward_speed * 0.5  # Turn left by slowing down the left wheel
    right_speed = forward_speed       # Right wheel keeps full speed
  elif cright < left:  # Hand is closer to the right side
    left_speed = forward_speed        # Left wheel keeps full speed
    right_speed = forward_speed * 0.5  # Turn right by slowing down the right wheel
  else:
    # Move straight if the hand is more or less centered
    left_speed = forward_speed
    right_speed = forward_speed

  # Set wheel speeds
  alvik.set_wheels_speed(left_speed, right_speed)

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)
