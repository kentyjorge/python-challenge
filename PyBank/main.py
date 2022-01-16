import os
import csv


bdata_csv = os.path.join("Resources","budget_data.csv")
#print(bdata_csv)

#function that 
#Total Months:
#Total Amount of Profit Losses
#Change in Profit Loss and then average
#Greatest increaste - Date and amount
#greates decrease - date and amount

#def fi_analysis(b_data):
    #date = str(b_data[0])
    #amount = int(b_data[1])
total_months = 0
total_amount = 0
change = 0 
firstValue = 0
lastValue = 0
minNum = 0
maxNum = 0
max = []
min = []
initial_amount = 0
amount = 0
change = 0
total_change = 0
#read in csv file
with open(bdata_csv, 'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    prev_row = None
    for row in csvreader:
        total_months = total_months + 1
        total_amount = int(row[1]) + total_amount

        #avg change want to take row amount - previous row amount, 
        #sum all those values, divide by total months
        if prev_row is None:
            total_change = 0
        else:
            change = int(row[1]) - int(prev[1])
            total_change = change + total_change
        
        if int(row[1]) > maxNum:
            maxNum = int(row[1])
            max = [row[0], row[1]]
        
        if int(row[1]) < minNum:
            minNum = int(row[1])
            min = [row[0], row[1]]
        
        prev = row

avg_change = total_change / total_months

print(total_months)
print(total_amount)
print(avg_change)
print(max)
print(min)