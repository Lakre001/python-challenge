#THE FIRST METHOD TO BE LAUNCHED IN PYBANK
# Import modules os and csv

import os
import csv

# CSV file in Bank path settings
Bank = os.path.join("Resources","budget_data.csv")

# Create the lists that will store data. 
profnL = []
monthly_changes = []
activity_period = []

# Initialization of variables.
tot_months = 0
totprofnL = 0
total_change_profit = 0
startProfnL = 0

# Open the CSV using the set path Bank for looping
with open(Bank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Looping to conduct the ask
    for row in csvreader:
      # Count is counting the number months in this dataset during the period
      tot_months = tot_months + 1 

      # To determine the greatest increase and decrease in profits during the period
      activity_period.append(row[0])

      # Append the profit information & calculate the total profit
      profnL.append(row[1])
      totprofnL = totprofnL + int(row[1])

      #Average change in profits from month to month. 
	  #And then the average change in profits
      endProfnL = int(row[1])
      monthly_change_profit = endProfnL - startProfnL

      #The monthly changes are stored in a monthly_change_profits list
      monthly_changes.append(monthly_change_profit)
      total_change_profit = total_change_profit + monthly_change_profit
      startProfnL = endProfnL

      #Average change in profits
      avg_change_profit = (total_change_profit / tot_months)
      
      #Max and Min change in profits with Date related
      greatest_increase_profit = max(monthly_changes)
      greatest_decrease_profit = min(monthly_changes)
      increase_date = activity_period[monthly_changes.index(greatest_increase_profit)]
      decrease_date = activity_period[monthly_changes.index(greatest_decrease_profit)]

print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(tot_months))
print("Total Profits: " + "$" + str(totprofnL))
print("Average Change: " + "$" + str(int(avg_change_profit)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profit) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profit)+ ")")
print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:

    text.write("----------------------------------------------------------\n")

    text.write("  Financial Analysis Output"+ "\n")

    text.write("----------------------------------------------------------\n\n")

    text.write("    Total Months: " + str(tot_months) + "\n")

    text.write("    Total Profits: " + "$" + str(totprofnL) +"\n")

    text.write("    Average Change: " + '$' + str(int(avg_change_profit)) + "\n")

    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profit) + ")\n")

    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profit) + ")\n")

    text.write("----------------------------------------------------------\n")


