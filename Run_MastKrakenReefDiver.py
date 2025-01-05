####################################
#      For Team 37633 Techies      #
#   Run_MastHangDiverReefShark.py  #
####################################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *

def mastKraken():
    #This function completes the "Raising the Mast" and "Kraken's Treasure" Missions
    SetSpeed(900)
    TurnRight(30)
    MoveForward(450)
    SetSpeed(100)
    TurnRight(60)
    SetSpeed(900)
    MoveForward(450)
    MoveBackward(20)
    MoveForward(60)
    SetSpeed(170)
    MoveBackward(140)
    '''
    SetSpeed(900)
    TurnLeft(70)
    MoveBackward(620)
    '''
    
def hangDiverandHitCoralReef(): # hang diver and hit coral bud
    TurnRight(106)
    MoveBackward(213)
    MoveRightArmUp(200, 8)
    SetSpeed(900)
    TurnRight(23)
    MoveForward(810)

def doShark():
    MoveBackward(190)
    right_arm.run_until_stalled(200, duty_limit=50)
    MoveRightArmDown(200, 20)
    MoveForward(140)
    TurnRight(35)
    SetSpeed(900)
    MoveForward(800)

def Do_MastKrakenReefDiver():
    #This function calls both individual mission functions and combines them
    mastKraken()
    hangDiverandHitCoralReef()
    #doShark()
    
#Do_MastKrakenReefDiver()
