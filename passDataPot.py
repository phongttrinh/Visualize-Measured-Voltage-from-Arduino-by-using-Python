#Author: Thanh Phong Trinh (TPT)

from importlib.resources import path #import the libary to use path in cut extrude
import time #
from tkinter import CENTER #import the libary to use align CENTER
import serial # this libary allows us collect data from arduino
import numpy as np # this libary allows to use caculation process
from vpython import * # this libary allows to make a 3-D shapes ...
arrowLength = 1
arrowWidth =.02
caseX = 2.5
caseY = 2
caseZ = .1
hubL = 0.03
hubR = 0.05
tickW = 0.02
tickL = 0.1
tickH = 0.01
minorTickL = 0.05
minorTickW = 0.005
minorTickH = 0.01
cnt = 0
numX = 1
numY = 1
numZ = 0.1
caseFactorX = 1.1
caseFactorY = 2
caseFactorZ = 4.5
labFactor = 1.12
butL = 0.1
butR = 0.6
# This part is to design components of Voltage Meter using Vpython
myArrow = arrow(length = arrowLength, shaftwidth = arrowWidth, color = color.red) 
myHub = cylinder(color =color.red, length = hubL, radius = hubR, axis = vector(0,0,1))
myScreen = box(color=color.white,size = vector(caseX,caseY,caseZ), pos = vector(0,caseY/2-0.2,-caseZ))
myCase = box(color = color.yellow, roundness = 0.1, size = vector(caseFactorX*caseX, caseFactorY*caseY, caseFactorZ*caseZ), pos = vector(0,0,-3.5*caseZ))
myGlassCover = box(color=color.white,opacity = 0.3, size = vector(caseX,caseY,caseZ), pos = vector(0,caseY/2-0.2,0))
myScreenSeal = box(color=color.black, size = vector(1.05*caseX,caseY*1.05,caseZ), pos = vector(0,caseY/2-0.2,-1.1*caseZ))
myButton = cylinder(color = color.white,length = butL, radius = butR, pos = vector(0,-1.2,-0.15), axis = vector(0,0,1))
myBar = box(color=color.red,size = vector(0.15,0.7,0.3), pos = vector(0,-1.2,-0.1), axis = vector(0.9,1.5,0))
myButtonSeal = extrusion(path =[vector(0,0,0), vector(0,0,-0.05)],color = color.black, shape=shapes.circle(radius = 0.65, thickness = 0.25),pos = vector(0,-1.2,-0.1))
myComSocket = extrusion(path = [vector(0,0,0), vector(0,0,-0.09)], color=color.black, shape = shapes.circle(radius = 0.1,  thickness = 0.76), pos = vector(0.85,-1.7,-0.1))
myComSocketSeal = extrusion(path = [vector(0,0,0), vector(0,0,-0.05)], color=color.red, shape = shapes.circle(radius = 0.12,thickness = 0.7), pos = vector(0.85,-1.7,-0.1))
myVolSocket = extrusion(path = [vector(0,0,0), vector(0,0,-0.09)], color=color.black, shape = shapes.circle(radius = 0.1,  thickness = 0.76), pos = vector(1.15,-1.7,-0.1))
myVolSocketSeal = extrusion(path = [vector(0,0,0), vector(0,0,-0.05)], color=color.red, shape = shapes.circle(radius = 0.12,thickness = 0.7), pos = vector(1.15,-1.7,-0.1))

#Note: using for loop and linspace to make major ticks
for alpha in np.linspace(np.pi/6,np.pi*5/6,6):
    myTickMajor = box(color=color.black, size = vector(tickL, tickW, tickH), pos = vector(arrowLength*np.cos(alpha),arrowLength*np.sin(alpha),0), axis = vector(arrowLength*np.cos(alpha), arrowLength*np.sin(alpha),0))

#Note: using for loop and linspace to make major ticks
for alpha in np.linspace(np.pi*5/6,np.pi/6,51):
    myTickMinor = box(color=color.black, size = vector(minorTickL, minorTickW, minorTickH), pos = vector(arrowLength*np.cos(alpha),arrowLength*np.sin(alpha),0), axis = vector(arrowLength*np.cos(alpha), arrowLength*np.sin(alpha),0))

#Note: using for loop and linspace to name those major ticks
for alpha in np.linspace(np.pi/6,np.pi*5/6,6):
    lab = text(text=str(cnt),color= color.black, height = 0.12, pos = vector(labFactor*arrowLength*np.cos(alpha),labFactor*arrowLength*np.sin(alpha),0), align = CENTER,axis = vector(arrowLength*np.cos(alpha - np.pi/2), arrowLength*np.sin(alpha-np.pi/2),0))
    cnt=cnt+1

#Note: using for loop and linspace to make small points on button 
for alpha in np.linspace(np.pi/9,np.pi*8/9,2):
    mySphere = sphere(color=color.black, radius =0.03, pos = vector(0.4*np.cos(alpha),0.4*np.sin(alpha) - 1.1,-0.05))

#Note: using for loop and linspace to name the right point
for alpha in np.linspace(np.pi/9,np.pi*8/9,1):
    lab = text(text = 'OFF', color =color.red, height = 0.055, pos = vector(0.45*np.cos(alpha),0.45*np.sin(alpha) - 1.1,-0.05),align = CENTER, axis = vector(0.4*np.cos(alpha - np.pi/2),0.4*np.sin(alpha- np.pi/2),0))

#Note: using for loop and linspace to name the left point    
for alpha in np.linspace(np.pi*8/9, np.pi/9,1):
    lab = text(text = 'ON', color =color.red, height = 0.055, pos = vector(0.45*np.cos(alpha),0.45*np.sin(alpha) - 1.1,-0.05),align = CENTER, axis = vector(0.4*np.cos(alpha - np.pi/2),0.4*np.sin(alpha- np.pi/2),0))

#Lable those components by using text in vPython
myLabel = text(text ='TPT Voltage Meter', color = color.red, pos = vector(0,1.54,0), height =0.16,align = CENTER)
myMainLabel = text(text ='TPT Voltage Meter', color = color.red, pos = vector(0,1.54,0), height =0.16, align = CENTER)
myComLable = text( text ='COM', color = color.red, height = 0.06, pos = vector(0.85,-1.9,-0.1), align = CENTER)
myVolLable = text(text= 'Volt', color= color.red, height = 0.06, pos = vector(1.15,-1.9,-0.1), align = CENTER)
myConnerLable = text(text ='Only DC Current', color = color.red, height = 0.07, pos = vector(-1.3,-1.9,-0.1))

#This part allows collect data from Arduino to Python
arduinoData = serial.Serial('com4',9600) # collect data from Com4 of Ardunino with baud rate 9600
time.sleep(1) # delay 1 second
while True:  
    while(arduinoData.inWaiting()==0): # while data == 0, pass
        pass
    dataPacket = arduinoData.readline() # read line by line data of 'arduinoData' and  store them in dataPacket
    dataPacket = str(dataPacket,'utf-8') # convert dataPacket from num to strings
    dataPacket = int(dataPacket.strip('\r\n')) # edit line of dataPacket to make it neat by strip \r\n off the end of the line
    voltVal = (dataPacket*(5./1023.)) # convert data to voltage
    voltVal = round(voltVal,1) # round the data to 1 decimal place
    theta = ((-2./3069.)*np.pi)*dataPacket + np.pi*5/6 #convert data to angle to be able adjust the arrow following the change in voltage
    myArrow.axis =  vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0) # adjust postion of the tip's arrow following theta
