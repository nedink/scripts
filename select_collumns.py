import sys
import csv

# Print specific collumns from a csv file

if len(sys.argv) < 3:  # check if the number of arguments is correct
    print("Usage: python3 select_collumns.py <filename> <collumn1> <collumn2> ...")
    sys.exit(1)

filename = sys.argv[1]  # the file to read from
collumns = [int(i) for i in sys.argv[2:]]  # the collumns to output

with open(filename, "r") as f:  # open the file and read the lines
    reader = csv.reader(f)

    output = []  # make an empty list to store the output

    for row in reader:
        row = [row[c] for c in collumns]  # filter the row to only include the collumns
        line = ', '.join(row)  # join the row into a string
        # line = row.join(", ")  # join the row into a string
        print(line)  # print the line

    # print(output)  # print the output
