# 2693 - N번째 큰 수
# 메모리: 30840KB, 시간: 68ms

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.sort(reverse=True)
    print(arr[2])