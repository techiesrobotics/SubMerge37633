##########################
#     For team 37633     # 
# sonar_submersible_fish #
##########################

from TechiesDriveBase import *

def sonardiscovery():
    SetSpeed(450)
    MoveForwardWithAccel(730, 300, 300)
    TurnLeft(90)
    MoveForward(245)
    MoveRightArmUp(330, 215)
    MoveBackward(190)

def sendoversubmersible():
    AccelDefaultReset()
    TurnRight(30)
    MoveBackward(100)
    TurnLeft(30)
    MoveRightArmDown(450, 90)
    run_task(DriveForwardAndMoveArm(340, left_arm, 210, -135))
    TurnRight(45)
    MoveForward(55)
    wait(5)
    StopAtWhite(290)
    #DetectArmStall(left_arm, 500, 1500, 40)# The old angle was -15, TODO
    MoveArmWithStallTimeDetection(left_arm, 500, 150)
    print(left_arm.load())

def anglerfish():
    MoveBackward(280)
    TurnLeft(53)
    SetSpeed(330)
    MoveForwardWithAccel(500, 1200, 1200)
    TurnLeft(25)
    MoveForward(135)
    TurnLeft(35)
    MoveForwardWithAccel(90, 1200, 1200)
    wait(10)
    MoveBackward(140)

def octopus():
    TurnRight(90)
    MoveBackward(180)
    
def sonar_submersible_fish():
    sonardiscovery()
    sendoversubmersible()
    anglerfish()
    octopus()




