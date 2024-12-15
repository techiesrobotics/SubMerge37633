from TechiesDriveBase import *
from TechiesArm import *
hub = PrimeHub()

def shippinglanes():
    SetSpeed(580)
    MoveForward(400)#415 with 2 wheels
    wait(8)
    TurnRight(30)
    MoveForward(80) #60 with 2 wheels
    MoveRightArmUp(200, 60)
    TurnRight(30)
    MoveBackward(180) #175 with 2 wheels
    wait(100)

def unexpectedencounter():
    TurnRight(63) #75
    wait(5)
    MoveBackward(60) #70 with 2 wheels
    MoveForward(460)

def coralsegments():
    PauseMission()
    SetSpeed(100)
    MoveForward(40)
    MoveBackward(120)

shippinglanes()
unexpectedencounter()
coralsegments()


