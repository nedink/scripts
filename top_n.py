#!/usr/bin/env python3

import sys
from tqdm import tqdm
import os
import time

# Print the first n lines of a CSV file.

# Check if the number of arguments is correct
if len(sys.argv) < 4:
    print("Usage: top_n.py [input_file] [output_file] [n]")
    print("Prints the first n lines of a CSV file.")
    sys.exit(1)

input_file = sys.argv[1]  # The file to read from
output_file = sys.argv[2]  # The file to write to
n = int(sys.argv[3])  # The number of rows to output

# with open(input_file) as input:
#     pbar = tqdm(total=sum(1 for _ in input), desc="Processing rows")  # progress bar

with open(input_file) as input, open(output_file, "w") as output:
    pbar = tqdm(total=n, desc="Processing rows")  # progress bar
    lines_read = 0
    for line in input:
        if lines_read >= n:
            break
        lines_read += 1
        output.write(line)
        # time.sleep(0.001)
        pbar.update()

    # Output the first n lines
    # for line in lines[:n]:
    #     output.write(line)
    #     pbar.update()  # update the progress bar

pbar.close()  # close the progress bar when the loop is finished
