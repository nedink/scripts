#!/usr/bin/env python3

import sys
import csv
from tqdm import tqdm

# Get foreign keys based on the value in the column specified and output to a new file.
# Get the id for each value by looking it up in a dictionary made from the primary table file.
# In the primary table, the id is expected to be in column 1, and the value to be in column 2.

if len(sys.argv) < 5:
    print("Usage: ./get_fkeys.py [input_file] [output_file] [primary_table_file] [val_col]")
    print("Add foreign keys to a table file based on the value in the column specified. Outputs to a new file.")
    sys.exit(1)

input_file = sys.argv[1]  # the table file to modify
output_file = sys.argv[2]  # a file to output to
primary_table_file = sys.argv[3]  # the primary, or independent table
val_col = int(
    sys.argv[4]
)  # the column in the input file to use as the value to look up in the primary table


# 1. Create a dictionary of the primary table, mapping from column 2 to column 1

primary_table = {}

with open(primary_table_file, "r") as f:
    pbar = tqdm(
        total=sum(1 for _ in f), desc="Processing primary table"
    )  # progress bar

with open(primary_table_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        primary_table[row[1]] = row[0]  # map from column 2 to column 1
        pbar.update()

    pbar.close()


# 2. Add the foreign key to the input file at the last column

with open(input_file, "r") as f:
    pbar = tqdm(
        total=sum(1 for _ in f), desc="Collecting fkeys for input file"
    )  # progress bar

with open(input_file, "r") as f, open(output_file, "w") as g:
    reader = csv.reader(f)
    writer = csv.writer(g)
    for row in reader:
        # row.append(
        #     primary_table[row[val_col]]
        # )  # add the foreign key to the end of the row
        writer.writerow([
            primary_table[row[val_col]]
        ])  # write the foreign key to the output file
        pbar.update()

    pbar.close()