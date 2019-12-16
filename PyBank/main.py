import pandas as pd
import csv

fname = './budget_data.csv'

with open(fname, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
    revenue = 0
    totalChange = 0
    largestIncrease = 0
    largestDecrease = 0
    
    for i, row in enumerate(csvreader):
        #print(f'{i}: {row}')
        revenue += int(row[1])
        
        if i > 0:
            change = int(row[1]) - int(old_row)
            totalChange += change
            
            if change > largestIncrease:
                largestIncrease = change
                monthOfIncrease = row[0]

            if change < largestDecrease:
                largestDecrease = change
                monthOfDecrease = row[0]
            
        #print(int(row[1]) > largestProfit)
        #Before next iteration, save current iteration's revenue to "old row" so we can calculate change
        old_row = row[1]
        
    monthCount = i + 1

    # Subtract 1 from monthCount to get the number of changes
    avgChange = totalChange / (monthCount - 1)

toPrint = f'Financial Analysis\n' \
    f'------------------\n' \
    f'Total Months: {monthCount}\n' \
    f'Total: ${revenue}\n' \
    f'Average Change: ${avgChange:.2f}\n' \
    f'Greatest Increase in Profits: {monthOfIncrease} (${largestIncrease})\n' \
    f'Greatest Decrease in Profits: {monthOfDecrease} (${largestDecrease})\n' 


print(toPrint)

# Printing to Terminal
print('Financial Analysis\n')
print('------------------')
print(f'Total Months: {monthCount}')
print(f'Total: ${revenue}')
print(f'Average Change: ${avgChange:.2f}')
print(f'Greatest Increase in Profits: {monthOfIncrease} (${largestIncrease})')
print(f'Greatest Decrease in Profits: {monthOfDecrease} (${largestDecrease})')