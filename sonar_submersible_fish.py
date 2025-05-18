from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()
def sonar():
    MoveForward(635)
    TurnLeft(47)
    wait(20)
    MoveForward(250)
    TurnRight(28)
    wait(45)
    MoveBackward(90)
    TurnLeft(30)
    wait(45)
    TurnRight(17)
    MoveForward(70)
    TurnRight(13)
    wait(10)
    TurnLeft(25)
    MoveForward(30)
    TurnLeft(55)
    wait(100)
    MoveBackward(50)

def submersible():
    MoveForward(330)
    MoveLeftArmUp(350, 380)
    TurnRight(70)
    StopAtBlack(60)
    MoveForward(140)
    MoveLeftArmDown(900, 230)
    wait(10)
    MoveLeftArmUp(320, 90)

def angler():
    MoveBackward(140)
    TurnRight(90)
    TurnRight(20)
    MoveBackward(280)
    TurnLeft(45)
    MoveBackward(50)
    TurnLeft(35)
    MoveBackward(20)
    
    

def octo():
    TurnRight(90)
    MoveForward(190)
    
def sonar_submersible_angler_octo():
    sonar()
    submersible()
    angler()
    octo()
#sonar_submersible_angler_octo()




