#!/usr/bin/env python3

import sys
import csv
from tqdm import tqdm

# Remove a line from a CSV file.

if len(sys.argv) < 4:
    print("Usage: remove_line_from_file.py [input_file] [output_file] [line_number]")
    print("Remove a line from a CSV file.")
    sys.exit(1)

input_file = sys.argv[1]  # the file to read from
output_file = sys.argv[2]  # the file to write to
line_number = int(sys.argv[3])  # the line number to remove

with open(input_file, "r") as input_csv, open(output_file, "w") as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    row_count = 0
    # for each row in the input file, remove the specified line and write the modified row to the output file
    for row in tqdm(reader, total=sum(1 for _ in open(input_file, "r")), desc="Processing rows"):
        if row_count != line_number:
            writer.writerow(row)  # write the modified row to the output file
        row_count += 1

