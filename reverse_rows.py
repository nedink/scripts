import csv
import sys

# Reverse the rows of a CSV file.

# check if the user has provided the correct number of arguments
if len(sys.argv) < 4:
    print("Usage: python reverse_rows.py <input_file> <output_file> <column_1> <column_2>")
    print("(Column indexes are zero-based)")
    sys.exit(1)

# open the csv file
with open(sys.argv[0], 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # create a new list
    new_csv = []
    # iterate over the rows of the csv
    for row in csv_reader:
        if len(row) <= sys.argv[2] or len(row) <= sys.argv[3]:
            print("The column numbers you provided are out of range")
            sys.exit(1)
        # reverse the two columns
        row[sys.argv[2]], row[sys.argv[3]] = row[sys.argv[3]], row[sys.argv[2]]
        # append the row to the new list
        new_csv.append(row)
        
# open the new csv file
with open('new_csv.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file)
    # write each row to the new csv file
    for row in new_csv:
        csv_writer.writerow(row)