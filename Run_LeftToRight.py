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
    SetSpeed(500)
    MoveForward(50)
    TurnRight(62)
    MoveForward(580)
    MoveBackward(125)
    TurnRight(28)

def doAngler():
    StopAtWhite(300)
    TurnLeft(90)
    MoveForward(395)
    TurnLeft(90)
    MoveForward(340)
    TurnLeft(20)
    MoveBackward(150)
    TurnRight(90)
    MoveForward(160)
    TurnRight(20)
    SetGyro(False)
    MoveForward(360)
    SetGyro(True)

def doSeabed():
    MoveRightArmUp(200, 70)
    MoveBackward(185)
    TurnRight(90)

def doCollectRight():
    MoveForward(710)
    TurnLeft(10)
    MoveForward(120)
    TurnRight(40)
    MoveForward(26)
    left_arm.run_until_stalled(-100)
    MoveLeftArmUp(80, 40)
    MoveBackward(40)
    SetSpeed(700)
    TurnRight(80)
    MoveForward(310)
    TurnLeft(50)
    MoveForward(550)
    
#Run_LeftToRight()

