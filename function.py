import connection
from collections import Counter


def find_repeats(char,lst):
   count = 0
   for i in lst:
      if i == char:
          count += 1

   return count 