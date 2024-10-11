from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def main():
    hangNursery()

def hangNursery():
    SetSpeed(300)
    MoveForward(110)
    MoveLeftArmUp(50, 35)
    MoveForward(100)
    MoveLeftArmUp(50, 33)
    MoveForward(125)
    MoveLeftArmDown(800, 30)
    MoveBackward(500)

main()

