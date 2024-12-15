##########################
#     For team 37633     # 
#        DriveBase       #
##########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
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

def IsForceSensorPressed():
    force = ForceSensor(Port.B)
    return force.pressed()

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

def testCustomizedColor():
    Color.LIGHT_GREEN = Color(h=91, s=70, v=76)
    Color.MY_DARK_GREEN = Color(h=154, s=84, v=36)
    Color.LIGHT_BLUE = Color(h=199, s=90, v=76)
    Color.MY_DARK_BLUE = Color(h=218, s=88, v=48)
    Color.MY_ORANGE = Color(h=8, s=75, v=100)
    Color.MY_RED = Color(h=350, s=87, v=62)
    Color.NONE = Color(h=0, s=0, v=0)
    my_colors = ( 
        Color.MY_RED,
        Color.LIGHT_GREEN,
        Color.MY_DARK_GREEN, 
        Color.LIGHT_BLUE, 
        Color.MY_DARK_BLUE,
        Color.YELLOW, 
        Color.WHITE,
        Color.MY_ORANGE,
        Color.NONE)
    color_sensor_side.detectable_colors(my_colors)
    while True:
        print(color_sensor_side.hsv())
        print (color_sensor_side.color())
        wait(60)

testCustomizedColor()

def move_and_leftdown(robot_distance, SetSpeed, armspeed, angle):
    left_motor.run(SetSpeed) 
    right_motor.run(SetSpeed) 
    left_arm.run_target(armspeed, -1 * angle)
    MoveForward(robot_distance)
