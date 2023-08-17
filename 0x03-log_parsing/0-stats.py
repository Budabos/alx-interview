#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """

from sys import stdin

# init vaariables
total_file_size = 0
status_code_count_map = {}

try:
    # loop through the lines from the keyboard input
    for line_no, line in enumerate(stdin, start=1):
        line = line.strip()

        # tokenize the line read
        line_token: list = line.split()
        # print(line_token)  # for debug
        # print(len(line_token))
        if len(line_token) != 9:
            continue

        # destructure the tokenized line
        ip_address, _, _, _, _, _, request, status_code, file_size = line_token

        try:
            status_code = int(status_code)
        except ValueError:
            continue

        total_file_size += int(file_size)

        if status_code in status_code_count_map:
            status_code_count_map[status_code] += 1
        else:
            status_code_count_map[status_code] = 1

        if line_no % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_count_map.keys()):
                print(f"{code}: {status_code_count_map[code]}")

except KeyboardInterrupt as err:
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count_map.keys()):
        print(f"{code}: {status_code_count_map[code]}")
    print(err)
