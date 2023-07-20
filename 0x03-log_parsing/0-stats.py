#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""


import sys

def compute_metrics(lines):
    total_size = 0
    status_counts = {}

    for line in lines:
        line = line.strip()
        elements = line.split()

        if len(elements) == 7:
            ip, -, -, date, -, status_code, file_size = elements
            try:
                file_size = int(file_size)
                total_size += file_size

                status_counts[status_code
                        ] = status_counts.get(status_code, 0) + 1
            except ValueError: pass
    return total_size, status_counts

def print_statistice(total_size, status_counts):
    print(f"Total file size: (total_size)")

    sorted_status_code = sorted(status_counts.keys(), key=int)
    for status_code in sorted_status_codes:
        print(f"{status_code}: {status_counts[status_code]}")

if __name__ == "__main__":
    lines = sys.stdin.readlines()

    try:
        line_count = 0
        total_size = 0
        status_counts = {}

        for line in lines:
            line_count += 1

            if line_count % 10 == 0:
                total_size, status_counts = compute_metrics(lines[:line_count])
                print_statistics(total_size, status_counts)

        total_size, status_counts = compute_metrics(lines)
        print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        total_size, status_counts = compute_metrics(lines[:line_count])
        print_statistics(total_size, status_counts)
