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
    SetSpeed(900)
    MoveBackward(230)
    SetSpeed(700)
    TurnRight(29)

def doAngler():
    StopAtWhite(300)
    MoveBackward(100)
    TurnLeft(60)
    MoveForward(285)
    TurnLeft(85)
    MoveForward(450)
    TurnRight(90)
    MoveForward(160)
    TurnLeft(30)
    SetGyro(False)
    MoveForward(360)
    SetGyro(True)

def doSeabed():
    MoveRightArmUp(200, 70)
    MoveBackward(185)
    TurnRight(90)

def doCollectRight():
    MoveForward(885)
    TurnRight(16)
    MoveLeftArmDown(200, 92)
    MoveBackward(90)
    SetSpeed(700)
    TurnRight(80)
    SetSpeed(900)
    MoveForward(850)

#Run_LeftToRight()
