#!/usr/bin/env python3

import sys
import csv

# Print specific collumns from a csv file

if len(sys.argv) < 3:  # check if the number of arguments is correct
    print("Usage: python3 select_collumns.py <file_name> <collumn1> <collumn2> ...")
    print("Print specific collumns from a csv file.")
    sys.exit(1)

file_name = sys.argv[1]  # the file to read from
collumns = [int(i) for i in sys.argv[2:]]  # the collumns to output

with open(file_name, "r") as f:  # open the file and read the lines
    reader = csv.reader(f)
    for row in reader:
        row = [row[c] for c in collumns]  # filter the row to only include the collumns
        line = ",".join(row)  # join the row into a string
        print(line)  # print the line
