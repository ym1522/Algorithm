# 5532 - 방학 숙제
# 메모리: 32952KB, 시간: 72ms

import sys, math
l = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

print(min(l - math.ceil(a/c), l - math.ceil(b/d)))