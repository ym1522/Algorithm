# 1427 - 소트인사이드
# 메모리: 30840KB, 시간: 68ms

import sys

n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
print(*n, sep='')

'''
실버 5 문제인데 너무 쉽게 풀려서 당황..
'''