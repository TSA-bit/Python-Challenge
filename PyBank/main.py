#import module for reading csv files
import os
import csv
#path to collect data from resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

#what is the total number of months included in the dataset
import datetime
end_date = datetime.datetime(2017, 3, 1)
start_date = datetime.datetime(2010, 1, 1)
num_months = (end_date.year - start_date.year) *12 + (end_date.month - start_date.month)

#read in the csv file
with open (csvpath, newline="", encoding = "utf-8") as budget:
    #split the data on commas
    csvreader = csv.reader(budget, delimiter=',')

    #read the header row first
    header = next(csvreader)
    
    
    #create empty lists for iteration
    total_months = []
    total_profit = []
    monthly_profit_change = []
   
    #iterate through months to obtain monthly change in profits
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        #take difference between two months and append montly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

    #obtain max and min of the monthly profit change list
    max_increase_value = max(monthly_profit_change)
    max_decrease_value = min(monthly_profit_change)

    #match month of max and min index
    max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

#Print statement
print("Financial Analysis")
print("----------------------------------")
print(num_months)
print(f"Total : ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${total_months[max_increase_month]})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#specify file to write to
output_path = os.path.join("output", "new.csv")

#open the file using "write mode".
with open(output_path, 'w') as csv.file:

#initialize csv writer
    csvwriter - csv.writer(csvfile)
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("----------------------------------")
    csvwriter.writerow(num_months)
    csvwriter.writerow(f"Total : ${sum(total_profit)}")
    csvwriter.writerow(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    csvwriter.writerow(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${total_months[max_increase_month]})")
    csvwriter.writerow(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


