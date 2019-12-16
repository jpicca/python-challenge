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

mostVotes = 0

totalVotes = sum(candidateTracker.values())

toPrint = f'Election Results\n' \
            f'-------------------------\n' \
            f'Total Votes: {totalVotes}\n' \
            f'-------------------------\n'

for i in candidateTracker:
    
    toPrint += f'{i}: {candidateTracker[i]/totalVotes:.3%} ({candidateTracker[i]})\n'
    
    if candidateTracker[i] > mostVotes:
        winner = i
        mostVotes = candidateTracker[i]
        
toPrint += f'-------------------------\n' \
            f'Winner: {winner}\n' \
            f'-------------------------' 

print(toPrint)

# Write information to a txt file
output = './electionresults.txt'

with open(output, 'w', newline='') as file:

    file.write(toPrint)