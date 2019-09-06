# This will allow us to create file paths across operating systems and csvreader
import os
import csv
# import numpy as np
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    file_to_output = "pyBankoutput.txt"
    # print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    #myList is everything in first column
    myList = []
    #myListcount is everything in second column
    myListcount = []    
    for row in csvreader:
        newitem = row[0]
        myList.append(newitem)
        newamount = row[1]
        myListcount.append(newamount)
    print("Financial Analysis")
    print("-----------------------")
    print("Total months:" + str(len(myList)))
    #find the sum of profits and losses
    totalsum = 0
    for each in myListcount:
        totalsum = totalsum + int(each)
    print("The net total of Profit/Losses is $" + str(totalsum))
    #find the greatest and smallest change and also the average of changes
    changeList = []
    change = 0

    maxchange = 0
    minchange = 0
    avgchange = 0
    maxchangefircol = None
    minchangefircol = None
    for i in range(len(myListcount)-1):
        change = int(myListcount[i+1]) - int(myListcount[i])
        changeList.append(change)

    maxchange = max(changeList)
    minchange = min(changeList)
    
    maxchangefircol = str(myList[changeList.index(max(changeList))])
    minchangefircol = str(myList[changeList.index(min(changeList))+ 1])
    
    avgchange = float(int(sum(changeList))) / len(changeList) 
    print("The greatest increase in profits is: " + str(maxchangefircol) + " $ " + str(maxchange))
    print("The greatest decrease in profits is: " + str(minchangefircol) + " $ " + str(minchange))
    print("The average change in profits is $" + str('%.2f' % avgchange))
#output
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total months:" + str(len(myList)))
    txt_file.write("\n")
    txt_file.write("The net total of Profit/Losses is $" + str(totalsum))
    txt_file.write("\n")
    txt_file.write("The greatest increase in profits is: " + str(maxchangefircol) + " $ " + str(maxchange))
    txt_file.write("\n")
    txt_file.write("The greatest decrease in profits is: " + str(minchangefircol) + " $ " + str(minchange)) 
    txt_file.write("\n")
    txt_file.write("The average change in profits is $" + str('%.2f' % avgchange))