from ast import Name
import os
import csv

edata_csv = os.path.join("Resources","election_data.csv")
print(edata_csv)

#*****INSTRUCTIONS***************
#total number of votes
#candidates who received votes
#% of voes each candidate won
#number of votes each candidate won
#winner of election
#*********************************
total_value = 0
nameDict = {}

#try to use a set to get unique values
# def uniqueNames(name):
#     candidates =[]
#     unique_names = set(Name)
#     for name in unique_names:
#         candidates.append(name)
    
#     return candidates

#use iteration to get unique numbers
# def uniqueNamesTwo(names):
#     for name in names:
#         if name in cds:
#             continue
#         else:
#             cds.append(row[2])
#     return cds

with open(edata_csv, 'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_value = total_value + 1
        #if list does not contain name, add name
        #sum tv for a name and divide by total
        name = row[2]
        
        if name not in nameDict:
            nameDict[name] = 1
            
        else:
            nameDict[name] = nameDict[name] + 1
            
       #need to sum values for a specific name
    #print(nameDict)

print(f"Toal votes: {total_value}")
#print(cds)
#print(nameDict)

for name,count in nameDict.items():
    print(f"{name}: {count/total_value:.0%} ({count:.0f})")
    
winner = max(nameDict,key=nameDict.get)
print(f"{winner} is the winner!")