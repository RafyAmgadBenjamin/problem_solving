#!/bin/python3

import math
import os
import random
import re
import sys


def is_leap_year_Greogorian(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def is_leap_year_julian(year):
    return year % 4 == 0


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    day = 13
    if year == 1918:
        return "26.09.1918"
    if year >= 1919:
        if is_leap_year_Greogorian(year):
            day = 12
    else:
        if is_leap_year_julian(year):
            day = 12

    return f"{day}.09.{year}"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())
    print(dayOfProgrammer(year))

    # fptr.write(result + '\n')

    # fptr.close()
