#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]

# Read league list IDs into a set for faster lookup
league_ids = set()
with open(leaguePath, 'r') as f:
    for line in f:
        league_ids.add(line.strip())

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Split the input line into page ID and count
    page_id, count = line.strip().split('\t', 1)

    # If the page is in the league list, pass it to the reducer
    if page_id in league_ids:
        print(f'{page_id}\t{count}')