import os
import csv


budget = os.path.join('pybank', 'Resources', 'budget_data.csv')


#opening budget data
with open(budget, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)


    #declaring variables
    months = 0
    total = 0
    change = 0
    month_aray = []
    values = []


    # Loop through the data
    for row in csvreader:
        #count months
        months = months + 1
        
        #net total
        total = int(row[1]) + total

        #change in profits 
        values.append(int(row[1]))
        month_aray.append(row[0])
        

i = 0
total_C = 0
for x in values:
    if i == 0:
        i = i + 1
        continue
    change = x - values[i-1]
    total_C = change + total_C
    i = i + 1

Average_change = round(total_C/(months - 1), 2)

print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${Average_change}")


# greatest increase and decrease in profits
c = 0

increase = 0
decrease = 0
for x in values:
    if c == 0:
        c = c + 1
        continue
    change = x - values[c-1]
    if change > increase:
        increase = change
        i_month = month_aray[c]
    if change < decrease:
        decrease = change
        d_month = month_aray[c]
    c = 1 + c
print(f"Greatest Increase in Profits: {i_month} (${increase})")
print(f"Greatest Decrease in Profits: {d_month} (${decrease})")

#writing resaults to a new file
f = open("pybank/Analysis/results.txt", "w")
f.write("Finacial Analysis\n")
f = open("pybank/Analysis/results.txt", "a")
#appends to existing file
f.write("----------------------------\n")
f.write(f"Total Months: {months}\n")
f.write(f"Total: ${total}\n")
f.write(f"Average Change: ${Average_change}\n")
f.write(f"Greatest Increase in Profits: {i_month} (${increase})\n")
f.write(f"Greatest Decrease in Profits: {d_month} (${decrease})\n")