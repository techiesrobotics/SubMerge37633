##########################
#     For team 37633     # 
# Run_BudsDiverSharkReef #
##########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *

def Do_BudsDiverSharkReef():
    coralBudsAndDiver()
    shark()
    coralReef()

def coralBudsAndDiver():
    ######do Coral Buds ######
    SetSpeed(500)
    # coral buds mission #
    MoveForward(635)  
    TurnLeft(90)    
    MoveRightArmDown(150, 73)
    MoveForward(90)
    #DetectArmStall(right_arm, 120, 35, 90)
    #MoveRightArmUp(100, 20)
    MoveArmWithStallTimeDetection(right_arm, 90, 80)
    MoveBackward(170)

# shark mission  #
def shark():
    TurnRight(38)
    MoveForward(320)
    MoveBackward(245)

# Coral Reef #
def coralReef():
    TurnRight(44)
    SetGyro(False)
    MoveForward(460)
    SetGyro(True)
    SetSpeed(500)
    MoveBackward(210)
    TurnRight(15)
    MoveBackward(700)

#Do_BudsDiverSharkReef()
