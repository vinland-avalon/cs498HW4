#!/usr/bin/env python3

import sys
import re

# Paths to stopwords and delimiters files
stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

# Read stopwords into a set for faster lookup
stopWords = set()
with open(stopWordsPath, 'r') as f:
    for word in f:
        stopWords.add(word.strip().lower())

# Read delimiters and create a regex pattern
with open(delimitersPath, 'r') as f:
    delimiters = f.read().strip()
    delimiterPattern = '|'.join(map(re.escape, delimiters))

# Process each line from standard input
for line in sys.stdin:
    # Tokenize the line using the delimiters
    tokens = re.split(delimiterPattern, line.strip().lower())
    for token in tokens:
        # Remove stopwords and non-empty tokens
        if token and token not in stopWords:
            print(f'{token}\t1')