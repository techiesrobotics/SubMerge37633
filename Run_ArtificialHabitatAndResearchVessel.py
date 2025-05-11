from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *

hub = PrimeHub()


SetSpeed(800)

#recode - below

MoveForward(400)
MoveRightArmUp(800,50)
MoveForward(400)
MoveBackward(200)
MoveRightArmUp(800,40)
MoveRightArmUp(600,27)
TurnRight(45)
MoveRightArmUp(600,30)
MoveForward(130)
TurnLeft(35)
MoveForward(350)

SetSpeed(200)
MoveRightArmDown(100,10)
MoveBackward(100)
MoveBackward(200)
wait(300)
MoveBackward(100)
TurnLeft(100)
MoveForward(200)
TurnRight(90)
MoveForward(600)