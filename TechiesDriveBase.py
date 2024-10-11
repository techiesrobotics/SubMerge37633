##########################
#     For team 37633     # 
##########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

#color_sensor = ColorSensor(Port.E)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=110)
drive_base.use_gyro(True)

def SetGyro(truefalse):
    drive_base.use_gyro(truefalse)

def SetSpeed(speed):
    drive_base.settings(straight_speed=speed)

def MoveForward(distance):
    drive_base.straight(distance)

def MoveBackward(distance):
    drive_base.straight(-1* distance)
    
def TurnRight(degrees):
    drive_base.turn(degrees)

def TurnLeft(degrees):
    drive_base.turn(-1* degrees)

def PauseMission():
    print ("starting")
    while Button.LEFT not in hub.buttons.pressed():
        wait(10)
    print ("continue with next step")

'''
MoveForward(200)
PauseMission()
MoveBackward(200)
PauseMission()
TurnRight(90)
PauseMission()
TurnLeft(90)
'''
#TurnRight(90)

#MoveBackward(140)

#MoveForward(100)

#drive_base.hold

#drive_base.coast

#drive_base.brake

#drive_base.coast_smart
