import pandas as pd
import csv

fname = './budget_data.csv'

with open(fname, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
    revenue = 0
    totalChange = 0
    largestProfit = 0
    largestLoss = 0
    
    for i, row in enumerate(csvreader):
        #print(f'{i}: {row}')
        revenue += int(row[1])
        
        if i > 0:
            totalChange += int(row[1]) - int(old_row)
        
        old_row = row[1]
        
    monthCount = i + 1
    avgChange = totalChange / monthCount


# Debug
print(f'Total Months: {monthCount}')
print(f'Total Revenue: {revenue}')
print(f'Average Change: {avgChange}')