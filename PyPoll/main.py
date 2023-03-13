#Module for reading csv file
import csv

#assigning contents of csv to a variable for use in this program
csvpath = 'Resources/election_data.csv'

#output folder and file
fileoutput_path = 'analysis/electionoutput.txt'

#starting points for the variables to be used
total_votes = 0
most_votes = 0
winner = ''
percentage = 0

#empth dictonary for final results
canidates = {}



#Using the csv module to read the csv file 'budget_data.csv' which has been assigned 
#to the variable csvfile_path
with open(csvpath) as csvfile:

    #steping thought the csv file using the csv module function .reader 
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #using next function to skip the header row of the csv
    csv_header = next(csvreader)
    
    #loop throw each row
    for row in csvreader:

        #running total of the votes
        total_votes = total_votes + 1

        #looking through the csv file and assigning the key and valuse to the newley created dictionary
        if row[2] in canidates:
            canidates[row[2]] =  canidates[row[2]] + 1
        else:
            canidates[row[2]] = 1
 
    #output the findings to both the screen and a .txt file
    with open(fileoutput_path, 'w') as output:

        #header text and values to be shown on screen and in file
        print('')
        output.write('\n')
        print('')
        output.write('\n')
        print(f'Electoin Results')
        output.write(f'Electoin Results \n')
        print(f'---------------------------------------')
        output.write(f'---------------------------------------\n')  
        print(f'Total Votes: {total_votes}')
        output.write(f'Total Votes: {total_votes} \n')
        print(f'---------------------------------------')
        output.write(f'---------------------------------------\n')

        #quick loop to snag the key and value for desplay and assigning values to variables for furture display or calculations
        for key, value in canidates.items():
            
            #getting the biggest amount of votes and who got those votes
            if value > most_votes:
                most_votes = value
                winner = key 

            #adding value to the percentage variable then actually turning it into a percentage
            percentage = value
            if percentage != total_votes:
                percentage = (percentage / total_votes) * 100

            #printing out the above efforts and inside rounding the valuse of percentage to 3 decimal places
            print(f'{key}: {round(percentage, 3)}%  ({value})')
            output.write(f'{key}: {round(percentage, 3)}%  ({value}) \n')

        #the rest of the text to be shonw on screen and in the .txt file
        print(f'---------------------------------------')
        output.write(f'---------------------------------------\n')
        print(f'Winner : {winner}')
        output.write(f'Winner : {winner} \n')
        print(f'---------------------------------------')
        output.write(f'---------------------------------------\n')
        print('')
        output.write('\n')
        print('')
        output.write('\n')












#with open('analysis/test.txt', 'w') as f:
    #f.write('Does this work')

#with open(fileoutput_path, 'w') as output:
    #output.write('\n')
    #output.write('\n')
    #output.write('Financial Analysis  \n')
    #output.write('----------------------------------------------------\n')
    #output.write(f'Total months: {counter} \n')
    #output.write("Total: $" + str(total) + '\n')
    #output.write(f'Avarage Change: ${average_change} \n')
    #output.write(f'Greatest Increase in Profits: {GreatIncr_Mo} (${GreatIncr}) \n')
    #output.write(f'Greatest Decrease in Profits: {GreatDec_Mo} (${GreatDec}) \n')
    #output.write('\n')