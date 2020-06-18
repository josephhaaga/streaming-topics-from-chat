"""
Prepend a timestamp to stdin stream messages
"""
import sys
import datetime


def print_with_timestamp(stdin_message):
    return f"[{datetime.datetime.now()}] {stdin_message}"


if __name__ == "__main__":
    for line in sys.stdin:
        line = print_with_timestamp(line)
        sys.stdout.write(line)
