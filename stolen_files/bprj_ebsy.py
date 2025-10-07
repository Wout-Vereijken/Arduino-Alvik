from arduino import *
from arduino_alvik import ArduinoAlvik
import time
import random

alvik = ArduinoAlvik()

BASE_SPEED = 20 # Wheel speed
detected_colors = set()  # Stores unique colors
color_count = 0  # Counts unique colors detected

# Defined raw color ranges
RGB_COLOR_RANGES = {   
    "ORANGE": ((316, 252, 255), (336, 272, 275)),
    "RED": ((265, 204, 232), (285, 224, 252)),
    "GREEN": ((178, 224, 221), (198, 244, 241)),
    "LIME": ((245, 280, 252), (265, 300, 272)),
    "PINK": ((270, 202, 241), (290, 222, 261)),
    "LIGHT BLUE": ((197, 271, 350), (217, 291, 370)),
    "DARK BLUE": ((175, 206, 248), (195, 226, 268)),
}

def setup():
    alvik.begin()  # Initialize the Alvik environment
    time.sleep(1)  # Delay for initialization

def get_color_from_rgb(r, g, b):
    for color, (lower, upper) in RGB_COLOR_RANGES.items():
        if lower[0] <= r <= upper[0] and lower[1] <= g <= upper[1] and lower[2] <= b <= upper[2]:
            return color
    return None

def celebration_dance():
    print("5 colors found")

    # Make LEDs blue
    alvik.left_led.set_color(0, 0, 1)
    alvik.right_led.set_color(0, 0, 1)
  
    # Wiggle left and right
    for _ in range(100):  # Amount of wiggles
        alvik.set_wheels_speed(BASE_SPEED, -BASE_SPEED)  # Wiggle right
        time.sleep(0.3)
        alvik.set_wheels_speed(-BASE_SPEED, BASE_SPEED)  # Wiggle left
        time.sleep(0.3)

def control_buttons():
    global BASE_SPEED
    if alvik.get_touch_ok():
        print("OK button pressed: Starting the robot")
        alvik.set_wheels_speed(BASE_SPEED, BASE_SPEED)  # Start moving forward
        
    elif alvik.get_touch_cancel():
        print("Cancel button pressed: Stopping the robot")
        alvik.set_wheels_speed(0, 0)  # Stop the robot

    elif alvik.get_touch_left():  
        print("Left button pressed: Decreasing speed")
        BASE_SPEED = max(0, BASE_SPEED - 1)  # Decrease speed, not below 0
        alvik.set_wheels_speed(BASE_SPEED, BASE_SPEED)  # Update wheels with new speed

    elif alvik.get_touch_right():  
        print("Right button pressed: Increasing speed")
        BASE_SPEED = min(100, BASE_SPEED + 1)  # Increase speed, not above 100
        alvik.set_wheels_speed(BASE_SPEED, BASE_SPEED)  # Update wheels with new speed

def hand_control():
    # Check obstacle distance using distance sensor
    left, cleft, center, cright, right = alvik.get_distance()
    
    # Move backward if hand is too close
    if center <= 12:
        alvik.set_wheels_speed(-BASE_SPEED, -BASE_SPEED)
        return  # Skip the rest of the loop to avoid further actions

    # Move forward once hand is far or out of sight
    elif 18 <= center <= 30:
        alvik.set_wheels_speed(BASE_SPEED, BASE_SPEED)
      
def loop():
    global BASE_SPEED, color_count  # Global variables

    # Check if the celebration condition is met
    if color_count >= 5:
        celebration_dance()
        return  # Exit loop

    # Control button functionalities
    control_buttons()

    # Move backwards if any obstacles obstruct its path
    hand_control()
  
    # Read line sensors
    ir_left, ir_center, ir_right = alvik.get_line_sensors()

    # Color detection
    r, g, b = alvik.get_color_raw()  # Get the raw RGB values
    color = get_color_from_rgb(r, g, b)

    # Set LED color to red
    alvik.left_led.set_color(1, 0, 0)
    alvik.right_led.set_color(1, 0, 0)
  
    # Count & Blink, with random movement on detection
    if color:
        if color not in detected_colors:
            detected_colors.add(color)  # Add the new color to the set
            color_count += 1  # Increment the unique color counter
            print(f"New color detected: {color}. Unique colors detected: {color_count}")

            # Blink LEDs to indicate the count of unique colors detected
            for _ in range(color_count):
                alvik.left_led.set_color(0, 1, 0)
                alvik.right_led.set_color(0, 1, 0)
                time.sleep(0.1)
                alvik.left_led.set_color(1, 0, 0)
                alvik.right_led.set_color(1, 0, 0)
                time.sleep(0.1)

        # Randomize movement direction
        turn_direction = random.choice(["left", "right"])
        if turn_direction == "left":
            alvik.set_wheels_speed(-BASE_SPEED, BASE_SPEED) # Turn left
        else:
            alvik.set_wheels_speed(BASE_SPEED, -BASE_SPEED) # Turn right
        time.sleep(random.uniform(0.5, 1.5)) #Random time between 0.5 and 1.5s for random direction
        alvik.set_wheels_speed(BASE_SPEED, BASE_SPEED) # Resume moving forward after random turn

    # Detect black border
    if ir_center > 300:
        alvik.set_wheels_speed(0, 0)
        time.sleep(0.2)
        alvik.set_wheels_speed(-BASE_SPEED, -BASE_SPEED)
        time.sleep(0.3)
        alvik.set_wheels_speed(0, 0)
        alvik.set_wheels_speed(BASE_SPEED, -BASE_SPEED)
        time.sleep(1)
        alvik.set_wheels_speed(BASE_SPEED, BASE_SPEED) # Resume moving forward after the turn

def cleanup():
    alvik.set_wheels_speed(0, 0)  # Stop all movement

# Start the robot behavior
start(setup, loop, cleanup)
