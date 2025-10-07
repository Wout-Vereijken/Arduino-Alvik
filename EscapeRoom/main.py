from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
    alvik.begin()
    print("")
    print("Choose which script you want to use")
    print("Red: escape room")
    print("Green: walk the bridge")
    print("Blue: rainbow road")

    global pressed
    pressed = False
  
    global amount
    amount = 1

def loop():
    global amount, pressed
  
    # Read button states
    button = alvik.get_touch_ok()
    buttonUp = alvik.get_touch_up()
    buttonDown = alvik.get_touch_down()
  
    # Handle button presses with debounce
    if button and not pressed:
        print("OK pressed")
        pressed = True

        # Run selected program
        if amount == 1:
            print("Running Escape Room script...")
            exec(open("getoutofbox.py").read())

        elif amount == 2:
            print("Running Walk the Bridge script...")
            exec(open("WalkBridge.py").read())

        elif amount == 3:
            print("Running Rainbow Road script...")
            exec(open("RainbowRoad.py").read())

    elif buttonUp and not pressed:
        amount += 1
        pressed = True
        delay(200)

    elif buttonDown and not pressed:
        amount -= 1
        pressed = True
        delay(200)

    # Reset pressed flag when no buttons are touched
    if not (button or buttonUp or buttonDown):
        pressed = False

    # Wrap-around logic for menu
    if amount == 4:
        amount = 1
    if amount == 0:
        amount = 3

    # Set LED colors for menu options
    if amount == 1:
        alvik.left_led.set_color(1, 0, 0)   # red
        alvik.right_led.set_color(1, 0, 0)
    elif amount == 2:
        alvik.left_led.set_color(0, 1, 0)   # green
        alvik.right_led.set_color(0, 1, 0)
    elif amount == 3:
        alvik.left_led.set_color(0, 0, 1)   # blue
        alvik.right_led.set_color(0, 0, 1)

    delay(100)

def cleanup():
    alvik.stop()
    print("Cleanup done.")

start(setup, loop, cleanup)
