# Modules
import os
import csv

# Path to collect data from the Resources folder
budget = os.path.join('Resources', 'budget_data.csv')
budgetDataCsv = csv.reader(open(budget))
header = next(budgetDataCsv)
# Create Dict
allData={k:int(v) for k,v in budgetDataCsv}
months = list(allData.keys())
ckey, pkey = months[1:], months[:-1]
# Define Variables
totalMonths=len(months)
netTotal=sum(allData.values())
# Populating the list for changes in profit/loss
change = {c: allData[c] - allData[p] for c,p in zip(ckey,pkey)}
totalChange=sum(change.values())
aveChange=round(totalChange/len(change),2)
sortedChange=sorted(change, key=change.get)
greatestIncrease=max(change.values())
greatestDecrease=min(change.values())
greatestIncreaseMonth=sortedChange[-1]
greatestDecreaseMonth=sortedChange[0]
# Create print function
def resultsFile():
    print(f'Financial Analysis', file=open("PyBankResults.txt", "a"))
    print(f'--------------------------------------', file=open("PyBankResults.txt", "a"))
    print(f'Total Months: {totalMonths}', file=open("PyBankResults.txt", "a"))
    print(f'Net Total: ${netTotal}', file=open("PyBankResults.txt", "a"))
    print(f'Average Change: ${aveChange}', file=open("PyBankResults.txt", "a"))
    print(f'Greatest Increase: {greatestIncreaseMonth} ${greatestIncrease}', file=open("PyBankResults.txt", "a"))
    print(f'Greatest Decrease: {greatestDecreaseMonth} ${greatestDecrease}', file=open("PyBankResults.txt", "a"))
    print(f'--------------------------------------', file=open("PyBankResults.txt", "a"))
resultsFile()
