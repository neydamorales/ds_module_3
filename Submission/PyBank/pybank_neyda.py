# Modules
import csv

# Set path for file
csvpath = r"C:\Users\polit\Desktop\Data Analytics Bootcamp\homework\ds_module_3\Starter_Code\PyBank\Resources\budget_data.csv"

# variables
month_count = 0
net_profit = 0 

# changes
last_month_profit = 0 
changes = []
month_of_change = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        # count months
        month_count = month_count + 1
        
        # add profit
        net_profit = net_profit + int(row[1])
    
        # calculate change month over month
        # exclude the first row
        if (month_count == 1): 
            # still need to track profit though 
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_of_change.append(row[0])
        
        # reset last month profit
        last_month_profit = int(row[1])

    avg_change = sum(changes) / len(changes)

    max_change = max(changes)
    max_month_index = changes.index(max_change)
    max_month = month_of_change[max_month_index]
    
    min_change = min(changes)
    min_month_index = changes.index(min_change)
    min_month = month_of_change[min_month_index]
    
    output = f"""Financial Analysis
----------------------------
Total Months: {month_count}
Total Profit: ${net_profit}
Average Change: ${round(avg_change,2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""

    print(output) 

    # professor taught us this hack for exporting results to text file
    with(open("output_neyda.txt", 'w') as f):
        f.write(output) 