import os
import csv
 
csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Analysis', 'budget_analysis.txt')

total_months = []
net_profit = 0
change = []
prev_PL= 0
greatest_in = 0
in_month = ' '
greatest_dec = 0
dec_month = ' '

#reading imported data
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    # print(csv_header)
    
    
    for row in csvreader:
        
        # Counting total number of months
        total_months.append(row[0])
        num_months = len(total_months)
        
        # Determining total profit/loss
        net_profit += int(row[1])
        
        # Calculating profit/loss changes between months
        change.append(int(row[1]) - prev_PL)
        prev_PL = int(row[1])
        
        if (int(row[1]) > greatest_in):
            greatest_in = int(row[1])
            in_month = row[0]
            
        if (int(row[1]) < greatest_dec):
            greatest_dec = int(row[1])
            dec_month = row[0]
        
    # print(f'There are {num_months} months included in the data set.')    
    # print(f'The net profit/loss over the entire period is ${net_profit}.')    
    # print(len(change))
    # print(change)
    # print(greatest_in)
    # print(greatest_dec)
    avg_change = sum(change) / len(change)
    # print(avg_change)
    
    analysis = f'''
        Financial Analysis
        -----------------------------------
        Total Months: {num_months} 
        Total: ${net_profit}
        Average Change: ${avg_change}
        Greatest Increase in Profits: {in_month} ${greatest_in}
        Greatest Decrease in Profits: {dec_month} ${greatest_dec}
        '''
    print(analysis)
    
    with open(output_path, 'w') as text:
        text.write(analysis)