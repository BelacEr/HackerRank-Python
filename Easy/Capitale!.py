# Problem: Capitalize!
# Difficulty: Easy
# Points: 20.00 points
# URL: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true   

#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    capitalized_words = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
