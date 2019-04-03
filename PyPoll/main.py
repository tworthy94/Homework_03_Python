# Modules
import os
import csv

# Path to collect data from the Resources folder
elections = os.path.join('Resources', 'election_data.csv')
electionDataCsv = csv.reader(open(elections))
header = next(electionDataCsv)
# Define Variables
totalVotes = 0
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

# Define candiates list
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
# Loop through the data
for row in electionDataCsv:
    # Find total votes
    totalVotes = totalVotes + 1
    # Count khanVotes
    if row[2] == candidates[0]:
        khanVotes = khanVotes + 1
    # Count correyVotes
    if row[2] == candidates[1]:
        correyVotes = correyVotes + 1
    # Count liVotes
    if row[2] == candidates[2]:
        liVotes = liVotes + 1
    # Count otooleyVotes
    if row[2] == candidates[3]:
        otooleyVotes = otooleyVotes + 1
    # Determine winner
    if khanVotes > correyVotes & khanVotes > liVotes & khanVotes > otooleyVotes:
        winner = "Khan"
    elif correyVotes > khanVotes & correyVotes > liVotes & correyVotes > otooleyVotes:
        winner = "Correy"
    elif liVotes > correyVotes & liVotes > correyVotes & liVotes > otooleyVotes:
        winner = "Li"
    elif otooleyVotes > khanVotes & otooleyVotes > correyVotes & otooleyVotes > liVotes:
        winner = "O\'Tooley"
# Define vote percentages
khanPercent = (khanVotes / totalVotes * 100)
correyPercent = (correyVotes / totalVotes * 100)
liPercent = (liVotes / totalVotes * 100)# Define vote percentages
otooleyPercent = (otooleyVotes / totalVotes * 100)
# Create print function for file output
def resultsFile():
    # Print results
    print(f'Election Results', file=open("PyPollReults.txt", "a"))
    print(f'------------------------', file=open("PyPollReults.txt", "a"))
    print(f'Total Votes: {totalVotes}', file=open("PyPollReults.txt", "a"))
    print(f'------------------------', file=open("PyPollReults.txt", "a"))
    print(f'Khan: {khanPercent:.2f}% ({khanVotes})', file=open("PyPollReults.txt", "a"))
    print(f'Correy: {correyPercent:.2f}% ({correyVotes})', file=open("PyPollReults.txt", "a"))
    print(f'Li: {liPercent:.2f}% ({liVotes})', file=open("PyPollReults.txt", "a"))
    print(f'O\'Tooley: {otooleyPercent:.2f}% ({otooleyVotes})', file=open("PyPollReults.txt", "a"))
    print(f'------------------------', file=open("PyPollReults.txt", "a"))
    print(f'Winner: {winner}', file=open("PyPollReults.txt", "a"))
    print(f'------------------------', file=open("PyPollReults.txt", "a"))
resultsFile()
