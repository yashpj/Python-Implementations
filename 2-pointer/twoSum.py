#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'two_sum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER target
#

def two_sum(numbers, target):
    # Write your code here
    l = len(numbers)
    left = 0
    right = l -1
    
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1
    return [-1,-1]
    
if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        numbers, target = eval(line)
        result = two_sum(numbers, target)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()