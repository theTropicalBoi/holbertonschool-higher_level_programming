#!/usr/bin/python3
def islower(c):
    ascii = ord(c)
    if 97 <= ascii <= 122:
        return True
    else:
        return False
