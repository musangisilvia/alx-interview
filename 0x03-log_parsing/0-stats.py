#!/usr/bin/python3

"""
    Module: 0-stats
    Program to read log files
"""
import sys
import re

# Define the regex pattern with named capture groups
regex_pattern = r'^(?P<ip_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \- ' \
               r'\[(?P<date>\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] ' \
               r'\"(?P<request>GET \/projects\/\d+ HTTP\/1\.1)\" ' \
               r'(?P<status_code>\d+) (?P<file_size>\d+)$'

total_size = 0
status_code_counts = {}
i = 0

# Loop to read input lines
try:
    for line in sys.stdin:
        line = line.strip()  # Remove leading/trailing whitespace and newline
        match = re.match(regex_pattern, line)
        if match:
            ip_address = match.group('ip_address')
            date = match.group('date')
            request = match.group('request')
            status_code = match.group('status_code')
            file_size = match.group('file_size')

            total_size += int(file_size)

            # Update the status code count in the dictionary
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

        else:
            continue

        i += 1

        if i % 10 == 0:
            print('File size: {}'.format(total_size))
            # Sort the status code counts dictionary by key in ascending order
            sorted_status_codes = sorted(status_code_counts.items(),
                                         key=lambda x: int(x[0]))
            for code, count in sorted_status_codes:
                print('{}: {}'.format(code, count))

except KeyboardInterrupt:
    # Print the final file size and status code counts before exiting
    print('File size: {}'.format(total_size))
    # Sort the status code counts dictionary
    # by key in ascending order
    sorted_status_codes = sorted(status_code_counts.items(),
                                 key=lambda x: int(x[0]))
    for code, count in sorted_status_codes:
        print('{}: {}'.format(code, count))
    sys.exit(0)

# Print the final file size and status code counts
print('File size: {}'.format(total_size))
# Sort the status code counts dictionary by key in ascending order
sorted_status_codes = sorted(status_code_counts.items(),
                             key=lambda x: int(x[0]))
for code, count in sorted_status_codes:
    print('{}: {}'.format(code, count))
