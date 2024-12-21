from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *

<<<<<<< Updated upstream

=======
ORANGE_HIGH = 20
ORANGE_LOW = 1
RED_HIGH = 365
RED_LOW = 349
MAGENTA_HIGH = 342
MAGENTA_LOW = 330
BLUE_HIGH = 225
BLUE_LOW = 210
PURPLE_HIGH = 250
PURPLE_LOW = 230
>>>>>>> Stashed changes

def determineColor():
    while True:
        myHSV = color_sensor_side.hsv(True)
        myColor = color_sensor_side.color(True)
<<<<<<< Updated upstream
        print(myHSV, myColor )

        if(Color.RED == myColor):
            if(myHSV.h > 1 and myHSV.h < 20):
                print("it's orange")
            elif(myHSV.h > 330 and myHSV.h < 342):
                print("it's magenta")
            elif(myHSV.h > 350 and myHSV.h < 360):
                print("it's red")
            else:
                print ("======================too close to tell")
        elif(Color.BLUE == myColor):
            print("it's blue")
=======
        print(myHSV, myColor)
        
        
        if(Color.RED == myColor):
            if(myHSV.h > ORANGE_LOW and myHSV.h < ORANGE_HIGH):
                print("it's orange")
            elif(myHSV.h > 330 and myHSV.h < 342):
                print("it's magenta")
            elif(myHSV.h > RED_LOW and myHSV.h < RED_HIGH):
                print("it's red")
            else:
                print ("======================too close to tell")
        
        elif(Color.BLUE == myColor):
            if(myHSV.h > 233 and myHSV.h < 250):
                print("it's purple")
            elif(myHSV.h > 212 and myHSV.h < 220):
                print("it's blue")
            else:
                print("==================too close to tell")
>>>>>>> Stashed changes
        elif(Color.GREEN == myColor):
            print("it's green")
        elif(Color.YELLOW == myColor):
            print("it's yellow")
        elif(Color.WHITE == myColor):
            print("it's white")
        else:
            print ("can not detect color")
<<<<<<< Updated upstream
            
        wait(100)
        
=======

        wait(100)
        
        
>>>>>>> Stashed changes

determineColor()

