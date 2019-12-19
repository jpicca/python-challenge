import csv

# File to be read
fname = './election_data.csv'

# Use a dictionary to keep track of the candidates and their votes
candidateTracker = {}

# Open csv file and create stream
with open(fname, 'r') as csvfile:
    
    # From the stream, create reader object which we'll loop through
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header, but hang onto the info in case we need it
    header = next(csvreader)
    
    # Loop through the rows of the reader object
    for row in csvreader:
        
        # Use an if conditional to check if we've found this particular candidate yet
        # If we have, add 1 to their vote count contained in the dictionary
        if row[2] in candidateTracker:
            
            candidateTracker[row[2]] += 1
        
        # If the candidate isn't in the dictionary yet, add them and set their vote count to 1    
        else:
            
            candidateTracker[row[2]] = 1

# Create a variable to keep track of the highest number of votes
mostVotes = 0

# Sum the values from the dictionary to find total votes
totalVotes = sum(candidateTracker.values())

# Create an f-string to add our results to
toPrint = f'Election Results\n' \
            f'-------------------------\n' \
            f'Total Votes: {totalVotes}\n' \
            f'-------------------------\n'

# Loop through candidates to check for winner
for i in candidateTracker:
    
    # Add candidate and their vote percentage/count to f-string
    toPrint += f'{i}: {candidateTracker[i]/totalVotes:.3%} ({candidateTracker[i]})\n'
    
    # Use an if conditional to find winning candidate
    if candidateTracker[i] > mostVotes:
        winner = i
        mostVotes = candidateTracker[i]

# Add winner to f-string        
toPrint += f'-------------------------\n' \
            f'Winner: {winner}\n' \
            f'-------------------------' 

# Print f-string
print(toPrint)

# Write information to a txt file
output = './electionresults.txt'

with open(output, 'w', newline='') as file:

    file.write(toPrint)