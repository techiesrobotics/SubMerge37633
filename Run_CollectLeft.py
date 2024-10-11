from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *
from TechiesArm import *

hub = PrimeHub()

def main():
    collectLeftItems()

def collectLeftItems():
    SetSpeed(700)
    MoveForward(420)
    wait(50)
    TurnRight(15)
    MoveBackward(600)

main()