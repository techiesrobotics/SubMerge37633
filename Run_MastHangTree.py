from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *
from TechiesArm import *

##########################
# For Team 37633 Techies #
#  Run_MastHangTree.py   #
##########################

hub = PrimeHub()
'''
SetSpeed(350)
drive_base.curve(485,90)
drive_base.curve(-420,100)
'''
def mastKraken():
    #This function completes the "Raising the Mast" and "Kraken's Treasure" Missions
    SetSpeed(900)
    MoveForward(250)
    TurnRight(30)
    MoveForward(295)
    SetSpeed(250)
    TurnRight(60)
    SetSpeed(300)
    MoveForward(325)
    MoveBackward(10)
    MoveForward(50)
    MoveBackward(110)
    SetSpeed(900)
    TurnLeft(60)
    MoveBackward(525)
    

def hangTree():
    #This function hangs the coral tree
    MoveForward(515)
    MoveLeftArmDown(900,35)
    MoveBackward(515)
    MoveLeftArmUp(900,35)

def Do_MastAndHangTree():
    #This function calls both individual mission functions and combines them
    mastKraken()
    PauseMission()
    hangTree()
    
#Do_MastAndHangTree()
