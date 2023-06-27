# Module 3 Challenge Python

# import libraries
import os
import csv

#variable declarations and starting values
rowCount=0
votesTotal=1
votesForCharles=0
votesForDiana=0
votesForRaymon=0
votesPercentForCharles=0
votesPercentForDiana=0
votesPercentForRaymon=0

csvData=[]
# reading csv file
filename="c:/Users/User1/Documents/GitCloned/Module-3-Challenge-Python/PyPoll/Resources/election_data.csv" 
with open(filename, mode='r') as csvFile:
# creating a csv reader object
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        # print(row)
        rowCount += 1
        csvData.append(row)
votesTotal=rowCount-1 # total votes are equal to rowCount-1, -1 because of title row

# collect candidates names only, in another list
candidates=[]
for c in range(rowCount):
    candidates.append(csvData[c][2]) # index [2] which is col 3, is candidate names.

# function for collect items, one at a time in a given list
unique_list = [] # declare variable for a list
def unique():
    for x in candidates:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x) # unique list now have candidate names, 3 names only and title 'Candidate'
    # print list, this section is for testing unique list, which has 3 names in it
    # for x in unique_list:
        # print (x) 
        # unique_list is, ['Candidate', 'Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane'] after checking print out.

unique() # calling function to run, as functions are not running unless called

# vote counts for each candidate
for v in range(rowCount):
    if (unique_list[1]==csvData[v][2]): # unique_list[1] is Charles Casper Stockham
        votesForCharles += 1    
    
    if (unique_list[2]==csvData[v][2]): # unique_list[2] is Diana DeGette
        votesForDiana += 1

    if (unique_list[3]==csvData[v][2]): # unique_list[3] is Raymon Anthony Doane
        votesForRaymon += 1

# find the max votes
maxVotes = max(votesForCharles, votesForDiana, votesForRaymon)
# find the candidate got max votes
if (maxVotes==votesForCharles):
    winner='Charles Casper Stockham'
elif (maxVotes==votesForDiana):
    winner='Diana DeGette'
elif (maxVotes==votesForRaymon):
    winner='Raymon Anthony Doane'

# votesPercent values
votesPercentForCharles = round(100*votesForCharles/votesTotal, 3)
votesPercentForDiana   = round(100*votesForDiana/votesTotal,   3)
votesPercentForRaymon  = round(100*votesForRaymon/votesTotal,  3)

# Output Results, converting numbers to string and add required signs like %, (), etc...
votesTotal      = str(votesTotal)
votesForCharles = str(votesPercentForCharles) + '%   (' + str(votesForCharles) + ')'
votesForDiana   = str(votesPercentForDiana)   + '%   (' + str(votesForDiana)   + ')'
votesForRaymon  = str(votesPercentForRaymon)  + '%   (' + str(votesForRaymon)  + ')'
winner          = str(winner)

# write all output to a string, then this string to be send to: 
# 1) print to terminal and 
# 2) export to a text file

outputStr = ""
outputStr += "----------------------------------------------------------------------"
outputStr += "\n         Module 3 Challenge Python PyPoll - Hikmet Yigit            "
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n"
outputStr += "\n"
outputStr += "\n"
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n                        Election Results                              "
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n"
outputStr += "\n Total Votes                   :" + votesTotal
outputStr += "\n"
outputStr += "\n"
outputStr += "\n Charles Casper Stockham       :" + votesForCharles
outputStr += "\n"
outputStr += "\n"
outputStr += "\n Diana DeGette                 :" + votesForDiana
outputStr += "\n"
outputStr += "\n"
outputStr += "\n Raymon Anthony Doane          :" + votesForRaymon
outputStr += "\n"
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n"
outputStr += "\n Winner                        :" + winner
outputStr += "\n"
outputStr += "\n----------------------------------------------------------------------"

# 1) Output Report to terminal
print(outputStr)

# 2) Output Report to a text file
filename="c:/Users/User1/Documents/GitCloned/Module-3-Challenge-Python/PyPoll/Analysis/Election Results.txt" 
with open(filename, 'w') as txtFile:
    txtFile.write(outputStr)
    
