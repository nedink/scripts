#!/usr/bin/env python3

import sys

# Print the first n lines of a CSV file.

# Check if the number of arguments is correct
if len(sys.argv) != 3:
    print("Usage: top_n.py [filename] [n]")
    print("Prints the first n lines of a CSV file.")
    sys.exit(1)

# The file to read from
filename = sys.argv[1]

# The number of rows to output
n = int(sys.argv[2])

# Open the file and read the lines
with open(filename) as f:
    lines = f.readlines()

# Output the first n lines
for line in lines[:n]:
    print(line, end="")
