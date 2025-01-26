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
    MoveRightArmDown(200, 210)
    MoveForward(50)
    TurnRight(65)
    #MoveForwardWithAccel(600,800,800)
    MoveForward(700)
    SetSpeed(900)
    MoveBackward(310)
    SetSpeed(700)
    TurnRight(23)

def doAngler():
    StopAtWhite(300)
    MoveBackward(100)
    TurnLeft(60)
    MoveForward(285)
    TurnLeft(85)
    MoveForward(440)
    TurnRight(110)
    MoveForward(120)
    TurnLeft(50)
    SetGyro(False)
    MoveForward(360)
    MoveBackward(20)
    SetGyro(True)
    

def doSeabed():
    MoveRightArmUp(200, 70)
    MoveBackward(200)
    TurnRight(90)

def doCollectRight():
    MoveForward(830)
    TurnRight(21)
    MoveLeftArmDown(200,92)
    MoveForward(25)
    MoveBackward(120)
    MoveLeftArmUp(200, 92)
    SetSpeed(700)
    TurnRight(60)
    SetSpeed(900)
    MoveForward(850)

#Run_LeftToRight()
