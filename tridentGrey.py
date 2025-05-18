from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from TechiesDriveBase import *

SetSpeed(700)
MoveForward(275)
TurnRight(90)
MoveForward(500)
TurnLeft(52)
SetSpeed(400)
MoveForward(70)
MoveRightArmUp(100,415)
MoveBackward(20)
wait(300)
MoveRightArmDown(100,315)
SetSpeed(700)
MoveBackward(100)
TurnRight(40)
MoveBackward(200)
TurnLeft(170)
MoveForward(160)
