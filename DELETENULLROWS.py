import openpyxl

# Open the Excel workbook in read-write mode
workbook = openpyxl.load_workbook('/Users/alexmammen/Documents/Projects/PowerliftingRanks/LifterSorting/IPF_Updated.xlsx')

# Get the sheet with the data
sheet = workbook['Sheet1']

# Initialize a list to store the rows to be deleted
rows_to_delete = []

# Iterate over the rows in the sheet
for row in sheet.rows:
    # Get the value in the column to be checked
    value = row[6].value
    # Check if the value is empty or None
    if value is None or value == '':
        # If the value is empty, add the row number to the rows_to_delete list
        rows_to_delete.append(row[6].row)
    # Get the value in the column to be checked
    value = row[7].value
    # Check if the value is empty or None
    if value is None or value == '':
        # If the value is empty, add the row number to the rows_to_delete list
        rows_to_delete.append(row[7].row)
    # Get the value in the column to be checked
    value = row[8].value
    # Check if the value is empty or None
    if value is None or value == '':
        # If the value is empty, add the row number to the rows_to_delete list
        rows_to_delete.append(row[8].row)
    # Get the value in the column to be checked
    value = row[9].value
    # Check if the value is empty or None
    if value is None or value == '':
        # If the value is empty, add the row number to the rows_to_delete list
        rows_to_delete.append(row[9].row)
    # Get the value in the column to be checked
    value = row[10].value
    # Check if the value is empty or None
    if value is None or value == '':
        # If the value is empty, add the row number to the rows_to_delete list
        rows_to_delete.append(row[10].row)    

# Iterate over the rows_to_delete list in reverse order
for row in reversed(rows_to_delete):
    # Delete the row from the sheet
    sheet.delete_rows(row, 1)

# Save the workbook
workbook.save('/Users/alexmammen/Documents/Projects/PowerliftingRanks/LifterSorting/IPF_Updated.xlsx')