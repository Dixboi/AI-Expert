**Source: [HackerRank](https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true)**

**Task:**
Given an integer, , perform the following conditional actions: <br>
- If `n` is odd, print `Weird`
- If `n` is even and in the inclusive range of  to , print `Not Weird`
- If `n` is even and in the inclusive range of  to , print `Weird`
- If `n` is even and greater than , print `Not Weird`

**Input Format** <br>
A single line containing a positive integer, .

**Solution**
```python
import math
import os
import random
import re
import sys

def function(n):
    if (n%2 != 0) or (6 <= n <= 20):
        return "Weird"
    
    if (2 <= n <= 5) or (n > 20):
        return "Not Weird"     

if __name__ == '__main__':
    n = int(input().strip())
    print(function(n))
```
