#!/bin/python

import math
import os
import random
import re
import sys
import ast

#
# Complete the 'find_kth_largest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

import heapq
def find_kth_largest(nums, k):
    # Write your code here
    l = len(nums)
    K = l - k
    min_heap = []
    
    for i in nums:
        heapq.heappush(min_heap, i)
    
    while K>0:
        K -= 1
        x = heapq.heappop(min_heap)
    return heapq.heappop(min_heap)
    
    
    
if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        # Convert the line to list of lists
        nums, k = eval(line)
        result = find_kth_largest(nums, k)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()

