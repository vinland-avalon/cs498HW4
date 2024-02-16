#!/usr/bin/env python3

import sys

page_count_pairs = []

# Input comes from STDIN
for line in sys.stdin:
    # Parse the input we got from mapper.py
    page, count = line.strip().split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    page_count_pairs.append((page, count))

# Sort the words according to the count (ascending) and lexicographically by word
# Since Python's sort is stable, we can do a two-step sort
page_count_pairs.sort(key=lambda x: x[0])  # Sort lexicographically by word
page_count_pairs.sort(key=lambda x: x[1])  # Then sort by count

# Select the bottom 10 items as the top words
top_pages = page_count_pairs[-5:]

# Output the top 10 words and their counts
for page, count in top_pages:
    print(f'{page}\t{count}')