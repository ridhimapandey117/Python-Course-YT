'''
- CSV (comma-separated variables) are a type of output common in spreadsheet programs
- Example:
    - Name. Hours, Rate
    - Dev,  20,    15
    - Mel,  40,    20
- .csv files ONLY contain raw data from spreadsheet

- Other libraries to consider:
    - Pandas
        - Has a whole data analysis library and can work with any tabular data type
        - Runs analysis and visuals
    - Openpyxl
        - Designed for Excel files, retains Excel functionality, and supports Excel formulas
        - python-excel.org tracks various other Excel based python libraries
    - Google Sheets Python API
        - GS-Python direct interface
        - Can directly make changes to GS
        - Available in many programming languages
'''

import csv
# Open the file
data = open('"C:\Users\User\IdeaProjects\Python Course YT\example.csv"') #might need to provide specific file location, else delete this note

# call csv.reader
csv_data = csv.reader(data)

# reformat it into a python object (list of lists)
data_lines = list(csv_data)