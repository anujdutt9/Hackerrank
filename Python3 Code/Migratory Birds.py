#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr.sort()
    result=Counter(arr)
    print(max(result, key=result.get))

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
