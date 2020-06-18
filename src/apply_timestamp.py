"""
Prepend a timestamp to stdin stream messages
"""
import sys
import datetime


def prepend_timestamp(stdin_message):
    return f"[{datetime.datetime.now()}] {stdin_message}"


if __name__ == "__main__":
    for line in sys.stdin:
        line = prepend_timestamp(line)
        sys.stdout.write(line)
    sys.exit(0)
