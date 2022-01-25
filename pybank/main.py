import csv
num_rows = 0

for row in open("budget_data.csv"):
    num_rows += 1
print("Total Months: " +num_rows)

with open('budget_data.csv') as csvfile:
  csvfile.next()
  total = sum(int(r[1]) for r in csv.reader(csvfile))
print("Total: " +total)

