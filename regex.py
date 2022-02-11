import re

txt = "The rain in India"

#search word starting with The and ending with India
x = re.search("^The.*India$", txt)
print(x)

y = re.findall("India", txt)
print(y)

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
txt1 = "hello heppo planet"
x1 = re.findall("he.{2}o", txt1)
print(x1)

#Check if the string contains either "falls" or "stays":
txt2 = "The rain in Spain falls mainly in the plain!"

x = re.findall("falls|stays", txt2)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

