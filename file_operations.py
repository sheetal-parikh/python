"""File operation - open and read"""
filename = ("test.txt")
file = open("test.txt", "r")
for line in file:
 print(line)
 
"""Writting into file"""
with open("test.txt","a") as f:
 f.write("\nNew test line")
 f.close()
 #fw.read("test.txt", "r")

"""Print current working directory"""
import os

print(os.getcwd())
print(os.listdir())