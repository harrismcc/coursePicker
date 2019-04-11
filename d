import tkinter
import schedge
import json
import sys, getopt
from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Class Json Editor")


        ##JSON FILE NAME ENTRY##
        self.json_label = Label(master, text="Json Filename: ")
        self.json_label.grid(column=0, row=0)

        self.json_box = Entry(master)
        self.json_box.grid(column=1, row = 0)

        self.json_button = Button(master, text="Enter", command = self.loadRest(master))
        self.json_button.grid(column = 3, row = 0)

    def loadRest(self, master):
        ##ADD CLASS ENTRY
        ceOffset = 3

        self.label = Label(master, text="Add Entry")
        self.label.grid(column=1, row=1)

        self.number_label = Label(master, text="Course No.")
        self.number_label.grid(column = 0, row = ceOffset)

        self.start_label = Label(master, text="Start Time")
        self.start_label.grid(column = 1, row= ceOffset)

        self.end_label = Label(master, text="End Time")
        self.end_label.grid(column = 2, row= ceOffset)

        self.number_box = Entry(master)
        self.number_box.grid(column=0, row= ceOffset+1)

        self.start_box = Entry(master)
        self.start_box.grid(column=1, row=ceOffset + 1)

        self.end_box = Entry(master)
        self.end_box.grid(column=2, row= ceOffset + 1)

        self.greet_button = Button(master, text="Add", command=self.addClass)
        self.greet_button.grid(column=2, row= ceOffset +2)


    def addClass(self):
        return 1
        

    def addItemToJson(self, json, item):
        schedge.addToJson(json, item)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()