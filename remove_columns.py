#!/usr/bin/env python3

# Remove columns from a CSV file and save the result to a new file.

import csv
import sys
from tqdm import tqdm

if len(sys.argv) < 3:
    print("Usage: remove_columns.py <input_file> <output_file> <column1> <column2> ...")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
columns_to_remove = sys.argv[3:]

# with open(input_file, 'r') as f:
#     pbar = tqdm(total=sum(1 for line in f))

with open(input_file, "r") as f:
    reader = csv.reader(f)
    with open(output_file, "w") as f2:
        writer = csv.writer(f2)
        for row in tqdm(
            reader,
            desc="Processing rows",
            total=sum(1 for _ in open(input_file)),
            unit=" rows",
        ):
            row_to_keep = [
                row[i] for i in range(len(row)) if str(i) not in columns_to_remove
            ]
            writer.writerow(row_to_keep)

