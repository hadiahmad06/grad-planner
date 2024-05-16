import pandas as pd
import os
import json

input = os.getcwd() + r"/jake_data.txt"
output = os.getcwd() + r"/data.txt"

def split_nested(str, delimiters): #splits all str values in a string list
    for delimiter in delimiters:
        str = "$".join(str.split(delimiter))
    return str.split("$")

def strip_list(lst): #strips all str values in a string list
    result = []
    if lst != 0:
        for str in lst:
            result.append(str.strip())
    return result

class Course: #Course class 
    def __init__(self, name, location, grades, length, creds, desc, rec, prereqs):
        self.name = name
        self.location = location
        self.grades = grades
        self.length = length
        self.creds = creds
        self.desc = desc
        self.rec = rec
        self.prereqs = prereqs

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

r = open(input)
txt = r.read()
r.close()
idNum = 0;
courses = txt.split("Course Name:")
data = []
for course in courses[1:]:
    temp = strip_list(split_nested(course, ["Location:","Grades:", "Course Duration:", "-long", "Course Description:", "Course Recommendation:", "Prerequisites:", "Additional Registration Information:"]))
    if (temp[3] == "Semester"):
        sems = 1
    elif(temp[3] == "Year"):
        sems = 2
    else:
        sems = -1
    data.append(Course(temp[0], temp[1], temp[2], sems, temp[4], temp[5], temp[6], temp[7]))
    idNum+=1

w = open(output, "w")
jsonText = json.dumps(data)
w.write(jsonText)
w.close()


