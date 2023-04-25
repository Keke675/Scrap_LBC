# Fill data into the row
def fill_data_into_row(worksheet, data):
    # Find the first empty row in the first column
    row = find_empty_row_Acol(worksheet)
    # Fill the row with the data
    worksheet.update_cell(row, 4, data["price"])
    worksheet.update_cell(row, 2, data["adress"])
    worksheet.update_cell(row, 5, data["surface"])
    worksheet.update_cell(row, 6, data["rooms"])
    worksheet.update_cell(row, 10, data["url"])

# Find the first empty row in the first column
def find_empty_row_Acol(worksheet):
    i = 1
    while(worksheet.cell(i,1).value != None):
        i += 1
    return i