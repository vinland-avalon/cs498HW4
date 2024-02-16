#!/usr/bin/env python3
import sys
import math

# Initialize variables for calculating statistics
sum_counts = 0
count = 0
min_count = sys.maxsize
max_count = 0
differences_squared_sum = 0
nums = []

# Input comes from STDIN
for line in sys.stdin:
    # Parse the input from mapper.py
    current_count, _ = line.strip().split('\t', 1)

    # Convert count to int
    current_count = int(current_count)

    # Update statistics for sum, count, min, and max
    sum_counts += current_count
    count += 1
    min_count = min(min_count, current_count)
    max_count = max(max_count, current_count)
    nums.append(current_count)

# Calculate mean after processing all items
mean = sum_counts // count


# Calculate the sum of squared differences from the mean
for num in nums:
    differences_squared_sum += (num - mean) ** 2

# Calculate variance
variance = differences_squared_sum // count

# Print the final output
print(f'Mean\t{mean}')
print(f'Sum\t{sum_counts}')
print(f'Minimum\t{min_count}')
print(f'Maximum\t{max_count}')
print(f'Variance\t{variance}')