##########################
#     For team 37633     # 
#    Run_TridentShark    #
##########################

from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def tridentshark():
    SetSpeed(400)
    SetAccel(650, 650)
    MoveForward(50)
    TurnRight(62)
    MoveForward(540)
    TurnLeft(23)
    SetGyro(False)
    MoveForward(130)
    SetGyro(True)
    MoveRightArmDown(150, 30)
    MoveBackward(130)
    SetSpeed(900)
    TurnRight(30)
    MoveBackward(600)

tridentshark()
