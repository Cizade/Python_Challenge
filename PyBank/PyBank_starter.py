# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = r"C:\Users\caded\Desktop\Classwork\Module_3_Challenge\Python_Challenge\PyBank\Resources\budget_data.csv"  # Input file path
file_to_output = r"C:\Users\caded\Desktop\Classwork\Module_3_Challenge\Python_Challenge\PyBank\analysis\budget_analysis.txt"  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
changes = []
previous_profit = None
max_increase = {"date":"", "amount": float("-inf")}
max_decrease = {"date":"", "amount": float("inf")}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    date, previous_profit = first_row[0], int(first_row[1])

    # Track the total and net change
    total_months += 1
    total_net += previous_profit

    # Process each row of data
    for row in reader:
        date, profit = row[0], int(row[1])
        
        # Track the total
        total_months += 1
        total_net += previous_profit

        # Calcular the monthly change and appent the changes list
        change = profit - previous_profit
        changes.append(change)

        # Calculate the greatest increase in profits (month and amount)
        if change > max_increase["amount"]:
                max_increase = {"date": date, "amount": change}

        # Calculate the greatest decrease in losses (month and amount)
        if change < max_decrease["amount"]:
                max_decrease = {"date": date, "amount": change}

        # Update the previous profit for the next iteration
        previous_profit = profit

# Calculate the average net change across the months
average_change = sum(changes) / len(changes) if changes else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase['date']} (${max_increase['amount']})\n"
    f"Greatest Decrease in Profits: {max_decrease['date']} (${max_decrease['amount']})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
