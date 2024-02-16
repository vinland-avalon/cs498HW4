#!/usr/bin/env python3

import sys

word_count_pairs = []

# Input comes from STDIN
for line in sys.stdin:
    # Parse the input we got from mapper.py
    word, count = line.strip().split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    word_count_pairs.append((word, count))

# Sort the words according to the count (ascending) and lexicographically by word
# Since Python's sort is stable, we can do a two-step sort
word_count_pairs.sort(key=lambda x: x[0])  # Sort lexicographically by word
word_count_pairs.sort(key=lambda x: x[1])  # Then sort by count

# Select the bottom 10 items as the top words
top_words = word_count_pairs[-10:]

# Output the top 10 words and their counts
for word, count in top_words:
    print(f'{word}\t{count}')