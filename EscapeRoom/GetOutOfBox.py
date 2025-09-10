from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
    alvik.begin()
    delay(1000)

def loop():
    left, cleft, center, cright, right = alvik.get_distance()
    print(left, "|", cleft, "|", center, "|", cright, "|", right)
    delay(100)

    # If an obstacle is detected within 40 cm on all sides
    if center < 40 and left < 40 and cleft < 40 and cright < 40 and right < 40:
        alvik.set_wheels_speed(50, -50)   # ✅ turn with stronger speed
        print("Turn in place")
    else:
        alvik.set_wheels_speed(50, 50)    # ✅ drive forward with stronger speed
        print("Drive forward")

def cleanup():
    alvik.stop()

start(setup, loop, cleanup)