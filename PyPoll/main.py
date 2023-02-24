import csv
import os
from pathlib import Path

# getting the csv path using os library
election_path = os.path.join("PyPoll", "Resources", "election_data.csv")
vote_id = []
county = []
candidates = []
votes_count = 0

votes_charles = 0
votes_diana = 0
votes_raymon = 0

# open and read csv
with open(election_path, 'r') as election_file: 
    csv_reader = csv.reader(election_file, delimiter=",")
    csv_header = next(csv_reader)
    # appending the data to the lists
    for row in csv_reader:
        vote_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    # count the total votes
        votes_count += 1
        # counting the votes for each candidate
        if row[2] =="Charles Casper Stockham":
            votes_charles += 1
        elif row[2] == "Diana DeGette":
            votes_diana += 1
        elif row[2] == "Raymon Anthony Doane":
            votes_raymon +=1
  # calculate the total votes for each candidate           
perc_charles = round((votes_charles/votes_count * 100),3)
perc_diana = round((votes_diana/votes_count * 100),3)
perc_raymon = round((votes_raymon/votes_count * 100),3)
#create a dictonary with each candidate and their votes to calculate the winner
winner_dict = {"Charles Casper Stockham": votes_charles, "Diana DeGette": votes_diana, "Raymon Anthony Doane": votes_raymon}
#get the winner from the dictionary using .get metod
winner = max(winner_dict, key = winner_dict.get)
#print the result using f string funciotn
print(f"""
Election Results
-------------------------
Total Votes: {votes_count}
-------------------------
Charles Casper Stockham: {perc_charles}% {votes_charles}
Diana DeGette: {perc_diana}% {votes_diana}
Raymon Anthony Doane: {perc_raymon}% {votes_raymon}
-------------------------
Winner: {winner}
-------------------------
""")
# create a txt file to store the results    
    
output_analysis = os.path.join("PyPull", "analysis", "results.txt")

with open(output_analysis,'w') as analysis:

    analysis.write(f"""
Election Results
-------------------------
Total Votes: {votes_count}
-------------------------
Charles Casper Stockham: {perc_charles}% {votes_charles}
Diana DeGette: {perc_diana}% {votes_diana}
Raymon Anthony Doane: {perc_raymon}% {votes_raymon}
-------------------------
Winner: {winner}
-------------------------
""")
