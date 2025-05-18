from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def shippinglanes():
    MoveForward(435)
    TurnRight(25)
    MoveForward(55)
    wait(10)
    MoveRightArmUp(200, 65)
    TurnRight(30)
    MoveBackward(140)
    TurnRight(70)

def octo():
    MoveBackward(195)
    SetSpeed(900)
    MoveForward(400)

'''
def coralsegments():
    PauseMission()
    SetSpeed(100)
    MoveForward(40)
    MoveBackward(120)
'''

def shippinglanes_octo():
    shippinglanes()
    octo()
    #coralsegments()
