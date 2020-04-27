###################################
# Title: "Reuleaux Triangle       #
# Programmer: Tabitha Wong        #
# Last modified:  March 27, 2019  #       
###################################

from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="black")
screen.pack()

screen.create_arc(100,0,700,600,start = 180,extent = -60, fill = "red",outline = "red")
screen.create_arc(-200,0,400,600 , start = 0, extent = 60, fill = "red", outline = "red")
screen.create_arc(-50,-260,550,340, start = 300, extent = -60, fill = "red", outline = "red")

