import os

import csv

election_data_csv = os.path.join("Resources", "election_data.csv")


with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    Totalcst_Votes = list(csvreader)
    Total_Votes = len(Totalcst_Votes)

Output_file = r"C:\Users\python_challenge\PyPoll\Analysis\Election_Results_Output.txt"

with open(Output_file, "w") as txt_file:

    Election_Result = (f"\n\nElection Results\n"
                        f"--------------------------\n"
                        f"Total votes: {Total_Votes}\n"
                        f"--------------------------\n")

    txt_file.write(Election_Result)  

    print(Election_Result)

    Candidates = {}
    for row in Totalcst_Votes:
            if row [2] not in Candidates:
                Candidates[row[2]] = 1
            else:
                Candidates[row[2]] += 1

    for candidate, Totalcst_Votes in Candidates.items():
            percentage = (Totalcst_Votes / Total_Votes) * 100
            txt_file.write(f'{candidate}: {percentage:.3f}% ({Totalcst_Votes})\n')
            print(f'{candidate}: {percentage:.3f}% ({Totalcst_Votes})\n')
            winner = max(Candidates, key=Candidates.get)

   
    txt_file.write(f"--------------------------\n")
    print(f"--------------------------\n")
    txt_file.write(f'Winner: {wir}')
    print(f'Winner: {winner}')
