## Python-Challenge
# Python Project for Rice University

In this homework project, I will be using previous learnt concepts to complete two python challenges, PyElections and PyFinances. Both of these challenges encompasses a real-world situation Python scripting skills can come in handy. 


# PyElections

In this challenge, I was tasked with helping the city of Houston modernize its vote-counting process for the next mayoral elections. No candidate won a majority (over 50%) of the vote during the general election that took place on November 5, 2019. The 2019 Houston mayoral election was decided by a runoff on December 14, 2019 to elect the Mayor of Space City. I was assigned to write a script that will decide the two candidates with the highest number of votes and advance to the runoff election.

I was given a set of the last general election data called [houston_election_data.csv](https://github.com/sahobitayo/python-challenge/blob/master/PyElections/Pyelect.csv). The dataset is composed of three columns: Candidate, County, and Voter ID. I was tasked to create a Python script that analyzes the votes and calculates each of the following:

1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. Print the names of the two candidates who will advance to the runoff election.

The final script printed both the analysis to the terminal and exported a text file with the results. 


# PyFinances



In this project, I was tasked with creating a Python script for analyzing the financial records of your company. I was given a set of financial data called [budget_data.csv](https://github.com/sahobitayo/python-challenge/blob/master/PyFinances/budget.csv). The dataset is composed of two columns: Profit/Losses and Date. 

My task was to create a Python script that analyzes the records to calculate each of the following:

1. The total number of months included in the dataset
2. The net total amount of "Profit/Losses" over the entire period
3. The average of the changes in "Profit/Losses" over the entire period
4. The greatest increase in profits (date and amount) over the entire period
5. The greatest decrease in losses (date and amount) over the entire period


## Smple Output
My final script should both print the analysis to the terminal and export a text file with the results:


1. PyBank
```
$ python main.py
        Date  Profit/Losses
0   Jan-2010         867884
1   Feb-2010         984655
2   Mar-2010         322013
3   Apr-2010         -69417
4   May-2010         310503
..       ...            ...
81  Oct-2016         102685
82  Nov-2016         795914
83  Dec-2016          60988
84  Jan-2017         138230
85  Feb-2017         671099

[86 rows x 2 columns]
Total number of months: 86
Net total amount of profit/losses: $38382578
Average of changes: $-2315.12
Greatest increase amount: $1926159.0
Greatest increase date: Feb-2012
Greatest decrease amount: $-2196167.0
Greatest decrease date: Sep-2013
-----------------------------------
Financial Analysis
-----------------------------------
Total Months: 86
Total: $38,382,578.00
Average Change: $-2,315.12
Greatest Increase in Profits: Feb-2012, $1,926,159.00
Greatest Decrease in Profits: Sep-2013, $-2,196,167.00
```

2. 
```
$ python main.py
         Voter ID County Candidate
0        12864552  Marsh      Khan
1        17444633  Marsh    Correy
2        19330107  Marsh      Khan
3        19865775  Queen      Khan
4        11927875  Marsh      Khan
...           ...    ...       ...
3520996  18050509  Marsh      Khan
3520997  13060332  Marsh      Khan
3520998  16754708  Queen      Khan
3520999  12083146  Queen      Khan
3521000  14526187  Queen  O'Tooley

[3521001 rows x 3 columns]
Total number of votes cast: 3521001
List of candidates who have received votes:
['Khan' 'Correy' 'Li' "O'Tooley"]
Number of votes each candidate won:
[2218231, 704200, 492940, 105630]
Percentage of votes each candidate won:
[63.0, 20.0, 14.0, 3.0]
Winner: Khan
---------------------------------------------------------------
Election Results
---------------------------------------------------------------
Total votes: 3,521,001
---------------------------------------------------------------
Candidates  Number of Votes Percentage of Votes (%)
      Khan        2,218,231                   63.0%
    Correy          704,200                   20.0%
        Li          492,940                   14.0%
  O'Tooley          105,630                    3.0%
---------------------------------------------------------------
Winner: Khan
---------------------------------------------------------------
```


## TOOLS USED
- **Python
- **Pandas
- **Jupyter Notebook

