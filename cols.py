#!/usr/bin/env python3

import sys
import csv

# Print collumns from a CSV file.

# Check if the number of arguments is correct
if len(sys.argv) != 3:
    print("Usage: take_cols.py [filename] [collumn1] [collumn2] ...")
    sys.exit(1)

# The file to read from
filename = sys.argv[1]

# The collumns to output
collumns = [int(i) for i in sys.argv[2:]]

# Open the file and read the lines
with open(filename, "r") as f:
    reader = f.read()

    # make a list of the collumns
    output = []
    for line in reader:
        for c in collumns:
            output.append(line[c])  # append the collumn to the output list

    # print the output
    print(output)
