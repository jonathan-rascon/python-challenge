import os
import csv

csvpath = os.path.join("python_challenge", "PyBank" ,"Resources", "budget_data.csv")
#define path
csvpath="python_challenge/PyBank/Resources/budget_data.csv"
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_changes = []
dates = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)


    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        if total_months > 1:
            change = int(row[1]) - previous_profit_loss
            profit_changes.append(change)
            dates.append(row[0])
        previous_profit_loss = int(row[1])

average_change = sum(profit_changes) / len(profit_changes)

greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)
increase_date = dates[profit_changes.index(greatest_increase)]
decrease_date = dates[profit_changes.index(greatest_decrease)]

print('Financial Analysis')
print('------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})')