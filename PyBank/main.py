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
    

    #using next function to skip the header row of the csv
    csv_header = next(csvreader)
    

    #loop throw each row
    for row in csvreader:
        
        counter += 1
        
        #set the current varialbe to this rows second column value
        current = row[1]

        # when the counter move up with row itteration change the valuse of varialbes change and previous
        if counter >= 1:
            change = int(current) - int(previous)   
            previous = current

        #total_change = total_change + change
        total = total + int(row[1])

        #if the chanve valuse currently stored equales the value currently in current basicly do nothing
        if change == int(current):
            total_change = total_change

        #else add the value of change to the valuse of total change I am sure there is a cleaner way but this works for now
        else:
            total_change = total_change + change

        # adding the greatest change to the varialbe GreatIncr and the date to GreatIncr_Mo
        if change > GreatIncr:
            GreatIncr = change
            GreatIncr_Mo = row[0]

        #same as above but for the smallest 
        if change <= GreatDec:
            GreatDec = change
            GreatDec_Mo = row[0]

    #filling the average variable 
    average_change = round((total_change / (counter -1)),2)

    #sending some spaces, a header and the desired analysis to the screen
    print("")
    print("")
    print('Financial Analysis')        
    print('----------------------------------------------------')
    print(f'Total months: {counter}')
    print("Total: $" + str(total))
    print(f"Avarage Change: ${average_change}")
    print(f'Greatest Increase in Profits: {GreatIncr_Mo} (${GreatIncr})')
    print(f'Greatest Decrease in Profits: {GreatDec_Mo} (${GreatDec})')
    print('')
    print('')


#sending the same info from above to a .txt file
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
