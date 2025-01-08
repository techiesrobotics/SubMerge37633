from TechiesDriveBase import *
hub = PrimeHub()

SetSpeed(450)
def backupsubmersible(): 
    MoveForwardWithAccel(730, 1000, 1000)
    TurnLeft(90)
    run_task(DriveForwardAndMoveArm(340, left_arm, 210, -135))
    TurnRight(45)
    MoveForward(55)
    wait(5)
    StopAtWhite(290)
    MoveArmWithStallTimeDetection(left_arm, 500, 120)
    print(left_arm.load())

def octo():
    MoveBackward(180)
    TurnRight(100)
    MoveBackward(180)

def submersible_octo():
    backupsubmersible()
    octo()

#submersible_octo()
