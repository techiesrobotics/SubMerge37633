##########################
#     For team 37633     # 
#    Run_TridentShark    #
##########################

from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def tridentshark():
    SetSpeed(300)
    SetAccel(650, 650)
    MoveForward(50)
    TurnRight(62)
    MoveForward(550)
    TurnLeft(23)
    SetGyro(False)
    SetSpeed(600)
    MoveForward(130)
    SetGyro(True)
    SetSpeed(40)
    MoveBackward(130)
    SetSpeed(900)
    MoveBackward(40)
    TurnRight(40)
    SetSpeed(900)
    MoveBackward(660)

#tridentshark()
