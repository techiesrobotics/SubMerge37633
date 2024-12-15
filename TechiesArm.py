from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task

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

def DetectArmStall(arm, speed, angle, maxLoad):
    arm.reset_angle(0)
    arm.run(angle)
    while abs(arm.load()) < abs(maxLoad):
        if abs(arm.angle()) < abs(angle):
            print(arm.angle())
            wait(1)
        else:
            break
    arm.hold()

#MoveLeftArmUp(100, 90)
#MoveLeftArmDown(100, 90)

#MoveRightArmUp(100,90)
#MoveRightArmDown(100,90)

#run_task(moveBothArmUp(100, 90))


