import os

inputfile = open(input("Enter the file name you are manipulating include .txt \n"))
outputfile = open(input("Enter the output file name include .txt \n"), "w")
cstrip = input("Enter the characters/words you would like to strip from this file, use commas to seperate them. Strings first, characters second. ").split(",")

print (cstrip)

for aline in inputfile: #executes the removal of specified characters
    for c in cstrip:
        c = c.strip(" ") #strips the space from user input cstrip
        aline = aline.replace(c, "") #replace acts a strip for the string instead of character(s)
    outputfile.write(aline)  #iterates and writes the new information to our outputfile
outputfile.close()
