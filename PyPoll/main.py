import os
import csv

poll = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(poll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    count = 0
    canidates = []
    votes = []

    for row in csvreader:
        #Counts the amount of votes
        count = count + 1
        
        #adds canidates to a list if their count is 0
        exist_count = canidates.count(row[2])
        if exist_count == 0:
            canidates.append(row[2])

        if row[2] == canidates[0]
            




print(canidates)