from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TechiesDriveBase import *

hub = PrimeHub()

SetSpeed(100)
#dump samples
MoveForward(350)
TurnRight(35)
SetSpeed(900)
MoveForward(150)

# move resaerch vessel

SetSpeed(600)
MoveBackward(70)
TurnLeft(32)
MoveForward(200)
TurnLeft(10)
MoveRightArmUp(300,30)
MoveForward(350)
MoveBackward(250)
MoveRightArmUp(800,40)
MoveRightArmUp(600,27)
wait(300)
SetSpeed(300)
MoveRightArmUp(400,40)
TurnRight(45)
MoveRightArmUp(300,20)
MoveForward(280)
TurnLeft(30)
MoveForward(300)

# complete artificial habitat

wait(500)

MoveRightArmDown(300,45)
TurnLeft(8)
SetSpeed(200)
MoveBackward(100)
MoveBackward(200)
wait(300)
MoveBackward(100)
TurnLeft(30)
MoveBackward(100)
TurnRight(40)
MoveBackward(50)
TurnLeft(90)
MoveForward(250)
TurnRight(85)
SetSpeed(900)
MoveForward(950)



###PAST CODE###

'''
SetSpeed(600)
MoveBackward(70)
TurnLeft(37)
MoveForward(200)
MoveRightArmUp(300,40)


MoveForward(350)
MoveBackward(200)
MoveRightArmUp(800,40)
MoveRightArmUp(600,27)
TurnRight(30)
MoveRightArmUp(600,30)
MoveForward(250)
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
'''
'''
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
'''
