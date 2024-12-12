from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *
from TechiesArm import *

##########################
# For Team 37633 Techies #
# Run_CollectLeftTree.py #
##########################


def collectLeftPiece():
    #This function will collect the left side pieces
    SetSpeed(800)
    MoveForward(420)
    MoveRightArmDown(500,90)
    MoveBackward(525)


def collectTree():
    #This function will collect the tree from it's holder
    SetSpeed(900)
    MoveForward(325)
    MoveBackward(325)
    

def Do_CollectLeftTree():
    #This function calls both individual mission functions and combines them
    collectLeftPiece()
    PauseMission()
    collectTree()
    
    

    #hub = PrimeHub()

#Do_CollectLeftTree() NEVER ENABLE WHEN RUNNING MASTER CODE