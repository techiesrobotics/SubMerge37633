##########################
#     For team 37633     # 
# Run_BudsDiverSharkReef #
##########################

from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def Do_BudsDiverSharkReef():
    #SetAccel(650, 650)
    coralBudsAndDiver()
    shark()
    coralReef()


def coralBudsAndDiver():
    ######do Coral Buds ######
    SetSpeed(500)
    # coral buds mission #
    MoveForward(620)  
    TurnLeft(90)    
    
    MoveRightArmDown(160, 70)
    MoveLeftArmUp(160, 95)
    MoveForward(170)
    MoveLeftArmDown(60, 160)
    MoveLeftArmUp(100, 30)
    DetectArmStall(right_arm, 80, 30, 80) #
    #MoveRightArmUp(150, 30)
    MoveBackward(170)

# shark mission  #
def shark():
    TurnRight(38)
    MoveForward(320)
    MoveBackward(260)

# Coral Reef #
def coralReef():
    TurnRight(44)
    SetGyro(False)
    MoveForward(460) 
    SetGyro(True)
    SetSpeed(500)
    #MoveBackward(220)
    MoveBackward(1000)

#Do_BudsDiverSharkReef()



