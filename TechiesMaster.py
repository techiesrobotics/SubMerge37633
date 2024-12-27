##########################
#     For team 37633     # 
#         Master         #
##########################
from TechiesDriveBase import *
from TechiesArm import *
from Run_MastDiverReefShark import *
from Run_CollectLeftTree import * #x
from Run_BudsDiver import *
from Run_HangDiverSeabedCollectRight import *
from shippinglanes_octo_segments import *
from sonar_submersible_fish import *
from Run_TridentShark import *

RED_HIGH = 365
RED_LOW = 349
ORANGE_HIGH = 20
ORANGE_LOW = 1
MAGENTA_HIGH = 342
MAGENTA_LOW = 330

BLUE_HIGH = 220
BLUE_LOW = 210
LIGHT_BLUE_HIGH = 200
LIGHT_BLUE_LOW = 190
PURPLE_HIGH = 248
PURPLE_LOW = 230

# may not need
#DARK_GREEN_HIGH = 165
#DARK_GREEN_LOW = 145
#YELLOW_HIGH = 60
#YELLOW_LOW = 41

hub = PrimeHub()
while True:
    detectedHSV = color_sensor_side.hsv()
    detectedColor = color_sensor_side.color()
    #print(detectedColor, detectedHSV)

    if(detectedColor == Color.GREEN):
        print("==============DarkGreen, Do_CollectLeftTree")
        Do_CollectLeftTree()
    
    # next is Do_MastHangTree(), move it to light blue

    elif detectedColor == Color.RED:
        if(detectedHSV.h > RED_LOW and detectedHSV.h < RED_HIGH):
            print("==============RED, Do_BudsDiver")
            Do_BudsDiver()
        elif(detectedHSV.h > ORANGE_LOW and detectedHSV.h < ORANGE_HIGH): #TODO
            print("==============ORANGE, Run_TridentShark")
            tridentshark()
        elif(detectedHSV.h > MAGENTA_LOW and detectedHSV.h < MAGENTA_HIGH): #TODO
            print("==============MAGENTA, Run_Habitat & sample to boat")
            MoveRightArmDown(100, 90)
        else:
            print("Not Orange, Red, or Magenta")
            print(color_sensor_side.color())

    elif detectedColor == Color.YELLOW:  # move from left to right
        print("==============YELLOW, Do_HangDiverSeabedCollectRight")
        Do_HangDiverSeabedCollectRight()

    # right side runs + replace white to run mastHangTree
    elif detectedColor == Color.BLUE:
        if(detectedHSV.h > LIGHT_BLUE_LOW and detectedHSV.h < LIGHT_BLUE_HIGH):
            print("==============light blue, Do_MastDiverReefShark")
            Do_MastDiverReefShark()
        elif(detectedHSV.h > BLUE_LOW and detectedHSV.h < BLUE_HIGH):
            print("==============BLUE, shippinglanes_octo_segments")
            shippinglanes_octo_segments() #TODO add pause mission inbetween
        elif(detectedHSV.h > PURPLE_LOW and detectedHSV.h < PURPLE_HIGH):
            print("==============PURPLE, sonar_submersible_fish")
            sonar_submersible_fish()
        else:
            print("======================too close to tell")
    wait(100)

        

