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
    if center < 60 and left < 30 and cleft < 45 and cright < 45 and right < 30:
        alvik.set_wheels_speed(30, -30)   # ✅ turn with stronger speed
        print("Turn in place")
    else:
        alvik.set_wheels_speed(30, 30)    # ✅ drive forward with stronger speed
        print("Drive forward")

def cleanup():
    alvik.stop()

start(setup, loop, cleanup)