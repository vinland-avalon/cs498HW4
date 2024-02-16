#!/usr/bin/env python3

import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # The mapper simply prints out all lines it receives.
    # This passes them to the reducer.
    print(line.strip())