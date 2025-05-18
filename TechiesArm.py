###################################
#         For team 37633          # 
#         TechiesArm.py           #
#    This file defines the arm    #
#        movement functions       #
###################################

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

#The asynchronous function allows two motors to run at the same time.

async def moveArmUp(arm, speed, angle):
    await arm.run_angle(speed, angle)

async def moveArmDown(arm, speed, angle):
    await arm.run_angle(speed, -1 * angle)
    
async def moveBothArmUp(speed, angle):
    await multitask(moveArmUp(left_arm, speed, angle), moveArmUp(right_arm,speed, angle))
    
async def moveBothArmDown(speed, angle):
    await multitask(moveArmDown(left_arm, speed, angle), moveArmDown(right_arm, speed, angle))

# This function detects the stall on the motor to tell if it gets stuck
# The motor continues to run until it reaches the desired angle on surpasses the max load.
# When the function is called, we must type in the max load based on testing.
# We test the load on the motor when there is no stall and code the program to print the load.
# Then we add strain on the motor to see what the load is when it stalls.
# That number will be our max load.
def DetectArmStall(arm, speed, angle, maxLoad):
    arm.reset_angle(0)
    arm.run(angle)
    while abs(arm.load()) < abs(maxLoad):
        print("======", arm.load())

        if abs(arm.angle()) < abs(angle):
            wait(1)
        else:
            break
    arm.hold()

# This function detects stall by starting a watch when the arm starts moving.
# When the needed angle is reached or the watch reaches a specific time, the program continues.
# The number for the watch is important because if it is too small, the arm won't have enough time to reach it's angle. But if it's too big, it will waste too much time.
def MoveArmWithStallTimeDetection(arm, speed, angle, time):
    arm.reset_angle(0)
    arm.run(angle)
    watch = StopWatch()
    while abs(arm.angle() < abs(angle)):
        if watch.time() > time:
            break
    arm.hold()
