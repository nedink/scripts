#!/usr/bin/env python3

import csv
from functools import reduce
import sys
from tqdm import tqdm

# Count the number of rows in a CSV file where a column contains a value

if len(sys.argv) < 4:
    print("Usage: count_where.py [input_file] [value] [col_index...]")
    print("Count the number of rows in a CSV file where a column contains a value")
    sys.exit(1)

input_file = sys.argv[1]
val = sys.argv[2]
col_indexes = sys.argv[3:]

with open(input_file, "r") as f:
    pbar = tqdm(total=sum(1 for _ in f), desc="Processing rows")  # progress bar

with open(input_file, "r") as f:
    reader = csv.reader(f)
    count = 0
    rows = []

    for (
        row
    ) in (
        reader
    ):  # for each row, if any column from col_indexes contains val, increment count
        if any([val in row[int(i)] for i in col_indexes]):
            count += 1
            rows.append(reader.line_num)
        pbar.update()

    pbar.close()
    print(
        f"{count} rows where '{val}' in columns {', '.join([str(i) for i in col_indexes])}"
    )
    print(f"rows: {', '.join([str(i) for i in rows[:10]])}")
