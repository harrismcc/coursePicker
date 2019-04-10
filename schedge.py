import json
import sys, getopt



class time:
    def __init__(self, minutes):
        #military time, stored as minutes since midnight
        self.minutes = minutes

    def __lt__(self, other):
        #self is less than other
        return self.minutes < other.minutes
    
    def __le__(self, other):
        #self is <= other
        return self.minutes <= other.minutes

    def __gt__(self, other):
        #self is > other
        return self.minutes > other.minutes

    def __ge__(self, other):
        #self is >= other
        return self.minutes >= other.minutes

    def __eq__(self, other):
        #self is == other
        return self.minutes == other.minutes

    def getMins(self):
        return self.minutes

    def __str__(self):
        #creates string of time
        hours = self.minutes // 60
        minutes = self.minutes - (60 * hours)   
        return str(hours) + ":" + str(minutes).zfill(2) 
    def __repr__(self):
        return str(self)   

class course:
    def __init__(self, classJson):
        self.data = classJson
        self.number = classJson["number"]
        self.priority = classJson["priority"]

    def conflicts(self, other):
        for s in self.data["times"]:
            for o in other.data["times"]:

                if s["day"] == o["day"]:
                    if o["start"] >= s["start"] and o["start"] <= s["end"]:
                        return True
                    elif o["end"] >= s["start"] and o["end"] <= s["end"]:
                        return True
        return False

    def __str__(self):
        final = self.number + " : "

        for i in self.data["times"]:
            final += i["day"] + " "
            final += str(i["start"]) + "-"
            final += str(i["end"]) + ", "
        
        return final

    def __repr__(self):
        return str(self)





def inFromJson(inFile):
    sch = json.load(open(inFile))
    totalClasses = []
    

    for item in sch["lineItems"]:
        
        totalClasses.append(course(item))
    
    return totalClasses

def toJson(course):
    

def addToJson(inFile, inCourse):
    try:
        newData = json.load(open(inFile))
    except json.JSONDecodeError:
        print("Not a json file")
        return 0

    try:
        newData["lineItems"].append(inCourse.data)
    except:
        newData["lineItems"] = []
        newData["lineItems"].append(inCourse.data)


    with open('test2.json', 'w') as outfile:
        json.dump(newData, outfile, indent=4)

    return 1

