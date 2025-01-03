##########################
#     For team 37633     # 
# sonar_submersible_fish #
##########################

from TechiesDriveBase import *

def sonar():
    SetSpeed(450)
    MoveForwardWithAccel(730, 300, 300)
    TurnLeft(90)
    MoveForward(245)
    MoveRightArmUp(330, 215)
    MoveBackward(190)

def submersible():
    TurnRight(30)
    MoveBackward(100)
    TurnLeft(30)
    MoveRightArmDown(450, 90)
    run_task(DriveForwardAndMoveArm(230, left_arm, 210, 100))
    TurnRight(45)
    MoveForward(40)
    wait(10)
    StopAtWhite(290)
    DetectArmStall(left_arm, 500, 100, 40)# The old angle was -15, TODO
    print(left_arm.load())

def fish():
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

def octo():
    TurnRight(90)
    MoveBackward(180)
    
def sonar_submersible_fish():
    sonar()
    submersible()
    fish()
    octo()




