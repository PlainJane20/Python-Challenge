import os
import csv

#Dependencies
candidate = []
vote_count = {}
percentage = {}
total_votes = 0

with open('PyPoll/Resources/election_data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        total_votes += 1
        if row[2] in candidate and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1
        #else create new spot in list for candidate
        else:
            candidate.append(row[2])
            vote_count[row[2]] = 1

#Calculation for the percentage
for key,value in vote_count.items():
    percentage[key] = str(round((value/total_votes)*100,3)) + "% ("+str(value)+ ")"

#Election winner
winner = max(vote_count.keys(), key=(lambda k: vote_count[k]))

#Output to txt file
with open('output_election.txt','w',newline='') as textfile:
    print('Election Results',file = textfile)
    print('----------------------------------',file = textfile)
    print(f'Total Votes:{total_votes}',file = textfile)
    print('----------------------------------',file = textfile)
    print(f'Percentage:{percentage}',file = textfile)
    print('----------------------------------',file = textfile)
    print(f'Winner:{winner}',file = textfile)
    print('----------------------------------',file = textfile)

with open('output_election.txt',newline='')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)