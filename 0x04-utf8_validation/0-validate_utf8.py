#!/usr/bin/python3
"""UTF-8 not UTF 8
"""


def validUTF8(data):
    """Checks for a valid UTF-8 encoding
    """
    for num in data:
        if num not in range(256):
            return False
    try:
        data_bytes = bytes(data)
        data_bytes.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
