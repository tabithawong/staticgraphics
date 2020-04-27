###################################
# Title: "Spring is here!"        #
# Programmer: Tabitha Wong        #
# Last modified:  March 27, 2019  #    
###################################

from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=700, background="lightslateblue")
screen.pack()

#WALL PATTERN
x = 0
brickwidth = 100
brickheight = 50

distance = 100
y1 = 0
y2 = 50
y = 50
for lol in range(16):
    if lol % 2 == 1:
        x = brickwidth/2
    y2 = y1 + brickheight
    for f in range(8):
        screen.create_line(x, y1, x, y2, fill = "purple", width = 3)
        x = x + brickwidth
    x = 0
    y1 = y1 + brickheight

for haha in range (16):
    screen.create_line(x,y,x+800,y, fill = "purple", width = 3)
    y = y + 50

#WINDOW
screen.create_rectangle(150, 100, 650, 350, fill="white", width = 3)
screen.create_rectangle(175, 125, 625, 325, fill="skyblue", width = 3)
screen.create_arc(75, 25, 275, 225, start=0, 
    extent=-90, fill="yellow")
screen.create_rectangle(563,200,625,325, fill = "tan4")
screen.create_rectangle(536,125,625,200, fill = "springgreen4", outline = "springgreen4")
screen.create_oval(555,175,625,210, fill = "springgreen4",outline = "springgreen4")
screen.create_oval(515,155,565,200, fill = "springgreen4", outline = "springgreen4")
screen.create_oval(505,125,565,170, fill = "springgreen4", outline = "springgreen4")


#TABLE
screen.create_rectangle(50, 480, 750, 550, fill = "white")
screen.create_rectangle(50, 550, 100, 700, fill = "white")
screen.create_rectangle(700, 550, 750, 700, fill = "white")

#CLOCK RADIO
screen.create_rectangle(75,430,200,480, fill = "thistle2")
screen.create_rectangle(85, 440, 190,470, fill = "grey65")
screen.create_line(138,430,106,400,width = 2)
screen.create_line(138, 430,169,400,width = 2)
screen.create_oval(106,400,111,405, fill = "black")
screen.create_oval(165,400,170,405, fill = "black")
h = randint(5,11)
m = randint(1,59)
if m < 10:
    screen.create_text(138,455,text = str(h)+":0"+str(m)+ " AM", font = "Fixedsys 14", fill = "lawngreen")

else:
    screen.create_text(138,455,text = str(h)+":"+str(m)+ " AM", font = "Fixedsys 14", fill = "lawngreen")

#CHAIR
screen.create_rectangle(425,650,475,700, fill = "RosyBrown4", width = 2)
screen.create_polygon(350,510,350,690,550,690,550,510, smooth = True, fill = "RosyBrown4", outline = "black", width = 2)

#CHAIR COLOUR PATTERN
for dog in range (75):
    l = randint(375,525)
    n = randint(550,650)
    size = randint(1,2)
    screen.create_oval(l,n,l+size,n+size, fill = "RosyBrown2", outline = "RosyBrown2")

#COMPUTER AND KEYBOARD
screen.create_rectangle(300, 275, 600, 425, fill="thistle2")
screen.create_rectangle(310,285,590,415, fill ="grey65")
screen.create_rectangle(425, 425, 475, 480, fill="thistle2")
screen.create_rectangle(325, 460, 575, 480, fill = "thistle2")
screen.create_rectangle(375, 310, 525, 390, fill = "white", width = 2)
screen.create_line(375,320,525, 320, width = 2)
screen.create_line(515, 313,520, 317, fill = "firebrick4", width = 2)
screen.create_line(515,317,520,313, fill = "firebrick4", width = 2)
screen.create_text(450,335, text = "WEATHER REMINDER:", font = "Times 10")
screen.create_text(450,360, text = "It's the first day of Spring!", font = "Times 8")
screen.create_text(450,370, text = "Say hello to the sun!", font = "Times 8")

#GRID LINES
##spacing = 50
##for x in range(0, 1000, spacing): 
##    screen.create_line(x, 25, x, 1000, fill="blue")
##    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)
##
##for y in range(0, 1000, spacing):
##    screen.create_line(25, y, 1000, y, fill="blue")
##    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)


