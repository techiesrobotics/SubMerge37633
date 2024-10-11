##########################
#     For team 37633     # 
##########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
hub = PrimeHub()

selected = hub_menu(1,2,3,4)

if selected == 1:
    import Run1


