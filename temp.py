from pypdf import PdfReader 

reader = PdfReader('ProgramOfStudies.pdf') 

feed = ""
for page in reader.pages:
    print(page.extract_text() + "\n\n\n")
    
print(feed)

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



