import random
import time
import json
from huskylib import HuskyLensLibrary
import RPi.GPIO as GPIO
import xgolib

hl = HuskyLensLibrary("I2C","", address=0x32)
xgo = xgolib.XGO('/dev/ttyS0')

'''
[xgo move command]
    xgo.move_x 
    xgo.move_y 
    xgo.turn   
    xgo.forward
    xgo.back
    xgo.left
    xgo.right
    xgo.turnleft
    xgo.turnright

[xgo action command]
xgo.action(1) = sit
xgo.action(2) = stand
xgo.action(3) = crawl
xgo.action(4) = turn left
xgo.action(5) = turn right
xgo.action(6) = push up
xgo.action(7) = warigari FB
xgo.action(8) = warigari RL
xgo.action(9) = warigari RL2
xgo.action(10) = warigati and twist
xgo.action(11) = pee
xgo.action(12) = see uppeer
xgo.action(13) = arm shake
xgo.action(14) = stretching
xgo.action(15) = wave
xgo.action(16) = warigari dance
xgo.action(17) = sit and warigari dance
xgo.action(18) = ???
xgo.action(19) = hand shake
'''

def printObjectNicely(obj):
    count=1
    
    print("\t "+ ("BLOCK_" if obj.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(obj.__dict__)) # json.dumps relevant file is none. but create in json type in real time
    #print(json.dumps(obj.__dict__)) #json.dumps type == str
    print("x =", obj.x)
    print("y =", obj.y)
    print("ID =", obj.ID)
        
    if obj.ID == 1: # if detected object 1, xgo forward 1 step
        xgo.forward(1)

    elif obj.ID == 2: # if detected object none, xgo left 1 step
        xgo.left(1)

ex = 1  
while(ex == 1):
    try:
        printObjectNicely(hl.getBlocksByID(1)) # print(hl.getBlocksByID(1)) == argument of object id 1, ex)  BLOCK_1 : {"x": 160, "y": 112, "width": 224, "height": 224, "ID": 1, "learned": true, "type": "BLOCK"}
        print(xgo.read_battery)
        time.sleep(0.2)
        
    except KeyboardInterrupt:
        print("\nQUITING")
        quit()
    except :
        #xgo.stop()
        xgo.action(1)
        pass
    # except TypeError:
    #     print("Please enter only a single letter")
    #except Exception as e:
        # General error -> just print it
    #    print(f"Error {e}")
    

