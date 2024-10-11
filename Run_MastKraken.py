from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()
'''
SetSpeed(350)
drive_base.curve(485,90)
drive_base.curve(-420,100)
'''

def main():
    mastKraken()

def mastKraken():
    SetSpeed(900)
    MoveForward(250)
    TurnRight(30)
    MoveForward(285)
    TurnRight(60)
    SetSpeed(900)
    MoveForward(240)
    MoveBackward(20)
    MoveForward(20)
    MoveBackward(75)
    TurnLeft(60)
    MoveBackward(525)
