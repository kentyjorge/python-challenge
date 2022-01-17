#import dependencies
import os
import csv

edata_csv = os.path.join("Resources","election_data.csv")

#*****INSTRUCTIONS***************
#calulate the following by reading the above csv and looping through the rows
#total number of votes
#candidates who received votes
#% of voes each candidate won
#number of votes each candidate won
#winner of election
#*********************************

#declare variables to add values to 
total_value = 0
nameDict = {}
#if list does not contain name, add name and set to 1
        #if name exists add 1
def candidate_count(edata):
    name = str(edata[2])
    if name not in nameDict:
        nameDict[name] = 1
    else:
        nameDict[name] = nameDict[name] + 1
#open and read the csv
with open(edata_csv, 'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    header = next(csvreader)

    for row in csvreader:
        total_value = total_value + 1
        candidate_count(row)
        #can_values(row)

#max function on the dictionary to get the name with the highest count
winner = max(nameDict,key=nameDict.get)

print(f'''Election Results
-----------------------------------
Total votes: {total_value}
-----------------------------------''')
#loop through dictonary and print each name and count
for name,count in nameDict.items():
    print(f"{name}: {count/total_value:.0%} ({count:.0f})")
print(f'''-------------------------
{winner} is the winner!
-----------------------------------''')
#create and update text file
text_file = os.path.join("analysis","pyPoll_Results.txt")
with open(text_file, "w") as text_file:
    text_file.write(f"Election Results\n")
    text_file.write("-----------------------------------\n")
    text_file.write(f"Total votes: {total_value}\n")
    text_file.write("-----------------------------------\n")
    #loop through dictonary and print each name and count
    for name,count in nameDict.items():
        text_file.write(f"{name}: {count/total_value:.0%} ({count:.0f})\n")
    text_file.write(f"-------------------------\n")
    text_file.write(f"{winner} is the winner!\n")
    text_file.write("-----------------------------------")