from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from TechiesDriveBase import *

def DeliverSharkyAndCollectTrident():
    SetSpeed(700)
    MoveForward(320)
    TurnRight(90)
    MoveForward(474)
    TurnLeft(49.7)
    MoveForward(177)
    MoveRightArmUp(200,460)
    MoveBackward(20)
    MoveRightArmDown(200,415)
    wait(500)
    MoveBackward(200)
    TurnRight(40)
    MoveBackward(500)

DeliverSharkyAndCollectTrident()