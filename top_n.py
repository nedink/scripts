#!/usr/bin/env python3

import sys
from tqdm import tqdm

# This script takes a CSV file and outputs the first n lines to a new file.

# Check if the number of arguments is correct
if len(sys.argv) < 4:
    print("Usage: top_n.py [input_file] [output_file] [n] [start | 0]")
    print("Prints the first n lines of a CSV file.")
    sys.exit(1)

input_file = sys.argv[1]  # The input file
output_file = sys.argv[2]  # The output file

n = int(sys.argv[3])  # The number of rows to output
start = 0  # The starting row
if len(sys.argv) == 5:
    start = int(sys.argv[4])

with open(input_file) as input:
    pbar = tqdm(total=min(sum(1 for _ in input), n), desc="Processing rows")  # progress bar

with open(input_file) as input, open(output_file, "a") as output:
    # pbar = tqdm(total=sum(1 for _ in input_file), desc="Processing rows")  # progress bar
    lines_read = 0
    i = 0
    for line in input:
        if i < start:
            i += 1
            continue
        if lines_read >= n:
            break
        lines_read += 1
        output.write(line)
        pbar.update()

pbar.close()  # close the progress bar when the loop is finished
