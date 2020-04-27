###################################
# Title: "Move Over, Van Gogh!"   #
# Programmer: Tabitha Wong        #
# Last modified:  March 27, 2019  #     
###################################
from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="black")
screen.pack()

wh = 100
d = 200
y1 = 0
y11 = 0
for hello in range (8):
    if hello % 2 == 0:
        x1 = 100
        x11 = 0
        colour = "blue"
    if hello % 2 == 1:
        x1 = 0
        x11 = 100
        colour = "red"
    for what in range(4):
        x2=x1+wh
        y2=y1+wh
        screen.create_rectangle(x1,y1,x2,y2, fill = "black")
        for kwcac in range(100):
            size = randint(4,6)
            xd = randint(x1,x2)
            yd = randint(y1,y2)
            screen.create_rectangle(xd,yd,xd+size,yd+size, fill = "blue")   
        x1 = x1 + d    
    for lol in range(4):
        x22 = x11 + wh
        y22 = y11 + wh
        screen.create_rectangle(x11,y11,x22,y22, fill = "black")
        for hlep in range(100):
            size = randint(4,6)
            xdd = randint(x11,x22)
            ydd = randint(y11,y22)
            screen.create_rectangle(xdd,ydd,xdd+size,ydd+size, fill = "red")
        x11 = x11 + d
    y1 = y1 + 100
    y11 = y11 + 100
    
