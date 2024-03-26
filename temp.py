from pypdf import PdfReader 

reader = PdfReader('ProgramOfStudies.pdf') 

feed = ""
# for page in reader.pages:
#     print(page.extract_text() + "\n\n\n")
    
print(feed)
credits = {}
credits["Arts"] = 2
credits["Electives"] = 13
credits["Personal Finance"] = 1

class Course:
    def __init__(self, name, length, creds = [], desc = "", rec = "", prereq = []):
        self.name = name
        self.length = length
        self.creds = creds
        self.desc = desc
        self.rec = rec
        self.prereq = prereq

    def print(self):
        credits = ""
        for i in self.creds:
            credits += i + ", "
        prerequisites = ""
        for i in self.prereq:
            prerequisites += i + ", "
        print(self.name + "\n\n" + str(self.length) + " semesters\n\nCovers " + credits + "\n\nCourse Description: \n" + self.desc + "\n\nCourse Recommendation:\n" + self.rec + "\n Prerequisites: " + prerequisites)

courses = []
#courses.append(Course("AP CALC BC & Advanced Topics", 2, ["art + electives"], "DESCRIPTPUON HERE CLASS IS CALC BV"))

#courses[0].print()
def split_nested(str, delimiters):
    for delimiter in delimiters:
        str = "$".join(str.split(delimiter))
 
    return str.split("$")
    # split_nested_helper([str], breaks)

# def split_nested_helper(lst, breaks):
#     if len(lst) != 0:
#         result = []
#         for str in lst:
#             if (len(breaks) == 1):
#                 result.append(str.split(breaks[0]))
#             else:
#                 result.append(split_nested_helper(str.split(breaks[0]), breaks[1:]))
#         print(result)
#         return result
#     else:
#         return lst


for i in range(32,33):#range(32, 200):
    #print(reader.pages[i].extract_text())
    breaks = ["Grades:", "Course Duration:", "Fulfills", "Prerequisite:", "Course Description:", "Course Recommendation:"]
    txt = split_nested(reader.pages[i].extract_text(), breaks)
    name = txt[0].split("Contents")[1]
    if "Year-long" in txt[1]:
        length = 2
    elif "Semester-long" in txt[1]:
        length = 1
    else:
        length = -1
    creds = " ".join(txt[3].split("\n")).split("or")
    prereq = " ".join(txt[4].split("\n")).split("or")
    desc = txt[5]
    rec = txt[6].split("Board")[0]
    courses.append(Course(name, length, creds, desc, rec, prereq))

for course in courses:
    course.print()





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



