import os
import csv

file = os.path.join('Resources', 'budget_data.csv')

with open(file, 'r') as csv_file:
  csv_reader = csv.reader(csv_file,delimiter=",")
  csv_header = next(csv_file)
  total_months = 0
  for row in csv_reader:
    total_months += 1
  print("Total Months: ", total_months)

with open(file, 'r') as csv_file:
  csv_reader = csv.reader(csv_file,delimiter=",")
  csv_header = next(csv_file)
  net_total = 0
  for row in csv_reader:
    net_total += int(row[1])
  print("Total: $", net_total)

with open(file, 'r') as csv_file:
  csv_reader = csv.reader(csv_file,delimiter=",")
  csv_header = next(csv_file)
  revenue_change = 0
  previous_revenue = 0
  dates = []
  profits = []

  for row in csv_reader:
    dates.append(row[0])
    revenue_change = int(row[1]) - previous_revenue
    profits.append(revenue_change)
    previous_revenue = int(row[1])
    revenue_avg = sum(profits)/len(profits)
  print(f"Average Change: ${str(round(revenue_avg,2))}")

  greatest_increase = max(profits)
  greatest_index = profits.index(greatest_increase)
  greatest_date = dates[greatest_index]
     
  print(f"Greatest Increase in Profits: {greatest_date}, (${str(greatest_increase)})")

  greatest_decrease = min(profits)
  lowest_index = profits.index(greatest_decrease)
  lowest_date = dates[lowest_index]
     
  print(f"Greatest Decrease in Profits: {lowest_date}, (${str(greatest_decrease)})")
  
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: $ {str(net_total)}")
line5 = str(f"Average Change: $ {str(revenue_avg)}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
