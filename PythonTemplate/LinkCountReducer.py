#!/usr/bin/env python3

import sys

current_page = None
current_count = 0
page = None

# Input comes from STDIN
for line in sys.stdin:
    # Parse the input from mapper
    page, count = line.strip().split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    # This IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_page == page:
        current_count += count
    else:
        if current_page:
            # Write result to STDOUT
            print(f'{current_page}\t{current_count}')
        current_count = count
        current_page = page

# Do not forget to output the last word if needed!
if current_page == page:
    print(f'{current_page}\t{current_count}')