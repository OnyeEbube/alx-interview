#!/usr/bin/python3
"""UTF-8 not UTF 8
"""


def validUTF8(data):
    """Checks for a valid UTF-8 encoding
    """
    try:
        data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
