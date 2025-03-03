import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

tMonths = []
tProfit_Losses = []
Changes = []
Average_Change = []

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        tMonths.append(row[0])
        tProfit_Losses.append(int(row[1]))
        Total_Months = len(tMonths)
        Profit_Losses = sum(tProfit_Losses)

    for i in range(1, Total_Months):
        change = tProfit_Losses[i] - tProfit_Losses[i-1]
        Changes.append(change)
        Average_Change = sum(Changes) / len(Changes)

Greatest_Increase = max(Changes)
Greatest_Increase_Date = tMonths[Changes.index(Greatest_Increase) + 1]

Greatest_Decrease = min(Changes)
Greatest_Decrease_Date = tMonths[Changes.index(Greatest_Decrease) - 1]

Output_file = r"C:\Users\python_challenge\PyBank\Analysis\Financial Analysis.txt"

with open(Output_file, "w") as txt_file:
    
    Financial_Result = (f"\n\nFianancial Analysis\n"
                        f"--------------------------\n"
                        f"Total Months: {Total_Months}\n"
                        f"Total: ${Profit_Losses}\n"
                        f"Average Change: ${Average_Change: .2f}\n"
                        f"Greatest Profit Increase : {Greatest_Increase_Date} (${Greatest_Increase})\n"
                        f"Greatest Profit Decrease : {Greatest_Decrease_Date} (${Greatest_Decrease})\n")
    
    txt_file.write(Financial_Result)  

    print(Financial_Result)
                    

