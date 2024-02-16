#!/usr/bin/env python3

import sys

current_word = None
current_count = 0
word = None

# Input comes from STDIN
for line in sys.stdin:
    # Parse the input from mapper
    word, count = line.strip().split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    # This IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to STDOUT
            print(f'{current_word}\t{current_count}')
        current_count = count
        current_word = word

# Do not forget to output the last word if needed!
if current_word == word:
    print(f'{current_word}\t{current_count}')