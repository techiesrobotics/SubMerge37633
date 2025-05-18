###############################
#        For team 37633       #
#       TechiesMaster.py      #
#  This file starts the runs  #
###############################
from TechiesDriveBase import *
from Run_CollectLeft import *
from sonar_submersible_fish import *
from Run_TestLeftSideFull import *
from Run_ArtificialHabitatAndResearchVessel import *
from Run_CollectSamples import *
from shippinglanes_octo_segments import *
from feedthewhale import *
from tridentgray import *

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

while True:
    detectedHSV = color_sensor_side.hsv()
    detectedColor = color_sensor_side.color()
    #print(detectedColor, detectedHSV)

    if(detectedColor == Color.GREEN):
        print("==============Green, Run_LeftToRight2")
        trident()

    elif detectedColor == Color.RED:
        # Pybricks's pre-defined colors mixes up red, orange and magenta.
        # So we used the hue of the color to detect the colors more accurately.

        if(detectedHSV.h > RED_LOW and detectedHSV.h < RED_HIGH):
            print("==============Red, Do_CollectLeft")
            Do_TreeBudsShark
        elif(detectedHSV.h > ORANGE_LOW and detectedHSV.h < ORANGE_HIGH):
            print("==============Orange, Do_BudsDiverSharkReef")
            Run_ArtificialHabitatAndResearchVessel()
        elif(detectedHSV.h > MAGENTA_LOW and detectedHSV.h < MAGENTA_HIGH):
            print("==============MAGENTA, Run_Habitat & sample to boat")
            collectSamples()
        else:
            print("Not Orange, Red, or Magenta")
            print(color_sensor_side.color())

    elif detectedColor == Color.YELLOW:
        print("==============YELLOW, Do_MastKrakenReefDiver")
        Do_MastKrakenReefDiver()

    elif detectedColor == Color.BLUE:
        # Pybricks's pre-defined colors mixes up blue, purple, light blue.
        # So we used the hue of the color to detect the colors more accurately.
        if(detectedHSV.h > LIGHT_BLUE_LOW and detectedHSV.h < LIGHT_BLUE_HIGH):
            print("==============LIGHT_BLUE, submersible_octo")
            feedthewhale()
        if(detectedHSV.h > BLUE_LOW and detectedHSV.h < BLUE_HIGH):
            print("==============BLUE, shippinglanes_octo_segments")
            shippinglanes_octo()
        elif(detectedHSV.h > PURPLE_LOW and detectedHSV.h < PURPLE_HIGH):
            print("==============PURPLE, sonar_submersible_fish")
            sonar_submersible_angler_octo()
        else:
            print("======================too close to tell")
    wait(100)
