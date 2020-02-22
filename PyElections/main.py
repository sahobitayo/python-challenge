# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


csvpath = os.path.join('Pyelect.csv')
total_no_votes= 0
percent_votes=[]
number_votes_candidate= []
candidates=[]
max_index=0

with open(csvpath, newline='', encoding= "utf8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)




    # Read each row of data after the header
    for row in csvreader:
        total_no_votes +=1
        if row[0] not in candidates:
            candidates.append(row[0])
            index = candidates.index(row[0])
            number_votes_candidate.append(1)
        else:
            index = candidates.index(row[0])
            number_votes_candidate[index] += 1
    
    # Add to percent_votes list 
    for votes in number_votes_candidate:
        percentage = (votes/total_no_votes) * 100
        percentage = round(percentage, 2)
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(number_votes_candidate)
    secondmax= min(number_votes_candidate)
    
    index = number_votes_candidate.index(winner)
    winning_candidate = candidates[index]
    
    def second_largest(number_votes_candidate):
        
        uniq_items = []
        for x in number_votes_candidate:  
            uniq_items.append(x)    
            uniq_items.sort()    
        return  uniq_items[-2] 
    secondmax= second_largest(number_votes_candidate)
    second_index= number_votes_candidate.index(secondmax)
    other_candidate= candidates[second_index]


    # Displaying results
print("Houston Mayoral Election Results")
print("-----------------------------------------")
print(f"Total Cast Votes: {str(total_no_votes)}")
print("-----------------------------------------")
for a in range(len(candidates)):
    print(f"{candidates[a]}: {percent_votes[a]}% ({number_votes_candidate[a]})")
print("-----------------------------------------")
print(f"1st Advancing Candidate: {winning_candidate}")
print(f"2nd Advancing Candidate: {other_candidate}")
print("-----------------------------------------")

#Exporing to .txt file
output = open("output.txt", "w")

line1 = "Houston Mayoral Election Results"
line2 = "--------------------------------------"
line3 = str(f"Total Cast Votes: {str(total_no_votes)}")
line4 = "--------------------------------------"
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for a in range(len(candidates)):
    line = str(f"{candidates[a]}: {str(percent_votes[a])}% ({str(number_votes_candidate[a])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"1st Advancing Candidate: {winning_candidate}")
line7 = str(f"2nd Advancing Candidate: {other_candidate}")
line8 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7, line8))