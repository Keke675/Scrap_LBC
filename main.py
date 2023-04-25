from Scraping import get_data_lbc as lbc
from GSheet import connect_to_sheets
from GSheet import sheets_commands as sheets

# Connect to the spreadsheet
worksheet = connect_to_sheets.connect_to_sheets()

while(1):
    url = input("Donne le lien batard : ")
    # Get the data from the website1
    data = lbc.get_data(url)

    #Fill data into new row
    sheets.fill_data_into_row(worksheet, data)
