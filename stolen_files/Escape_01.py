from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

SPEED = 30      # Base forward speed
TURN_SPEED = 20 # Turning speed
DIST_THRESHOLD = 40  # Distance to consider as "obstacle"
OPEN_THRESHOLD = 50  # Distance to consider as "exit gap"

def setup():
    alvik.begin()
    delay(1000)

def loop():
    # Get distance readings
    left, cleft, center, cright, right = alvik.get_distance()
    print(f"L:{left} CL:{cleft} C:{center} CR:{cright} R:{right}")
    delay(10)

    # Check if there’s an open gap ahead
    if center > OPEN_THRESHOLD:
        # Exit detected → move straight ahead
        alvik.set_wheels_speed(SPEED, SPEED)
        return

    # If blocked ahead, decide turn direction
    if center < DIST_THRESHOLD or cleft < DIST_THRESHOLD or cright < DIST_THRESHOLD:
        if left > right:
            # Turn left (more space on the left side)
            alvik.set_wheels_speed(-TURN_SPEED, TURN_SPEED)
        else:
            # Turn right
            alvik.set_wheels_speed(TURN_SPEED, -TURN_SPEED)
    else:
        # Otherwise, move forward along the corridor
        alvik.set_wheels_speed(SPEED, SPEED)

def cleanup():
    alvik.stop()

start(setup, loop, cleanup)
