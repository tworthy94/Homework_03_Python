# Modules
import os
import csv

# Path to collect data from the Resources folder
infile = os.path.join('Resources', 'budget_data.csv')
budgetDataCsv = csv.reader(open(infile))
header = next(budgetDataCsv)
# Define Variables
months = []
totalMonths = 0
netTotal = 0
profitLoss = []
profitLossStepped = []
    # Loop through the data
for row in budgetDataCsv:
    # Find total months in spreadsheet
    totalMonths = totalMonths + 1
    #Caluclating total profit
    netTotal= netTotal + int(row[1])
    # Append months list
    months.append(row[0])
    # Append profit/loss lists
    profitLoss.append(int(row[1]))
    profitLossStepped.append(int(row[1]))
# Deleting first entry of lists
del(months[0])
del(profitLoss[len(months)])
del(profitLossStepped[0])
# Populating the list for changes in profit/loss
change = [x - y for x, y in zip(profitLossStepped,profitLoss)]
totalChange=sum(change)
aveChange=round(totalChange/len(months),2)
greatestIncrease=max(change)
greatestDecrease=min(change)
# Create print function
def resultsFile():
    print(f'Financial Analysis', file=open("PyBankResults.txt", "a"))
    print(f'--------------------------------------', file=open("PyBankResults.txt", "a"))
    print(f'Total Months: {totalMonths}', file=open("PyBankResults.txt", "a"))
    print(f'Net Total: ${netTotal}', file=open("PyBankResults.txt", "a"))
    print(f'Average Change: ${aveChange}', file=open("PyBankResults.txt", "a"))
    print(f'Greatest Increase: ${greatestIncrease}', file=open("PyBankResults.txt", "a"))
    print(f'Greatest Decrease: ${greatestDecrease}', file=open("PyBankResults.txt", "a"))
    print(f'--------------------------------------', file=open("PyBankResults.txt", "a"))
resultsFile()
