import csv

# File to be read
fname = './election_data.csv'

candidateTracker = {}

# Open csv file and create stream
with open(fname, 'r') as csvfile:
    
    # From the stream, create reader object which we'll loop through
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header, but hang onto the info in case we need it
    header = next(csvreader)
    
    for row in csvreader:
        
        if row[2] in candidateTracker:
            
            candidateTracker[row[2]] += 1
            
        else:
            
            candidateTracker[row[2]] = 1

percentages = []
mostVotes = 0

totalVotes = sum(candidateTracker.values())

# Loop through candidates in the dictionary
for i in candidateTracker:

    # Add their percentages to a list
    percentages.append(candidateTracker[i]/totalVotes)

    # Find the winner
    if candidateTracker[i] > mostVotes:
        winner = i
        mostVotes = candidateTracker[i]

print(winner)