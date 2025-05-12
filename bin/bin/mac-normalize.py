#!/usr/bin/env python3
"""
Normalize mac address to format: 'ff:ff:ff:ff:ff:ff'
"""

import argparse
import re
import sys

N = 2
RE_VALIDATE = re.compile(r"[a-zA-Z0-9]{12}")


def normalize(s):
    mac = s.lower()
    for char in ".-_: \n":
        mac = mac.replace(char, "")
    validate(mac)

    items = [mac[i:i+N] for i in range(0, len(mac), N)]

    for i in items:
        int(i, 16)
    return ":".join(items)


def validate(s):
    """Checks if `s` contains wrong symbols.

    >>> validate("0a1b2c3d4x5z")
    True
    >>> validate("0")
    Traceback (most recent call last):
    ...
    ValueError: too few symbols
    >>> validate("0а1б2ц334455")
    Traceback (most recent call last):
    ...
    ValueError: wrong symbols
    """

    if len(s) < 12:
        raise ValueError("too few symbols")

    if not RE_VALIDATE.match(s):
        raise ValueError("wrong symbols")

    return True


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("-i", action="store_true", help="read from stdin")
    p.add_argument("ADDRS", metavar="MAC", nargs="*", help="mac addresses")
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()

    macs = []

    if args.i:
        for line in sys.stdin:
            macs.append(line.strip())

    macs.extend(args.ADDRS)

    for m in macs:
        print(normalize(m))
