from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

# PID and Speed constants
KP = 40
KI = 1
KD = 0.05
BASE_SPEED = 40

# Initialize key variables
error = 0
integral = 0
last_error = 0

# Function to determine positional error from the line
def get_position_error():
  ir_left, ir_center, ir_right = alvik.get_line_sensors()
  total = ir_left + ir_center + ir_right

  if total == 0:  # Avoid division by zero if sensors don't detect anything
    return 0

  # Calculate the error based on sensor positions
  error = ((ir_left * 1 + ir_center * 2 + ir_right * 3) / total) - 2
  return error

def setup():
  alvik.begin()
  delay(1000)  # Short delay to stabilize after initialization

def loop():
  global error
  global integral
  global last_error

  # Get the current error from the line sensors
  error = get_position_error()
  integral += error
  derivative = error - last_error

  # PID calculation to determine speed adjustment
  adjustment = KP * error + KI * integral + KD * derivative

  # Adjust speeds
  left_speed = BASE_SPEED + adjustment
  right_speed = BASE_SPEED - adjustment

  # Ensure speeds stay in the range 0-70 RPM
  left_speed = max(0, min(70, left_speed))
  right_speed = max(0, min(70, right_speed))

  # Set wheel speeds
  alvik.set_wheels_speed(left_speed, right_speed)

  # Update the last error
  last_error = error
  delay(100)  # Small delay to allow smoother control

def cleanup():
  alvik.stop()

start(setup, loop, cleanup)
