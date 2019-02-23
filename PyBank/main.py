import os
import csv
import datetime

#csv_file = os.path.join('C:\My Files\Renju\1- Data Science\Python_Module2\PyBank', "budget_data.csv")
csvpath = os.path.join("Resources","budget_data.csv" )
                       
with open(csvpath, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    num_months = 0
    Total = 0
    change = 0
    prev_value = 0 
    total_change = 0 
    current_value = 0
    max_change = 0 
    min_change = 0
    
    for row in csv_reader:
        if num_months > 0:
            current_month = row[0]
            current_value = int(row[1])
            Total+=current_value
            if num_months == 1:                
                prev_value = int(row[1])                
            else:
                change = current_value - prev_value
                total_change+=change
                prev_value = current_value   
                
                if change > max_change:
                    max_change = change
                    max_month = current_month
                   
                if change < min_change:
                    min_change = change
                    min_month = current_month
            
        num_months+=1
    
    max_dt = datetime.datetime.strptime(max_month, '%y-%b') 
    min_dt = datetime.datetime.strptime(min_month, '%y-%b') 
      
    print("Financial Analysis")   
    print("----------------------------")
    print("Total Months: " + str(num_months-1))    
    print("Total: $" + str(Total))
    print("Average  Change: $" + str( ('%.2f' % (total_change/(num_months-2))).rstrip('0').rstrip('.')))
    print("Greatest Increase in Profits: " + datetime.date.strftime(max_dt,'%b-%Y') + " ($" + str(max_change) +")")
    print("Greatest Decrease in Profits: " + datetime.date.strftime(min_dt,'%b-%Y') + " ($" + str(min_change) +")")
    
