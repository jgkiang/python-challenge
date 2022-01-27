import os
import csv

file = os.path.join('Resources', 'election_data.csv')

num_votes = []
candidates = []
vote_percent = []
total_votes = 0

with open(file, 'r') as csv_file:
  csv_reader = csv.reader(csv_file,delimiter=",")
  csv_header = next(csv_file)
  for row in csv_reader:
    total_votes += 1

    if row[2] not in candidates:
        candidates.append(row[2])
        index = candidates.index(row[2])
        num_votes.append(1)
    else:
        index = candidates.index(row[2])
        num_votes[index] += 1

for votes in num_votes:
    percentage = (votes/total_votes) * 100
    percentage = round(percentage)
    percentage = "%.2f%%" % percentage
    vote_percent.append(percentage)
    
winner = max(num_votes)
index = num_votes.index(winner)
winning_candidate = candidates[index]

print("Election Results")
print("--------------------------")
print("Total Votes: ", total_votes)
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(vote_percent[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")
  
output = open("output.txt", "w")

line1 = "Election Results"
line2 = "---------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(vote_percent[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))