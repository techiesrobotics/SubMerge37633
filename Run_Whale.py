from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def main():
    whale()

def whale():
    SetSpeed(500)
    MoveForward(680)
    TurnRight(45)
    SetSpeed(585)
    MoveForward(300)
    MoveBackward(250)
    TurnLeft(55)
    MoveBackward(700)

