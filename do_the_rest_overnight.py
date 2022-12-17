#!/usr/bin/env python3
import os
import sys
import csv
from tqdm import tqdm
import psycopg2 as pg

# Commit the rest of the files to the "Payment" table in a database at postgresql://postgres3:1549@@21@34.68.1.34:5432/trpcdb
# The input files are named f"removed_lines.10000000.{n}.csv" where n is a number from 0 to 9.


if len(sys.argv) < 2:
    print("Usage: do_the_rest_overnight.py [db_name] [db_user] [db_password] [db_host] [db_port] [start] [n]")
    print("Commit the rest of the files to the 'Payment' table in a database")
    sys.exit(1)

db_name = sys.argv[1]
db_user = sys.argv[2]
db_password = sys.argv[3]
db_host = sys.argv[4]
db_port = sys.argv[5]
start = int(sys.argv[6])
n = int(sys.argv[7])

# connect to the database
conn = pg.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
)

# create a cursor
cur = conn.cursor()

# copy each file to the "Payment" table
for i in range(start, n):

    # open the file
    with open(f"removed_lines.10000000.{i}.csv", "r") as f:
        pbar = tqdm(total=sum(1 for _ in f), desc=f"Processing file {i}")  # progress bar

    with open(f"removed_lines.10000000.{i}.csv", "r") as f:
        # copy the file to the "Payment" table
        cur.copy_from(f, "Payment", sep=",")
        conn.commit()
        pbar.update()

    pbar.close()