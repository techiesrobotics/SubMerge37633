##########################
#     For team 37633     # 
#         Master         #
##########################
from TechiesDriveBase import *
from TechiesArm import *
from Run_CollectLeftTree import *
from Run_MastHangTree import *
from Run_BudsDiverSharkReef import *
from Run_MastHangTree import *
from Run_HangDiverSeabedCollectRight import *

hub = PrimeHub()
while True:
    if color_sensor_side.color() == Color.GREEN:
        print(color_sensor_side.color())
        Do_CollectLeftTree()
        
    elif color_sensor_side.color() == Color.BLUE: #need customized color 4 replacement
        print(color_sensor_side.color())
        Do_MastHangTree()
        
    elif color_sensor_side.color() == Color.RED:
        print(color_sensor_side.color())
        Do_BudsDiverSharkReef()
    
    elif color_sensor_side.color() == Color.YELLOW:
        print(color_sensor_side.color())
        Do_HangDiverSeabedCollectRight()
        
    #elif color_sensor_side.color() == Color.BLUE:
    #    print(color_sensor_side.color())
    #    shippinglanes_octo()

    elif color_sensor_side.color() == Color.VIOLET:
        print(color_sensor_side.color())
        sonar_submersible_fish()
    elif color_sensor_side.color() == Color.ORANGE:
        print(color_sensor_side.color())
        send_coral_segments()
    elif color_sensor.color() == Color.BLACK:
        print(color_sensor_side.color())
        sonar_submersible_fish()