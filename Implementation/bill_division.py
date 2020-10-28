#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    items = len(bill)
    total = 0
    for i in range(items):
        if i != k:
            total += bill[i]
    actual_payment = total / 2
    payment_diff = int(b - actual_payment)
    if payment_diff == 0:
        print("Bon Appetit")
    else:
        print(payment_diff)


if __name__ == "__main__":
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    print(bonAppetit(bill, k, b))
