#!/bin/python3

import math
import os
import random
import re
import sys

"""If odd, print Weird
If even and in the inclusive range of 2 to 5, print Not Weird
If even and in the inclusive range of 6 to 20, print Weird
If even and greater than 20, print Not Weird"""

if __name__ == '__main__':
  n = int(input().strip())

if n % 2 > 0:
  print("Weird")
elif n % 2 == 0:
  if 2 <= n and n <=5:
    print("Not Weird")
  elif 6 <= n and n <= 20:
    print("Weird")
  elif n > 20:
    print("Not Weird")