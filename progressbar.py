#!/usr/bin/env python3

# import the `time` and `tqdm` modules
import time
from tqdm import tqdm

# create a progress bar with a total of 50 iterations
pbar = tqdm(total=50)

# loop through some hypothetical process that takes a while
for i in range(50):
    # do some work here...
    time.sleep(0.1)  # simulate a delay
    
    # update the progress bar
    pbar.update()

# close the progress bar when the loop is finished
pbar.close()
