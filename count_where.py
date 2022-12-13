#!/usr/bin/env python3

import csv
from functools import reduce
import sys

# Count the number of rows in a CSV file where a column is equal to a value

if len(sys.argv) < 4:
    print("Usage: count_where.py [input_file] [value] [col_index...]")
    print("Count the number of rows in a CSV file where a column is equal to a value")
    sys.exit(1)

input_file = sys.argv[1]
val = sys.argv[2]
col_indexes = sys.argv[3:]

with open(input_file, "r") as f:
    reader = csv.reader(f)
    count = 0

    for row in reader:  # use reduce and && to check if all columns are True

        row = [
            i for i in row if i in col_indexes
        ]  # filter the row to only the columns we want

        row = [
            True for i in row if i == val
        ]  # map the row to a list of booleans where the value is equal to the value we want

        # print(len(row))

        result = reduce(
            lambda x, y: x and y, row, True
        )  # reduce the list of booleans to a single boolean

        if result:
            count += 1  # if the row is True, increment the count
        
    print(count)