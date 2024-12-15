##########################
#     For team 37633     # 
#        DriveBase       #
##########################
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from TechiesArm import *

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.E)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=110)
drive_base.use_gyro(True)

def IsForceSensorPressed():
    force = ForceSensor(Port.B)
    return force.pressed()

def SetGyro(truefalse):
    drive_base.use_gyro(truefalse)

def SetSpeed(speed):
    drive_base.settings(straight_speed=speed)

def SetAccel(accelStraight, accelTurn):
    drive_base.settings(straight_acceleration=accelStraight, turn_acceleration=accelTurn)
   
def MoveForward(distance):
    drive_base.straight(distance)

def MoveForwardWithAccel(distance, accelStraight, accelTurn):
    drive_base.settings(straight_acceleration=accelStraight, turn_acceleration=accelTurn)
    drive_base.straight(distance)

def MoveBackwardWithAccel(distance, accelStraight, accelTurn):
    drive_base.settings(straight_acceleration=accelStraight, turn_acceleration=accelTurn)
    drive_base.straight(-1 * distance)

def MoveBackward(distance):
    drive_base.straight(-1* distance)
    
def TurnRight(degrees):
    drive_base.turn(degrees)

def TurnLeft(degrees):
    drive_base.turn(-1* degrees)

def StopAtWhite(speed):
    drive_base.drive(speed, 0)
    print("reflection", color_sensor.reflection())
    while(color_sensor.reflection() < 97):
        wait(10)
    print("reflection", color_sensor.reflection())
    drive_base.brake()

def PauseMission():
    print("start pause mission")
    SetGyro(False)
    while Button.LEFT not in hub.buttons.pressed():
        wait(10)
    print("pause mission end")
    SetGyro(True)

def MoveForwardWithSuddenStop(distance):
    drive_base.use_gyro(True)
    drive_base.drive(800, 0)
    while drive_base.distance()< distance : 
        print(drive_base.distance())
        wait(20)
    drive_base.straight(0)

def move_and_leftdown(robot_distance, SetSpeed, armspeed, angle):
    left_motor.run(SetSpeed) 
    right_motor.run(SetSpeed) 
    left_arm.run_target(armspeed, -1 * angle)
    MoveForward(robot_distance)
