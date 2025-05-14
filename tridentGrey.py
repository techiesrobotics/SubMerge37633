from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from TechiesDriveBase import *

def trident():
  SetSpeed(700)
  MoveForward(200)
  TurnRight(90)
  MoveForward(340)
  TurnLeft(50.7)
  SetSpeed(400)
  MoveForward(180)
  MoveRightArmUp(100,415)
  MoveBackward(20)
  wait(300)
  MoveRightArmDown(100,315)
  SetSpeed(700)
  MoveBackward(300)
  TurnLeft(100)
  MoveForward(50)
