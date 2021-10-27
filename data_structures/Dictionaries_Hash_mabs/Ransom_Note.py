#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

from collections import Counter


def checkMagazine(magazine: list, note: list):
    # try:
    #     return "Yes" if [magazine.remove(word) for word in note] else "No"
    # except:
    #     return "No"

    # for word in note:
    #     if not word in magazine:
    #         print("No")
    #         return
    #     magazine.remove(word)
    # print("Yes")

    # pass
    # Write your code here

    magazine = Counter(magazine)
    note = Counter(note)

    for word in note:
        if magazine[word] < note[word]:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
