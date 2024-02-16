#!/usr/bin/env python3
import sys

linked_pages = set()
all_pages = set()

for line in sys.stdin:
    # Parse the input from mapper
    page_id, page_type = line.strip().split('\t')

    if page_id not in all_pages:
        all_pages.add(page_id)

    # If the page is linked to by another, add to linked_pages set
    if page_type == 'L':
        if page_id not in linked_pages:
            linked_pages.add(page_id)

# Orphan pages are those that are not in linked_pages set but in parent_pages
orphan_pages = all_pages - linked_pages

# Print orphan pages sorted in increasing order
for orphan_page in sorted(orphan_pages, key=int):
    print(orphan_page)