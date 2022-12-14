#!/usr/bin/env python3

import csv
import sys
from tqdm import tqdm

# Add a column to a CSV file from a file containing the values for the new column.

if len(sys.argv) < 4:
    print(
        "Usage: add_column_from_file.py [input_file] [output_file] [values_file] [column_index ?? 0]"
    )
    print(
        "Add a column to a CSV file from a file containing the values for the new column."
    )
    sys.exit(1)

input_file = sys.argv[1]  # the file to read from
output_file = sys.argv[2]  # the file to write to
values_file = sys.argv[3]  # the file containing the values for the new column
column_index = (
    0
)  # the index of the column to insert the new column (last column by default)
if len(sys.argv) > 4:
    column_index = int(sys.argv[4])

# check that the input_file and values_file are the same length
if sum(1 for _ in open(input_file, "r")) != sum(1 for _ in open(values_file, "r")):
    print("Error: input_file and values_file must be the same length")
    sys.exit(1)

with open(input_file, "r") as input_csv, open(output_file, "w") as output_csv, open(
    values_file, "r"
) as values_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)
    values = [
        row[0] for row in csv.reader(values_csv)
    ]  # read the values from the values file

    row_count = 0
    # for each row in the input file, insert the value from the values file at the specified column and write the modified row to the output file
    for row in tqdm(reader, total=sum(1 for _ in open(input_csv, "r")), desc="Processing rows"):
        row.insert(
            column_index, values[row_count]
        )  # insert the value from the values file at the specified column
        writer.writerow(row)  # write the modified row to the output file
        row_count += 1
