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
data = open(r"C:\Users\User\IdeaProjects\Python Course YT\example.csv", encoding='utf-8') #need to provide specific file location
#utf-8 tells program what type of encoding it can read

# call csv.reader
csv_data = csv.reader(data)

# reformat it into a python object (list of lists)
data_lines = list(csv_data)

#How to loop to let it read data info
for line in data_lines[:5]:
    print(line)

#How to extract row
print(data_lines[10])

#How to extract a singular value
print(data_lines[10][3]) #Works like a 2d array

#How to get column
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

print(all_emails) #printing to show results

#How to get multiple columns
full_names = []
for line in data_lines[1:]:
    full_names.append(line[1]+ " " + line[2])

print(full_names)

#How to WRITE to a .cvs file
file_to_output = open('to_save_file.csv',mode='w',newline='') #What separates every newline
csv_writer = csv.writer(file_to_output, delimiter=',') #delimiter is just what separates one column from one another

#writing a singular row
csv_writer.writerow(['a', 'b', 'c'])

#writing multiple rows

csv_writer.writerows([['1','2','3'], ['4','5','6'],['7','8','9']])

#How to close file
file_to_output.close()

#How to append (add onto) files
f = open('to_save_file.csv', mode='a',newline='') #mode a means append, or adding on
csv_writer = csv.writer(f)
csv_writer.writerow(['what','is','this'])
f.close()




'''
Puzzle Spreadsheet
'''

puzzle_file_1 = open(r"C:\Users\User\IdeaProjects\Python Course YT\python-bootcamp\to_save_file.csv")

link = ''

for l = puzzle_file_1[:]