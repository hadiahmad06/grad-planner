from pypdf import PdfReader
import pickle

reader = PdfReader('ProgramOfStudies.pdf') 

credits = {} #graduation requirements base
credits["Arts"] = 2
credits["Elective Requirement"] = 13
credits["Personal Finance"] = 1
credits["English"] = 8
credits["Math"] = 6
credits["Physical Education/Health"] = 2
credits["Science"] = 2

name_dict = {}
grades_dict = {}
length_dict = {}
cred_dict = {}
prereq_dict = {}

def append_dict(dict, key, value):
    if key in dict.keys() and dict[key] != None:
        dict[key] = dict[key].append(value)
    else:
        dict[key] = [value]
        

class Course: #Course class 
    def __init__(self, name, grades, length, creds = [], desc = "", rec = "", prereqs = []):
        self.name = name
        self.grades = grades
        self.length = length
        self.creds = creds
        self.desc = desc
        self.rec = rec
        self.prereqs = prereqs
        
        append_dict(name_dict, name, self)
        append_dict(grades_dict, grades, self)
        append_dict(length_dict, length, self)
        for cred in creds:
            append_dict(cred_dict, cred, self)
        for prereq in prereqs:
            append_dict(prereq_dict, prereq, self)

            
            

    def __str__(self): #converts to string
        credits = ""
        for i in self.creds[:-1]:
            credits += i + " + "
        credits += self.creds[-1]
        prerequisites = ""
        for i in self.prereqs[:-1]:
            prerequisites += i + " or\n"
        prerequisites += self.prereqs[-1]
        return "Course Name:\n" + self.name + "\n\n" + str(self.length) + " semesters\n\nFulfills: " + credits + "\n\nCourse Description: \n" + self.desc + "\n\nCourse Recommendation:\n" + self.rec + "\n\nPrerequisites:\n" + prerequisites+"\n\n\n\n\n\n\n\n\n\n"

courses = []

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

skip_pages = [40,41,49,52,53,64,65,70,71,80,81,91]
#pages that should be skipped, not necessary

feed = ""
for i in range(131,155):#(32, 39):#163): #checks all grad requirements
    feed += reader.pages[i].extract_text()
        
while "Additional" in feed:  
    try:
        breaks = ["Grades:", "Course Duration:", "Fulfills", "Prerequisite:", "Course Description:", "Course Recommendation:"]
        temp = feed.split("Additional")
        feed = "Additional".join(temp[1:])
        txt = split_nested(temp[0], breaks)
        name = split_nested(txt[0], ["In-Person","Hybrid","Online","Contents","course.","None", "."])[-1]
        grades = txt[1]
        if "Year-long" in txt[2]:
            length = 2
        elif "Semester-long" in txt[2]:
            length = 1
        else:
            length = -1
        creds = strip_list("".join(txt[3].split("for")[0]).split(" or "))
        prereq = strip_list("".join("".join(txt[4].split(";"))).split(" or "))
        if "None" in txt[4]:
            prereq = ["None"]
        desc = txt[5]
        rec = txt[6].split("Board")[0]
        courses.append(Course(name, grades, length, creds, desc, rec, prereq))
    except IndexError as e:
        print("Index Error on page "+ str(i))

with open ('course_data.pickle', 'wb') as file:
    pickle.dump(courses, file)

f = open ('course_data.txt', 'w')
for course in courses:
    f.write(str(course))
f.close()

n=0
for course in courses:
    n+=1

print(n)
# dictionaries = [name_dict,grades_dict,length_dict,cred_dict,prereq_dict]
# for dict in dictionaries:
#     for key in dict.keys():
#         print(str(key)+"\n")
#         if dict[key] != None:
#             for item in dict[key]:
#                 print(item.name +" + ")
    




# old code for testing
    

# for i in range(len(reader.pages)): # FINDS TABLE OF CONTENTS
#     toc = reader.pages[i].extract_text().split("\n")
#     if toc[0] == ("Table of Contents"):
#         break

# index = []
# toc = (reader.pages[i].extract_text() + "\n" + reader.pages[i+1].extract_text()).split("\n")
# for line in toc: # ASSIGNS EACH PAGE TO A NUMBER
#     info = line.split(" ")
#     try: index.append((" ".join(info[:-1]), int(info[-1])))
#     except: index.append((" ".join(info[:-1]), None))

# def get_idx(str):
#     for i in range(len(index)):
#         (a, _) = index[i]
#         if a == str:
#             return i

# def strToText( str):
#     reader.pages[get_idx(str)].extract_text()

# def idxToText( idx):
#     reader.pages[idx].extract_text()

# feed = strToText("Graduation Requirements")

# courses = "\n\n".join([])

