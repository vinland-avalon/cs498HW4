#!/usr/bin/env python3
import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Split the input line into word and count
    word, count = line.strip().split('\t', 1)
    # Emit the count
    print(f'{count}\t1')