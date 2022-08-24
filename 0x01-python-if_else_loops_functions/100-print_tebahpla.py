#!/usr/bin/python3
for char in range(26):
    print(
            "{}".format(chr(ord("z") - char) if char % 2 == 0
    else chr(ord("z") - 32 - char)), end=""i)
