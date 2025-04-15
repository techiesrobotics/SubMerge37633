from TechiesDriveBase import *

hub = PrimeHub()
def FSIshippinglanes():
    SetSpeed(900)
    MoveForward(-455)
    wait(8)
    TurnRight(35)
    MoveForward(20)
    MoveForward(-45)
    MoveRightArmUp(1000,65)
    wait(4)
    TurnRight(60)

def FSIunexpectedencounter():
    TurnLeft(60)
    MoveForward(150)
    TurnRight(110)
    MoveForward(240)
    MoveBackward(400)
    SetGyro(False)

def FSIcoralsegments():
    PauseMission()
    SetSpeed(100)
    MoveForward(-40)
    MoveBackward(-120)

def FSIshippinglanes_octo_segments():
    FSIshippinglanes()
    FSIunexpectedencounter()
    FSIcoralsegments()

FSIshippinglanes_octo_segments()

