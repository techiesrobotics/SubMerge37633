##########################
#     For team 37633     # 
##########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
hub = PrimeHub()

selected = hub_menu(0,1,2,3,4)

if selected == 0:
    import Run_CollectLeft
elif selected == 1:
    import Run_MastKraken



