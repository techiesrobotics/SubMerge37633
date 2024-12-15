##########################
#     For team 37633     # 
#         Master         #
##########################
from TechiesDriveBase import *
from Run_CollectLeftTree import * #x
from Run_MastHangTree import *
from Run_BudsDiverSharkReef import *
from Run_HangDiverSeabedCollectRight import *
from shippinglanes_octo_segments import *
from sonar_submersible_fish import *
from Run_TridentShark import *

ORANGE_HIGH = 20
ORANGE_LOW = 1
RED_HIGH = 365
RED_LOW = 349
MAGENTA_HIGH = 342
MAGENTA_LOW = 330
BLUE_HIGH = 220
BLUE_LOW = 210
PURPLE_HIGH = 248
PURPLE_LOW = 230
DARK_GREEN_HIGH = 165
DARK_GREEN_LOW = 145
LIGHT_GREEN_HIGH = 90
LIGHT_GREEN_LOW = 100

hub = PrimeHub()
while True:
    detectedHSV = color_sensor_side.hsv()
    detectedColor = color_sensor_side.color()
    print(detectedColor, detectedHSV)

    #TODO:  when to run the mask mission?  
    # Do_MastAndHangTree
    if(detectedColor == Color.GREEN):
        print("==============DarkGreen, Do_CollectLeftTree")
        Do_CollectLeftTree()
    
    elif detectedColor == Color.YELLOW:  # TODO need to test
        #if(detectedHSV.h > LIGHT_GREEN_LOW and detectedHSV.h < LIGHT_GREEN_HIGH):
            print("==============YELLOW, Do_HangDiverSeabedCollectRight")
            Do_HangDiverSeabedCollectRight()

    elif detectedColor == Color.WHITE:  # TODO Need to use a different color
            print("==============YELLOW, Do_MastHangTree")
            Do_MastHangTree()

    elif detectedColor == Color.RED:
        if(detectedHSV.h > RED_LOW and detectedHSV.h < RED_HIGH):
            print("==============RED, Do_BudsDiverSharkReef")
            Do_BudsDiverSharkReef()
        elif(detectedHSV.h > ORANGE_LOW and detectedHSV.h < ORANGE_HIGH): #TODO
            print("==============ORANGE, Run_TridentShark")
            tridentshark()
        elif(detectedHSV.h > MAGENTA_LOW and detectedHSV.h < MAGENTA_HIGH): #TODO
            print("==============MAGENTA, Run_Habitat & sample to boat")
            #Add the run for the Artificial Habitat
        else:
            print("Not Orange, Red, or Magenta")
            print(color_sensor_side.color())
    
    # right side runs
    elif detectedColor == Color.BLUE:
        if(detectedHSV.h > BLUE_LOW and detectedHSV.h < BLUE_HIGH):
            print("==============BLUE, shippinglanes_octo_segments")
            shippinglanes_octo_segments() #TODO add pause mission inbetween
        if(detectedHSV.h > PURPLE_LOW and detectedHSV.h < PURPLE_HIGH):
            print("==============PURPLE, sonar_submersible_fish")
            sonar_submersible_fish()
        else:
            print("========================================too close to tell")
    wait(100)
'''
    elif color_sensor_side.color() == Color.VIOLET:  # TODO
        print(color_sensor_side.color())
'''
        

