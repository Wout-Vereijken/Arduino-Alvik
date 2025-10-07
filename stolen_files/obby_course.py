from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

# Convert distance (in cm) to time, assuming speed (R) in cm/s
# Adjust this conversion factor based on testing/calibration
def forward_cm(R, cm):
    # Time calculation assuming speed R (in cm/s)
    time_per_cm = 1000 / R  # ms per cm
    t = cm * time_per_cm
    alvik.set_wheels_speed(R, R)
    delay(int(t))
    alvik.set_wheels_speed(0, 0)

# Pivot turn 90 degrees to the right in place
def pivot_90_right():
    alvik.set_wheels_speed(30, 0)
    delay(2600)  # Adjust timing based on real-world testing
    alvik.set_wheels_speed(0, 0)

# Pivot turn 90 degrees to the right but with one wheel moving forward and one backward
def pivot_90_right_with_opposing_wheels():
    alvik.set_wheels_speed(30, -30)
    delay(2600)  # Adjust timing based on real-world testing
    alvik.set_wheels_speed(0, 0)

# Smooth turn: one wheel moves faster than the other for a smoother curve
def smooth_right_turn():
    alvik.set_wheels_speed(30, 15)  # Adjust speed for smooth turn
    delay(3000)  # Adjust time based on the angle and desired smoothness
    alvik.set_wheels_speed(0, 0)

def setup():
    alvik.begin()
    delay(1000)

def loop():
    # Go forward 30 cm
    forward_cm(10, 30)
    
    # Pivot turn 90 degrees to the right
    pivot_90_right()
    
    # Go forward 30 cm
    forward_cm(10, 30)
    
    # Pivot 90 degrees right but with one wheel moving forward, the other backward
    pivot_90_right_with_opposing_wheels()
    
    # Go forward 30 cm
    forward_cm(10, 30)
    
    # Make a smooth right turn
    smooth_right_turn()

    # End the loop, stopping the robot
    alvik.set_wheels_speed(0, 0)
    while True:
        pass  # Prevent further loop execution

def cleanup():
    alvik.stop()

start(setup, loop, cleanup)