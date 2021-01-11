# BOOTCAMP DATA ANALYTICS
# ------------------------------------------------------------------------------------
# PYTHON HOMEWORK:  Py Me Up, Charlie
# AUTHOR:           TANIA ANGELINA ROSAS ORTIZ
# DATE:             JAN 9, 2021
# AVAILABILITY:     tdm-mxc-data-pt-12-2020-u-c\Week 3 - Python\homework\PyBank
# DATA INPUT:       Resources\budget_data.csv
# DATA OUTPUT:      analysis\PyBankAnalysis.txt
# ------------------------------------------------------------------------------------

# DEPENDENCIES
import os
import csv

# ASIGN FILE
file = os.path.join("Resources", "budget_data.csv")

# CREATE LISTS
TransactionDate = []
Profit_Losses = []
Changes = []
Profit_LossesInt = []
Profit_LossesNext = []
Profit_LossesPrev = []

# READ THE FILE AND POPULATE LISTS
with open(file) as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for row in lines: 
        TransactionDate.append(row[0])          # READ DATE
        Profit_Losses.append(row[1])            # READ PROFIT/LOSSES

# REMOVE HEADERS FROM DATA
TransactionDate.pop(0)
Profit_Losses.pop(0)

for item in Profit_Losses:
    Profit_LossesInt.append(int(item))

# TOTAL NUMBER OF MONTHS INCLUDED IN THE DATASET
TotalMonths = len(TransactionDate)

# THE NET TOTAL AMOUNT OF "PROFIT/LOSSES" OVER THE ENTIRE PERIOD
NetPL = sum(Profit_LossesInt)

# CALCULATE THE CHANGES IN "PROFIT/LOSSES" OVER THE ENTIRE PERIOD 
Profit_LossesNext = Profit_LossesInt.copy()
Profit_LossesNext.pop(0)
Profit_LossesPrev = Profit_LossesInt.copy()
Profit_LossesPrev.pop()

for plNext, plPrev in zip(Profit_LossesNext,Profit_LossesPrev):
    change=plNext-plPrev
    Changes.append(change)

# THEN FIND THE AVERAGE OF THOSE CHANGES
ChangeSum = sum(Changes)
ChangeTot = len(Changes)
AverageChange = ChangeSum/ChangeTot
AverageChange = round(AverageChange,2)

# THE GREATEST INCREASE IN PROFITS (DATE AND AMOUNT) OVER THE ENTIRE PERIOD
MaxIncrease = max(Profit_LossesInt)
MaxIncreasePos = Profit_LossesInt.index(MaxIncrease)
MaxIncreaseDate = TransactionDate[MaxIncreasePos]

# THE GREATEST DECREASE IN LOSSES (DATE AND AMOUNT) OVER THE ENTIRE PERIOD
MaxDecrease = min(Profit_LossesInt)
MaxDecreasePos = Profit_LossesInt.index(MaxDecrease)
MaxDecreaseDate = TransactionDate[MaxDecreasePos]

# YOUR FINAL SCRIPT SHOULD BOTH PRINT THE ANALYSIS TO THE TERMINAL AND EXPORT A TEXT FILE WITH THE RESULTS
output_file = os.path.join("analysis", "PyBankAnalysis.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {TotalMonths}"])
    writer.writerow([f"Total: $ {NetPL}"])
    writer.writerow([f"Average  Change: $ {AverageChange}"])
    writer.writerow([f"Greatest Increase in Profits: {MaxIncreaseDate} (${MaxIncrease})"])
    writer.writerow([f"Greatest Decrease in Profits: {MaxDecreaseDate} (${MaxDecrease})"])

txtpath = "analysis/PyBankAnalysis.txt"
with open(txtpath, 'r') as txtfile:
    lines = txtfile.read()
    print(lines)

# ------------------------------------------------------------------------------------
# LIST OF REFERENCES:
#
# ------------------------------------------------------------------------------------
