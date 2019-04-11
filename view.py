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

        self.days_label = Label(master, text="Days")
        self.days_label.grid(column=3, row=ceOffset)

        self.priority_label = Label(master, text = "Priority: ")
        self.priority_label.grid(column = 0, row = ceOffset + 3)

        self.priority_box = Entry(master)
        self.priority_box.grid(column = 1, row = ceOffset + 3)

        self.number_box = Entry(master)
        self.number_box.grid(column=0, row= ceOffset+1)

        self.start_box = Entry(master)
        self.start_box.grid(column=1, row=ceOffset + 1)

        self.end_box = Entry(master)
        self.end_box.grid(column=2, row= ceOffset + 1)

        self.days_box = Entry(master)
        self.days_box.grid(column=3, row = ceOffset +1)

        self.start2_box = Entry(master)
        self.start2_box.grid(column=1, row=ceOffset + 2)

        self.end2_box = Entry(master)
        self.end2_box.grid(column=2, row= ceOffset + 2)

        self.days2_box = Entry(master)
        self.days2_box.grid(column=3, row = ceOffset +2)

        self.greet_button = Button(master, text="Add", command=self.addClass)
        self.greet_button.grid(column=2, row= ceOffset +3)


    def addClass(self):
        data = {}
        data["number"] = self.number_box.get()
        data["priority"] = int(self.priority_box.get())
        data["times"] = []
        

        #day box one
        for day in self.days_box.get():
            dayData = {}
            dayData["day"] = day
            dayData["start"] = self.parseTime(self.start_box.get())
            dayData["end"] = self.parseTime(self.end_box.get())

            data["times"].append(dayData)

        #day box two
        if self.days2_box.get() != '':
            for day in self.days2_box.get():
                dayData = {}
                dayData["day"] = day
                dayData["start"] = self.parseTime(self.start2_box.get())
                dayData["end"] = self.parseTime(self.end2_box.get())

                data["times"].append(dayData)

        newCourse = schedge.course(data)
        my_addToJson(self.json_box.get(), newCourse)

    def parseTime(self, tString):
        #turns a time in format (11:45AM) into mpm

        ampm = ""
        hours = ""
        minutes = ""
        switch = False
        ampm = tString[-2:].lower()

        #remove ampm
        tString = tString[:-2]

        for char in tString:
            if switch == True:
                #minutes
                minutes += char
            elif char == ":":
                switch = True
            else:
                hours += char

        hours = int(hours)
        minutes = int(minutes)

        if ampm == "am":
            return (60 * hours) + minutes
        else:
            return (12 * 60) + (60 * hours) + minutes


def my_addToJson(inFile, inCourse):
    #copy of function from schedge, but had very strange broken behavior when it was calling that one
    #not sure why
    #TODO: Fix addToJson
    try:
        newData = json.load(open(inFile))
        print("loaded ", inFile)
    except json.JSONDecodeError:
        print("Not a json file")
        return 0

    try:
        newData["lineItems"].append(inCourse.data)
    except:
        newData["lineItems"] = []
        newData["lineItems"].append(inCourse.data)


    with open(inFile, 'w') as outfile:
        print("dumping json")
        json.dump(newData, outfile, indent=4)

    return 1 


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()