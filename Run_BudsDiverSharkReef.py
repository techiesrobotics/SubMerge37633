from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def main():
    coralBudsAndDiver()
    shark()
    coralReef()


def coralBudsAndDiver():
    ######do Coral Buds ######
    SetSpeed(500)
    # coral buds mission #
    MoveForward(635)  
    TurnLeft(90)    
    MoveRightArmDown(150, 67)
    MoveForward(90)
    MoveRightArmUp(150, 35)
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
    MoveBackward(200)
    TurnRight(15)
    MoveBackward(700)

main()