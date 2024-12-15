##########################
#     For team 37633     # 
#        DriveBase       #
##########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.E)
color_sensor_side = ColorSensor(Port.B)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=110)
drive_base.use_gyro(True)

def SetGyro(truefalse):
    drive_base.use_gyro(truefalse)

def SetSpeed(speed):
    drive_base.settings(straight_speed=speed)

def SetAccel(accelStraight, accelTurn):
    drive_base.settings(straight_acceleration=accelStraight, turn_acceleration=400)
   
def MoveForward(distance):
    drive_base.straight(distance)

def MoveForwardWithAccel(distance, accelStraight, accelTurn):
    drive_base.settings(straight_acceleration=accelStraight, turn_acceleration=400)
    drive_base.straight(distance)

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
