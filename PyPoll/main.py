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
            votes.append(0)

        
        can_ID = canidates.index(row[2])
        votes[can_ID] = votes[can_ID] + 1

#Creates dict that stores canidates votes and names
Canidates_dict = {"Canidate":[], "Votes":[], "Percent_votes":[]}
for x in canidates:
    position = canidates.index(x)
    Canidates_dict["Canidate"].append(x)
    Canidates_dict["Votes"].append(votes[position])
    votes_p = round((votes[position]/count)*100,3)
    Canidates_dict['Percent_votes'].append(str(votes_p) + "%")

#iterates through dict to find who has the highest vote count
Winner_Votes = 0
interate = 0
for x in Canidates_dict["Votes"]:
    if x > Winner_Votes:
        Winner_Votes = x
        Winner_canidate = Canidates_dict["Canidate"][interate]
    interate = 1 + interate


#Print to terminal
print(f"Election Results")
print(f"-----------------------")
print(f"Total Votes: {count}")
print(f"-----------------------")
interate = 0
for x in Canidates_dict["Canidate"]:
    print(f"{x}: {Canidates_dict['Percent_votes'][interate]} ({Canidates_dict['Votes'][interate]})")
    interate = 1 + interate
    
print(f"-----------------------")
print(f"Winner: {Winner_canidate}")
print(f"-----------------------")

#Save to text file
f = open("pypoll/Analysis/results.txt", "w")
f.write("Election Results\n")
f = open("pypoll/Analysis/results.txt", "a")
f.write(f"-----------------------\n")
f.write(f"Total Votes: {count}\n")
f.write(f"-----------------------\n")
interate = 0
for x in Canidates_dict["Canidate"]:
    f.write(f"{x}: {Canidates_dict['Percent_votes'][interate]} ({Canidates_dict['Votes'][interate]})\n")
    interate = 1 + interate
    
f.write(f"-----------------------\n")
f.write(f"Winner: {Winner_canidate}\n")
f.write(f"-----------------------\n")