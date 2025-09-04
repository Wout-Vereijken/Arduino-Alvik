from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
  alvik.begin()
  delay(1000)
  
def loop():
    roll, pitch, yaw = alvik.get_orientation()
    print("Yaw:", yaw)
    
    BASE_SPEED = 10
    MULTIPLIER = 0.5   # lower so it doesn’t spin too violently
    
    NewYaw = yaw - 180
    extra_rpm = abs(NewYaw) * MULTIPLIER
    adapted_speed = BASE_SPEED + extra_rpm

    if yaw > 185:  # Need to turn right
        print("Turn Right")
        alvik.set_wheels_speed(adapted_speed, -adapted_speed)

    elif yaw < 175:  # Need to turn left
        print("Turn Left")
        alvik.set_wheels_speed(-adapted_speed, adapted_speed)

    else:
        print("Aligned! Stop.")
        alvik.set_wheels_speed(0, 0)
    
    delay(200)
  
def cleanup():
  alvik.stop()
  
start(setup, loop, cleanup)