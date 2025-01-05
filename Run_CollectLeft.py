##########################
# For Team 37633 Techies #
# Run_CollectLeftTree.py #
##########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *

def collectLeftPiece():
    #This function will collect the left side pieces
    SetSpeed(800)
    MoveForward(470)
    MoveLeftArmDown(500,90)
    MoveBackward(620)

# removed from run
'''
def collectTree():
    #This function will collect the tree from it's holder
    SetGyro(True)
    SetSpeed(900)
    MoveForward(390)
    MoveBackward(400)
'''  

def Do_CollectLeftTree():
    #This function calls both individual mission functions and combines them
    collectLeftPiece()
    #PauseMission()
    #collectTree()

#Do_CollectLeftTree() #NEVER ENABLE WHEN RUNNING MASTER CODE
