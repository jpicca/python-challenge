import pandas as pd
import csv

# File to be read
fname = './budget_data.csv'

# Open csv file and create stream
with open(fname, 'r') as csvfile:

    # From the stream, create reader object which we'll loop through
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header, but hang onto the info in case we need it
    header = next(csvreader)

    # Initialize some variables that we'll use in our upcoming loop
    revenue = 0
    totalChange = 0
    largestIncrease = 0
    largestDecrease = 0
    
    # Loop through the reader object
    for i, row in enumerate(csvreader):
        
        # Add each row's profit to a total we keep track of
        revenue += int(row[1])
        
        # Once we move pass the first row of data, we can calculate the change
        if i > 0:

            # Subtract the prior row from the current row
            change = int(row[1]) - int(old_row)

            # Add this change to a total change, which we'll use to calc an average
            totalChange += change
            
            # Check if this change is the most positive change yet
            # If so, update our variable
            if change > largestIncrease:
                largestIncrease = change
                monthOfIncrease = row[0]

            # Check if this change is the most negative change yet
            # If so, update our variable
            if change < largestDecrease:
                largestDecrease = change
                monthOfDecrease = row[0]
            
        #Before next iteration, save current iteration's revenue to "old row" so we can calculate change
        old_row = row[1]
    
    # Create a month count variable from the index (but add 1 since i was 0-indexed)
    monthCount = i + 1

    # Calculate the average change
    # We subtract 1 from monthCount to get the number of changes
    avgChange = totalChange / (monthCount - 1)

# Create a multiline f-string to both print and save to a txt file
toPrint = f'Financial Analysis\n' \
    f'------------------\n' \
    f'Total Months: {monthCount}\n' \
    f'Total: ${revenue}\n' \
    f'Average Change: ${avgChange:.2f}\n' \
    f'Greatest Increase in Profits: {monthOfIncrease} (${largestIncrease})\n' \
    f'Greatest Decrease in Profits: {monthOfDecrease} (${largestDecrease})\n' 

# Print to terminal
print(toPrint)

# Write information to a txt file
output = './financialanalysis.txt'

with open(output, 'w', newline='') as file:

    file.write(toPrint)