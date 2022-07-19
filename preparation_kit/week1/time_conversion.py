#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
        time_slots = s.split(":")
        hours = time_slots[0]
        mins = time_slots[1]
        secs = time_slots[2][:2]
        day_slot = time_slots[2][-2:].lower()

        if hours == "12" and day_slot =="am":
            milit_hour = "00"
        elif day_slot == "pm" and hours != "12": 
            milit_hour =  str(int(hours) + 12) 
        else:
            milit_hour = hours

        res = f"{milit_hour}:{mins}:{secs}"

        return res

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
