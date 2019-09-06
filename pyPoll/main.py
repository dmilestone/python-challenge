# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    file_to_output = "pyPolloutput.txt"
    
    totalvotes = 0
    correy = 0
    khan = 0
    li = 0
    otool = 0
    
    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] == "Correy":
            correy = correy + 1
        elif (row[2] == "Khan"):
            khan = khan + 1
        elif (row[2] == "Li"):
            li = li + 1
        else:
            otool = otool + 1

    percorrey = 0
    perkhan = 0
    perli = 0
    perotool = 0
    percorrey = '%.2f' % ((correy/totalvotes) * 100)
    perkhan = '%.2f' % ((khan/totalvotes) * 100)
    perli = '%.2f' % ((li/totalvotes) * 100)
    perotool = '%.2f' % ((otool/totalvotes) * 100)
       
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
    print("Election Results")
    print("--------------------")
    print("The total number of votes cast is: " + str(totalvotes))
    print("--------------------")
    print("Correy came in with " + str(correy) + " votes with " + str(percorrey) + "%")
    print("Khan came in with " + str(khan) + " votes with " + str(perkhan) + "%")
    print("Li came in with " + str(li) + " votes with " + str(perli) + "%")
    print("O'Tooley came in with " + str(otool) + " votes with " + str(perotool) + "%")
    print("--------------------")
    
    if correy > khan and correy > li and correy > otool:
        winner = "Correy"
    elif khan > correy and khan > li and khan > otool:
        winner = "Khan"
    elif li > correy and li > khan and li > otool:
        winner = "Li"
    else:
        winner = "O'Tooley"
    print("The winner is " + str(winner))

#output 
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("--------------------")
    txt_file.write("\n")
    txt_file.write("The total number of votes cast is: " + str(totalvotes))
    txt_file.write("\n")
    txt_file.write("--------------------")
    txt_file.write("\n")
    txt_file.write("Correy came in with " + str(correy) + " votes with " + str(percorrey) + "%")
    txt_file.write("\n")
    txt_file.write("Khan came in with " + str(khan) + " votes with " + str(perkhan) + "%")
    txt_file.write("\n")
    txt_file.write("Li came in with " + str(li) + " votes with " + str(perli) + "%")
    txt_file.write("\n")
    txt_file.write("O'Tooley came in with " + str(otool) + " votes with " + str(perotool) + "%")
    txt_file.write("\n")
    txt_file.write("--------------------")
    txt_file.write("\n")
    txt_file.write("The winner is " + str(winner))