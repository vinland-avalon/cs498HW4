#!/usr/bin/env python3
import sys


for line in sys.stdin:
    # Split the line into page ID and linked pages
    _, links = line.strip().split(':')
    linked_page_ids = links.split()

    # Emit the linked page IDs with a marker to indicate they are linked to
    for linked_page_id in linked_page_ids:
            print(f'{linked_page_id}\t{"1"}')