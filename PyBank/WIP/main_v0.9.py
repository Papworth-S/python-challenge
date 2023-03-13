#Module for reading csv file
import csv

#assigning contents of csv to a variable for use in this program
csvpath = 'Resources/budget_data.csv'

#output folder and file
fileoutput_path = 'analysis/bankoutput.txt'

#Setting up variables and giving them a starter intiger 
total = 0
change = 0
total_change = 0
counter = 0
GreatIncr = 0
GreatIncr_Mo = ''
GreatDec  = 99999999
GreatDec_Mo = ''
previous = 0

#Using the csv module to read the csv file 'budget_data.csv' which has been assigned 
#to the variable csvfile_path
with open(csvpath) as csvfile:

    #steping thought the csv file using the csv module function .reader 
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #using next function to skip the header row of the csv
    csv_header = next(csvreader)
    #print(f'Header: {csv_header}')

    #loop throw each row
    for row in csvreader:

        #TOSS print(row)
        counter += 1
        
        #set the current varialbe to this rows second column value
        current = row[1]

        # when the counter move up with row itteration change the valuse of varialbes change and previous
        if counter >= 1:
            change = int(current) - int(previous)  #not sure about this 
            previous = current

        #total_change = total_change + change
        total = total + int(row[1])

        #for testing TOSS, append the value of change to eaach row
        row.append(change)

        #if the chanve valuse currently stored equales the value currently in current basicly do nothing
        if change == int(current):
            total_change = total_change

        #else add the value of change to the valuse of total change I am sure there is a cleaner way but this works for now
        else:
            total_change = total_change + change

        #for testing TOSS, prit each row to confim the above loop and equatoins are working as desired
        #print(row)

        if change > GreatIncr:
            GreatIncr = change
            GreatIncr_Mo = row[0]

        if change <= GreatDec:
            GreatDec = change
            GreatDec_Mo = row[0]

    #total_change = total_change - change
    average_change = round((total_change / (counter -1)),2)
    
    print("")
    print("")
    print('Financial Analysis')        
    print('----------------------------------------------------')
    print(f'Total months: {counter}')
    #print("Current: " + (current))
    #print("Previous: " + (previous))
    #print("Change: "  + str(change))
    print("Total: $" + str(total))
    #print("SumofChange: " + str(total_change))
    print(f"Avarage Change: ${average_change}")
    print(f'Greatest Increase in Profits: {GreatIncr_Mo} (${GreatIncr})')
    print(f'Greatest Decrease in Profits: {GreatDec_Mo} (${GreatDec})')
    print('')
    print('')


#with open('analysis/test.txt', 'w') as f:
    #f.write('Does this work')

with open(fileoutput_path, 'w') as output:
    output.write('\n')
    output.write('\n')
    output.write('Financial Analysis  \n')
    output.write('----------------------------------------------------\n')
    output.write(f'Total months: {counter} \n')
    output.write("Total: $" + str(total) + '\n')
    output.write(f'Avarage Change: ${average_change} \n')
    output.write(f'Greatest Increase in Profits: {GreatIncr_Mo} (${GreatIncr}) \n')
    output.write(f'Greatest Decrease in Profits: {GreatDec_Mo} (${GreatDec}) \n')
    output.write('\n')
