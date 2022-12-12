#!/usr/bin/env python3

# Remove columns from a CSV file.

import csv
import sys
from tqdm import tqdm

# check if there are at least three arguments (input file, 
# output file, and at least one column index)
if len(sys.argv[1:]) < 3:
    # print a usage message if there are not at least three arguments
    print(
        "Usage: python remove_columns.py [input_file] [output_file] [column1] [column2] ..."
    )
    print("Removes columns from a CSV file.")
    exit(1)

# get the name of the input and output files from the command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# get the indices of the columns to remove from the command line arguments
# the indices are passed as strings, so we need to convert them to integers
columns_to_remove = [int(i) for i in sys.argv[3:]]

with open(input_file, "r") as input_csv:
    num_rows = sum(1 for row in input_csv)

# open the input and output files
with open(input_file, "r") as input_csv, open(output_file, "w") as output_csv:
    # create a CSV reader and writer
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    # create a progress bar with the total number of rows
    pbar = tqdm(total=num_rows, desc="Processing rows")

    # loop through each row in the input file
    for row in reader:
        # remove the columns specified in the arguments
        for index in sorted(columns_to_remove, reverse=True):
            if index >= len(row):
                continue
            del row[index]
        # write the modified row to the output file
        writer.writerow(row)
        pbar.update()  # update the progress bar

    pbar.close()  # close the progress bar when the loop is finished
