#!/usr/bin/env python3

# Generate a UUID for each row in a CSV file.

import csv
import sys
from tqdm import tqdm
import uuid

# Generate a UUID for each row in a CSV file

if len(sys.argv) < 3:
    print(
        "Usage: python3 generate_uuid_column.py [input_file] [output_file] [column_index ?? 0]"
    )
    print("Generate a UUID for each row in a CSV file.")
    exit(1)

input_file = sys.argv[1]  # the file to read from
output_file = sys.argv[2]  # the file to write to
column_index = 0  # the index of the column to insert the UUID (first column by default)
if len(sys.argv) > 3:
    column_index = int(sys.argv[3])

with open(input_file, "r") as input_csv:
    pbar = tqdm(total=sum(1 for _ in input_csv), desc="Processing rows")  # progress bar

with open(input_file, "r") as input_csv, open(output_file, "w") as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    # pbar = tqdm(total=sum(1 for _ in input_csv), desc="Processing rows")  # progress bar

    row_count = 0
    # for each row in the input file, insert a new UUID at the specified column and write the modified row to the output file
    for row in reader:
        writer.writerow(
            row[:column_index] + [str(uuid.uuid4())] + row[column_index:]
        )  # insert a new UUID at the specified column and write the modified row to the output file
        pbar.update()  # update the progress bar
        # row_count += 1
        # if row_count > 5000:
        #     break

    pbar.close()  # close the progress bar when the loop is finished
