import csv
import os
from pathlib import Path

# getting the csv path using os library
budget_path = os.path.join("PyBank", "Resources", "budget_data.csv")
# create 2 lists to receive the data
date = []
budget = []

# open and read csv
with open(budget_path, 'r') as budget_file: 
    csv_reader = csv.reader(budget_file)
    csv_header = next(csv_reader)
#appending the data to the lists

    for row in csv_reader:
        date.append(row[0])
        budget.append(int(row[1]))
# calculate the number of months, net changes and increses and decreases on the dataset
total_months = len(date)
total_net = 0
for row in budget:
    total_net += row
print(total_net)
total_changes = []

for row in range(len(budget)-1):
    total_changes.append(budget[row+1]-budget[row])

avg_changes = round(sum(total_changes) / len(total_changes),2)


max_increase =  max(total_changes)

month_max = date[total_changes.index(max_increase)+1]
min_increase =  min(total_changes)
month_min = date[total_changes.index(min_increase)+1]

# print the analyses with the f function
print(f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${avg_changes}
Greatest Increase in Profits: {month_max} ${max_increase}
Greatest Decrease in Profits: {month_min} ${min_increase}
"""
)

# create a txt file to store the results    
output_analysis = os.path.join("PyBank", "analysis", "results.txt")

with open(output_analysis,'w') as analysis:

    analysis.write(f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${avg_changes}
Greatest Increase in Profits: {month_max} ${max_increase}
Greatest Decrease in Profits: {month_min} ${min_increase}
""")
