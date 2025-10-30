from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()
Distance = 0
exitDistance = 0

def calibration():
    global Distance, exitDistance
    #rotate the alvik
    alvik.set_wheels_speed(-15, 15)  

    for _ in range(1000): 
      #get the furthest distance
        left, cleft, center, cright, right = alvik.get_distance()
        delay(10)
        #check if new furthest distance
        if center > Distance:
            Distance = center
            alvik.left_led.set_color(1, 0, 0)
            alvik.right_led.set_color(1, 0, 0)
            delay(100)
            alvik.left_led.set_color(0, 0, 0)
            alvik.right_led.set_color(0, 0, 0)

    #stop the alvik
    alvik.set_wheels_speed(0, 0)
  
    exitDistance = Distance  
    delay(1000)  


def FindExit():
    global exitDistance
    #rotate the alvik but slower
    alvik.set_wheels_speed(-5, 5)
    for _ in range(20000):  
        left, cleft, center, cright, right = alvik.get_distance()
        delay(1)

        if abs(exitDistance - center) < 3:  
            alvik.set_wheels_speed(0, 0)
            delay(500)
            #drive towards exit
            alvik.set_wheels_speed(30, 30)
            delay(20000)
            #stop the alvik
            alvik.set_wheels_speed(0, 0)
            #stop the function
            break
          
def setup():
    alvik.begin()
    delay(1000)
    calibration()
    FindExit()


def loop():

    delay(5000)


def cleanup():
    alvik.stop()



start(setup, loop, cleanup)