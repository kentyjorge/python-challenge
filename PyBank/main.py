#import dependencies
import os
import csv

bdata_csv = os.path.join("Resources","budget_data.csv")

#********INSTRUCTIONS**********
#function that calls the applicable CSV, loops through the rows and calculates the following
#Total Months:
#Total Amount of Profit Losses
#Change in Profit Loss and then average
#Greatest increaste - Date and amount
#greates decrease - date and amount
#print to txt file
#********************************

#declare necessary variables
total_months = 0
total_amount = 0
change = 0 
minNum = 0
maxNum = 0
max = []
min = []
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
        #sum all change values, divide by total months less one -there is no change the first month
        if prev_row is None:
            total_change = 0
        else:
            change = int(row[1]) - int(prev_row[1])
            total_change = change + total_change
        
        #determine the min and max of the values
        if int(row[1]) > maxNum:
            maxNum = int(row[1])
            max = [row[0], row[1]]
        
        if int(row[1]) < minNum:
            minNum = int(row[1])
            min = [row[0], row[1]]
        #store row in previous row to compare to next row
        prev_row = row

#calculate the avg change based on the sum of changes and number of months less one
avg_change = total_change / (total_months-1)

print('''Finanancial Analysis
-----------------------------------''')
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${avg_change:.0f}")
print(f"Greatest Increase in Profits: {max[0]} (${max[1]})")
print(f"Greatest Decrease in Profits: {min[0]} (${min[1]})")

#print to text file
text_file = os.path.join("analysis","pyBank_Results.txt")
with open(text_file, "w") as text_file:
    text_file.write("Finanancial Analysis\n")
    text_file.write("-----------------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${total_amount}\n")
    text_file.write(f"Average Change: ${avg_change:.0f}\n")
    text_file.write(f"Greatest Increase in Profits: {max[0]} (${max[1]})\n")
    text_file.write(f"Greatest Decrease in Profits: {min[0]} (${min[1]})\n")