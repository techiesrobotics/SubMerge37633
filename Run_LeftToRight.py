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
    MoveRightArmDown(200, 190)
    MoveForward(50)
    TurnRight(65)
    #MoveForwardWithAccel(600,800,800)
    MoveForward(700)
    SetSpeed(900)
    MoveBackward(250)
    SetSpeed(700)
    TurnRight(22)

def doAngler():
    StopAtWhite(300)
    MoveBackward(100)
    TurnLeft(60)
    MoveForward(285)
    TurnLeft(85)
    MoveForward(440)
    TurnRight(105)
    MoveForward(115)
    TurnLeft(45)
    SetGyro(False)
    MoveForward(330)
    SetGyro(True)

def doSeabed():
    MoveRightArmUp(200, 70)
    MoveBackward(185)
    TurnRight(90)

def doCollectRight():
    MoveForward(810)
    TurnRight(12)
    MoveLeftArmDown(200,89)
    MoveForward(80)
    MoveBackward(60)
    MoveLeftArmUp(200, 92)
    SetSpeed(700)
    TurnRight(70)
    SetSpeed(900)
    MoveForward(850)

#Run_LeftToRight()
