#Import modules

import os
import csv

elec_file = os.path.join("Resources" , "election_data.csv")

# List of the names of candidates
candi = []


# List of a count of votes for each candidate

nvote = []

# List for the percentage of total votes per candidate
percent_vote = []

# Initialization of total number of votes 
total_votes = 0

with open(elec_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:

        # Incremente the counter of total votes
        total_votes += 1
        
        if row[2] not in candi:

            candi.append(row[2])

            index = candi.index(row[2])

            nvote.append(1)

        else:

            index = candi.index(row[2])

            nvote[index] += 1

    
    # Add the percentage votes to the list 

for votes in nvote:

        percentage = (votes/total_votes) * 100

        percentage = round(percentage)

        percentage = "%.3f%%" % percentage

        percent_vote.append(percentage)
        

    # Find the winning candidate
    
        winner = max(nvote)

        index = nvote.index(winner)

        winning_candi = candi[index]

    # Displaying results

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")

for i in range(len(candi)):
    #print(candi[i] + ": " + str(percent_vote[i]) + "% (" + str(nvote[i]) + ")")#Another try
    print("-------------------------")
    print(f"{candi[i]}: {str(percent_vote[i])} ({str(nvote[i])})")
print(f"Winner: {winning_candi}")
print("--------------------------")
print("--------------------------")
    
print("Eletions over!!!")

# Exporting to a text file: election_results.txt /Text output file


with open('election_results.txt', 'w') as text:

    text.write("Election Results\n")

    text.write("---------------------------------------\n")

    text.write("Total Vote: " + str(total_votes) + "\n")

    text.write("---------------------------------------\n")

    for i in range(len(set(candi))):

        text.write(candi[i] + ": " + str(percent_vote[i]) +"% (" + str(nvote[i]) + ")\n")

    text.write("---------------------------------------\n")

    text.write("The winner is: " + winning_candi + "\n")

    text.write("---------------------------------------\n")