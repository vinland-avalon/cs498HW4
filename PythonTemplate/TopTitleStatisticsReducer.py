#!/usr/bin/env python3
import sys
import math

# Initialize variables for calculating statistics
sum_counts = 0
count = 0
min_count = sys.maxsize
max_count = 0
squared_sum = 0

# Input comes from STDIN
for line in sys.stdin:
    # Parse the input from mapper.py
    current_count, _ = line.strip().split('\t', 1)

    # Convert count to int
    current_count = int(current_count)

    # Update statistics
    sum_counts += current_count
    squared_sum += current_count ** 2
    count += 1
    min_count = min(min_count, current_count)
    max_count = max(max_count, current_count)

# Calculate mean
mean = sum_counts // count

# Calculate variance using the formula: Var(X) = E[(X - μ)^2]
variance = (squared_sum // count) - (mean ** 2)

# Print the final output
print(f'Mean\t{mean}')
print(f'Sum\t{sum_counts}')
print(f'Minimum\t{min_count}')
print(f'Maximum\t{max_count}')
print(f'Variance\t{variance}')