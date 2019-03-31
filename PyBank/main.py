# Modules
import os
import csv

# Path to collect data from the Resources folder
budgetDataCSV = os.path.join('Resources/budget_data.csv')

# Define Variables
months = []
totalMonths = 0
netTotal = 0
profitLoss = []
profitLossStepped = []

# Read in the CSV file
with open(budgetDataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

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
def results():
# Print header
    print(f'Financial Analysis')
    print(f'--------------------------------------')
    print(f'Total Months: {totalMonths}')
    print(f'Net Total: ${netTotal}')
    print(f'Average Change: ${aveChange}')
    print(f'Grestest Increase: ${greatestIncrease}')
    print(f'Grestest Decrease: ${greatestDecrease}')
    print(f'--------------------------------------')
results()

# Create print function
def resultsFile():
# Print header
    print(f'Financial Analysis', file=open("PyBankReults.txt", "a"))
    print(f'--------------------------------------', file=open("PyBankReults.txt", "a"))
    print(f'Total Months: {totalMonths}', file=open("PyBankReults.txt", "a"))
    print(f'Net Total: ${netTotal}', file=open("PyBankReults.txt", "a"))
    print(f'Average Change: ${aveChange}', file=open("PyBankReults.txt", "a"))
    print(f'Grestest Increase: ${greatestIncrease}', file=open("PyBankReults.txt", "a"))
    print(f'Grestest Decrease: ${greatestDecrease}', file=open("PyBankReults.txt", "a"))
    print(f'--------------------------------------', file=open("PyBankReults.txt", "a"))
resultsFile()
