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
with open (csvpath, 'r') as csvfile:
    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row first
    csv_header = next(csvreader)

    print("Financial Analysis")
    print("----------------------------------")
    print(num_months)

    #the total net amount of "profit/losses over the entire period
    sum_profit = 0
    sum_loss = 0
    totalPL = 0
    profit = 0

    for row in csvreader:
        profit = int(row[1])
        if profit >0:
            sum_profit = sum_profit + profit
        elif profit <0:
            sum_loss = sum_loss + profit
        totalPL = sum_profit + sum_loss
    print(f"Total : {totalPL}")

    


