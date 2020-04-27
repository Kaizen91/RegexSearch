#! /Users/stephenlang/anaconda/bin/python
#regexSearch.py - opens all txt files in a given folder and searches for any line that 
#matches a user-supplied regex.

import sys, os

#get the user supplied regex
userRegex = re.compile(str(sys.argv[1]))

#remove non .txt files in the folder
foldercontents = os.listdir(os.path.abspath('./folder'))
txtRegex = re.compile(r'(.)+(.txt)$')
for i in range(len(foldercontents)):
    mo = txtRegex.search(foldercontents[i])
    if mo == None:
        del foldercontents[i]

#open all the text files in the folder
#break the text into lines. 
#search each line using the regex.
#print the results on the screen.
