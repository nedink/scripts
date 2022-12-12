#!/usr/bin/env python3

# Print the rows in a file that contain a given string.

import sys
from tqdm import tqdm

# check if the number of arguments is correct
if len(sys.argv) != 3:
    print("Usage: rows_containing.py [filename] [string]")
    print("Prints the rows in a file that contain a given string.")
    sys.exit(1)

# get the name of the file and the string to search for from the command row arguments
filename = sys.argv[1]
string = sys.argv[2]

# open the file and read through it row by row
with open(filename, "r") as f:
    pbar = tqdm(total=50)  # create a progress bar with a total of 50 iterations
    for row in f:
        pbar.update()  # update the progress bar
        # if the row contains the string, print it without a newline
        if string in row:
            print(row, end="")
    pbar.close()  # close the progress bar when the loop is finished
