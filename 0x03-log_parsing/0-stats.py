#!/usr/bin/env python3

import sys
import signal

# Initialize variables to hold statistics
total_file_size = 0
status_code_counts = {}

def print_statistics():
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        print(f"{code}: {count}")
    print()

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line_count, line in enumerate(sys.stdin, start=1):
        parts = line.strip().split()

        if len(parts) < 7:
            continue

        ip, _, _, _, _, status_code, file_size = parts

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        total_file_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    pass

print_statistics()

