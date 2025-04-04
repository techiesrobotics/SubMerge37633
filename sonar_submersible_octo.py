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
    AccelDefaultReset()
    SetSpeed(800)
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

def octo():
    MoveBackward(180)
    TurnRight(100)
    MoveBackward(180)
   
def sonar_submersible_octo():
    sonar()
    submersible()
    octo()
