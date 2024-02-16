#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Split the line into page ID and linked pages
    page_id, links = line.strip().split(':')
    linked_page_ids = links.split()

    # Emit the page ID with a marker to indicate it has links
    print(f'{page_id}\t{"P"}')

    # Emit the linked page IDs with a marker to indicate they are linked to
    for linked_page_id in linked_page_ids:
        if linked_page_id != page_id:
            print(f'{linked_page_id}\t{"L"}')