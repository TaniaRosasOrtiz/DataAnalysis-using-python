# BOOTCAMP DATA ANALYTICS
# ------------------------------------------------------------------------------------
# PYTHON HOMEWORK:  Py Me Up, Charlie
# AUTHOR:           TANIA ANGELINA ROSAS ORTIZ
# DATE:             JAN 10, 2021
# AVAILABILITY:     tdm-mxc-data-pt-12-2020-u-c\Week 3 - Python\homework\PyPoll
# DATA INPUT:       Resources\election_data.csv
# DATA OUTPUT:      analysis\PyPollAnalysis.txt
# ------------------------------------------------------------------------------------

# DEPENDENCIES
import os
import csv

# ASIGN FILE
file = os.path.join("Resources", "election_data.csv")

# CREATE LISTS
Candidates = []
CandidatesUnique = []

# READ THE FILE AND POPULATE LISTS
with open(file) as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for row in lines: 
        Candidates.append(row[2])          # READ Candidate

# REMOVE HEADERS FROM DATA
Candidates.pop(0)

# THE TOTAL NUMBER OF VOTES CAST
VotesTotal = len(Candidates)

# A COMPLETE LIST OF CANDIDATES WHO RECEIVED VOTES
list_set = set(Candidates) 
CandidatesUnique = list(list_set)   # CONVERT SET TO THE LIST 
CandidatesUniqueTotal = len(CandidatesUnique)

# THE PERCENTAGE OF VOTES EACH CANDIDATE WON
# for candidate in CandidatesUnique:
#     if candidate


# THE TOTAL NUMBER OF VOTES EACH CANDIDATE WON


# THE WINNER OF THE ELECTION BASED ON POPULAR VOTE


# YOUR FINAL SCRIPT SHOULD BOTH PRINT THE ANALYSIS TO THE TERMINAL AND EXPORT A TEXT FILE WITH THE RESULTS
output_file = os.path.join("analysis", "PyPollAnalysis.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {VotesTotal}"])
    writer.writerow(["-------------------------"])
#     for row in writer:
#         writer.writerow([f"Greatest Increase in Profits: {MaxIncreaseDate} (${MaxIncrease})"])
#     writer.writerow(["-------------------------"])
#     writer.writerow([f"Winner: {NetPL}"])
#     writer.writerow(["-------------------------"])

txtpath = "analysis/PyPollAnalysis.txt"
with open(txtpath, 'r') as txtfile:
    lines = txtfile.read()
    print(lines)

# ------------------------------------------------------------------------------------
# LIST OF REFERENCES:
# 
# REFERENCE (1): @Striver (n.d.) "Python | Get unique values from a list". Python. Geeks for Geeks. Retrieve on Jan 10, 2021 from https://www.geeksforgeeks.org/python-get-unique-values-list/
#
# ------------------------------------------------------------------------------------