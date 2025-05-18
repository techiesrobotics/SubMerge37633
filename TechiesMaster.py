from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from TechiesDriveBase import *

def trident():
    SetSpeed(700)
    MoveForward(285)
    TurnRight(90)
    MoveForward(510)
    TurnLeft(51.5)
    SetSpeed(400)
    MoveForward(70)
    MoveRightArmUp(100,425)
    MoveBackward(20)
    wait(300)
    MoveRightArmDown(100,315)
    SetSpeed(700)
    MoveBackward(100)
    TurnRight(60)
    MoveBackward(600)
