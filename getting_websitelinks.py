import re

filename = input("Enter the filename(without txt): ")
fullpathname = "Website/" + filename + ".txt"
newpathfile = "Website/outputs/" + filename + "_output.txt"
fileToOpen = open(fullpathname)
fileToWrite = open(newpathfile, "w")
lines = fileToOpen.readlines()

for line in lines:
    if re.match("https://", line):
        fileToWrite.write(f"{line}\n")