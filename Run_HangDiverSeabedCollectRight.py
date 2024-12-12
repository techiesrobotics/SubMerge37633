###################################
#         For team 37633          # 
# Run_HangDiverSeabedCollectRight #
###################################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def Do_HangDiverSeabedCollectRight():
    hangDiver()
    seabedSample()
    collectRight()

def hangDiver():
    SetSpeed(400)
    MoveForward(735)
    TurnRight(35)
    #MoveRightArmDown(200, 56)
    MoveForward(100)

    MoveRightArmDown(200, 12)
    wait(30)
    MoveBackward(130)

def seabedSample():
    TurnRight(54)
    #MoveRightArmDown(200, 10)
    MoveForward(500)
    TurnLeft(90)
    MoveForward(80)
    MoveRightArmUp(200, 70)
    MoveBackward(100)
    TurnRight(90)

def collectRight():
    MoveForward(760)
    TurnLeft(10)
    MoveForward(120)
    TurnRight(20)
    MoveForward(40)
    MoveLeftArmDown(200, 110)
    MoveBackward(30)
    TurnRight(95)
    MoveForward(360)
    TurnLeft(50)
    MoveForward(530)

#####Not Used ########
def RaiseSharedMission():
    TurnRight(70)
    #PauseMission()
    MoveForward(220)
    #PauseMission()
    TurnLeft(20)
    #PauseMission()
    MoveLeftArmUp(200, 70)
    MoveLeftArmDown(200, 70)
    MoveBackward(200)
    MoveLeftArmUp(200, 100)
    #################

#Do_HangDiverSeabedCollectRight()