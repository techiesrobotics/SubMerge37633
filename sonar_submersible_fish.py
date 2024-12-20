##########################
#     For team 37633     # 
# sonar_submersible_fish #
##########################

from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def sonar():
    SetSpeed(450)
    #MoveForward(730) #740
    MoveForwardWithAccel(730, 300, 300)
    TurnLeft(90)
    MoveForward(245)
    MoveRightArmUp(330, 215)
    MoveBackward(190)

def submersible():
    drive_base.reset
    TurnRight(30)
    MoveBackward(100) #110
    TurnLeft(30)
    MoveRightArmDown(450, 90)
    move_and_leftdown(230, 450, 210, 120)
    TurnRight(45)
    MoveForward(40)
    wait(10)
    StopAtWhite(290)
    MoveLeftArmUp(500, 100)
    DetectArmStall(left_arm, 150, -15, 60)

def fish():
    MoveBackward(280) #320
    TurnLeft(53)
    SetSpeed(330) #350
    MoveForward(500)
    TurnLeft(25)
    MoveForward(135)
    TurnLeft(35)
    MoveForward(90)
    wait(10)
    MoveBackward(140)

def octo():
    TurnRight(90)
    MoveBackward(131)
    
def sonar_submersible_fish():
    sonar()
    submersible()
    fish()
    octo()

