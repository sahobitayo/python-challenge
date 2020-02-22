# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


csvpath = os.path.join('budget.csv')
total_months= 0
difference=0
no= 867884
total=0
dates=[]
profit_loss= []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(csv_header)


    for row in csvreader:
        dates.append(row[1])
        total_months +=1
        number= int(row[0])
        total +=number
    #Put profit/loss between each month
        change =  int(row[0])- no
        profit_loss.append(change)
        no = int(row[0])

    average_change = sum(profit_loss)/85
    average_change= round(average_change,2)
    # Find greatest value and date
    greatest= max(profit_loss)
    index_great= profit_loss.index(greatest)
    profit_date= dates[index_great]
    #Find the lowest value and date
    lowest= min(profit_loss)
    index_low= profit_loss.index(lowest)
    loss_date= dates[index_low]
    #Print Values
    print("Financial Analysis")
    print("--------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {profit_date} ({greatest})")
    print(f"Greatest Decrease in Profits: {loss_date} ({lowest})")
    
        
 #Exporing to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total)}")
line5 = str(f"Average Change: ${str(average_change)}")
line6 = str(f"Greatest Increase in Profits: {profit_date} (${str(greatest)})")
line7 = str(f"Greatest Decrease in Profits: {loss_date} (${str(lowest)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))  
    

    
