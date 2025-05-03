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
    MoveForward(190)
    TurnRight(20)
    MoveForward(405)
    SetSpeed(100)
    TurnRight(70)
    SetSpeed(400)
    MoveForward(200)
    '''MoveBackward(20)
    MoveForward(90)
    SetSpeed(170)'''
    MoveBackward(170)

def hangDiverCoralBuds():
    #This function hangs the diver on the rack and flips the coral buds
    SetSpeed(600)
    TurnRight(88)
    SetSpeed(900)
    MoveBackward(510)
  

def Do_MastKrakenReefDiver():
    #This function calls both individual mission functions and combines them
    mastKraken()
    hangDiverCoralBuds()

    
Do_MastKrakenReefDiver()

