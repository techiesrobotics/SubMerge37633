##########################
# For Team 37633 Techies #
#   Run_LeftToRight.py   #
##########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *

def Run_LeftToRight():
    doDeliverShark()
    doAngler()
    doSeabed()
    doCollectRight()

def doDeliverShark():
    SetSpeed(700)
    MoveForward(50)
    TurnRight(60)
    #MoveForwardWithAccel(600,800,800)
    MoveForward(610)
    MoveBackward(135)
    TurnRight(29)

def doAngler():
    StopAtWhite(300)
    wait(5)
    TurnLeft(90)
    MoveForward(350)
    TurnLeft(77)
    MoveForward(325)
    #TurnLeft(20)
    MoveBackward(100)
    TurnRight(30)
    MoveForward(125)
    TurnRight(60)
    SetGyro(False)
    MoveForward(360)
    SetGyro(True)

def doSeabed():
    MoveRightArmUp(200, 70)
    MoveBackward(185)
    TurnRight(90)

def doCollectRight():
    MoveForward(850)
    TurnRight(12)
    MoveLeftArmDown(200, 92)
    MoveBackward(60)
    SetSpeed(700)
    TurnRight(80)
    MoveForward(310)
    TurnLeft(50)
    MoveForward(550)
    
#Run_LeftToRight()
