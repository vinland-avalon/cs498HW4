#!/usr/bin/env python3
import sys

# Dictionary to hold page ID and its corresponding count of incoming links
popularity_dict = {}

# Read input from the mapper
for line in sys.stdin:
    page_id, count = line.strip().split('\t', 1)
    popularity_dict[page_id] = int(count)

# Convert the popularity dictionary to a list of tuples and sort by count
sorted_popularity = sorted(popularity_dict.items(), key=lambda item: item[1])

# Dictionary to hold the page ID and its rank
ranks = {}

# Calculate rank for each page
for i in range(len(sorted_popularity)):
    # The rank is the index in the sorted list of all pages with strictly fewer counts
    page_id, count = sorted_popularity[i]
    # Use previous index for rank as it indicates the number of pages with fewer counts
    rank = i - sum(c == count for _, c in sorted_popularity[:i])
    ranks[page_id] = rank

# Print out the page ID and its rank, sorted by page ID in decreasing order
for page_id in sorted(ranks, key=int, reverse=True):
    print(f'{page_id}\t{ranks[page_id]}')
