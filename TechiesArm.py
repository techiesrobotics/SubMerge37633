from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
## this is to test github setup -- download 1 file
## this is 2nd test github setup -- download everything
## this is 3rd test github setup -- create branch
## this is 4th test github setup -- create branch and merge to main
left_arm = Motor(Port.A)
right_arm = Motor(Port.F, Direction.COUNTERCLOCKWISE)

def MoveLeftArmUp(speed, angle):
    left_arm.run_angle(speed, angle)

def MoveLeftArmDown(speed, angle):
    left_arm.run_angle(speed, angle * -1)

def MoveRightArmUp(speed, angle):
    right_arm.run_angle(speed, angle)

def MoveRightArmDown(speed, angle):
    right_arm.run_angle(speed, angle * -1)

async def moveArmUp(arm, speed, angle):
    await arm.run_angle(speed, angle)

async def moveArmDown(arm, speed, angle):
    await arm.run_angle(speed, -1 * angle)

async def moveBothArmUp(speed, angle):
    await multitask(moveArmUp(left_arm, speed, angle), moveArmUp(right_arm,speed, angle))

async def moveBothArmDown(speed, angle):
    await multitask(moveArmDown(left_arm, speed, angle), moveArmDown(right_arm, speed, angle))

#MoveLeftArmUp(100, 90)
#MoveLeftArmDown(100, 90)

#MoveRightArmUp(100,90)
#MoveRightArmDown(100,90)

#run_task(moveBothArmUp(100, 90))


