from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *



def determineColor():
    while True:
        myHSV = color_sensor_side.hsv(True)
        myColor = color_sensor_side.color(True)
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
        elif(Color.GREEN == myColor):
            print("it's green")
        elif(Color.YELLOW == myColor):
            print("it's yellow")
        elif(Color.WHITE == myColor):
            print("it's white")
        else:
            print ("can not detect color")
            
        wait(100)
        

determineColor()
