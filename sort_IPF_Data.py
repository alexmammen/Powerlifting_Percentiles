import csv

# Only converting to csv so I can manipulate data easily. Will than convert back to excel file to run back-end

# Open the input CSV file in read mode
with open('/Users/alexmammen/Documents/Projects/PowerliftingRanks/LifterSorting/IPF_Updated.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Initialize an empty list to store the cleaned rows
    cleaned_rows = []
    # Skip the first row of data (the header row)
    next(reader)
    # Iterate over the rows in the CSV
    for row in reader:
        # Check if the value in the "Equipment" column is "Raw" and the value in the "Age" column is not empty and the value in the "Event" column is "SBD"
        if row[3] == 'Raw' and row[4] and row[2] == 'SBD':
            # If all the conditions are met, append the row to the cleaned rows list
            cleaned_rows.append(row)

# Open the output CSV file in write mode
with open('/Users/alexmammen/Documents/Projects/PowerliftingRanks/LifterSorting/IPF_Updated.csv', 'w') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the cleaned rows to the output file
    for row in cleaned_rows:
        writer.writerow(row)
