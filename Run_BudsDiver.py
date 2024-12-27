##########################
#     For team 37633     # 
# Run_BudsDiverSharkReef #
##########################

from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def Do_BudsDiver():
    #SetAccel(650, 650)
    coralBudsAndDiver()


def coralBudsAndDiver():
    
    ######do Coral Buds ######
    SetSpeed(500)
    # coral buds mission #
    MoveForward(630)  
    TurnLeft(90)    
    MoveRightArmDown(160, 70)
    MoveForward(170)
    DetectArmStall(right_arm, 80, 30, 80) #
    #MoveRightArmUp(150, 30)
    MoveBackward(140)
    TurnLeft(65)
    SetSpeed(900)
    MoveForward(680)

#Do_BudsDiver()

