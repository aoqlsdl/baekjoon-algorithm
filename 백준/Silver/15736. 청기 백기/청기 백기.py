import math
import sys

# a_{1} = 0, a_{2} = 1, a_{3} = 1, a_{4} = 2, ..., a_{8} = 2, a_{9} = 3, ... a_{15} = 3, a_{16} = 4, ...
# 백기의 개수 = 루트 n
n = int(sys.stdin.readline())
print(int(math.sqrt(n)))