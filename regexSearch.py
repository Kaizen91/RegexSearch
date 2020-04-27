#! /Users/stephenlang/anaconda/bin/python
#regexSearch.py - opens all txt files in a given folder and searches for any line that 
#matches a user-supplied regex.

import sys, os, re

#get the user supplied regex
userRegex = re.compile(str(sys.argv[1]))

#remove non .txt files in the folder
foldercontents = os.listdir(os.path.abspath('./folder'))
txtRegex = re.compile(r'(.)+(.txt)$')
for content in foldercontents:
    mo = txtRegex.search(content)
    if mo == None:
        foldercontents.remove(content)

#open all the text files in the folder

for string in foldercontents:
    txtFile = open("./folder/"+ string)
    #break the text into lines. 
    fileLines = txtFile.readlines()
    #search each line using the regex.
    for line in fileLines:
        mo = userRegex.findall(line)
        if len(mo) != 0:
            #print the results on the screen.
            print('Result found in ' +string +': ' + ' '.join(mo))
                 






