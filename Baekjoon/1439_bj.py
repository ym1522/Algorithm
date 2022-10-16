# 1439 - 뒤집기

import sys

s = list(sys.stdin.readline().rstrip())
ss = len(s)  # 이거 안하면 무한루프 안끝남 ㅠㅠ
print(len(s))
print(s)

i = 0
while i < ss:
    if s[i] != s[i+1]: s.insert(i+1, ''); i += 2
    else: i += 1
    
print(s)

# sp = '1' if s.count('0') <= s.count('1') else '0'  # 갯수가 아니라 연속되는 구간의 갯수가 더 많은 것을 골라야 함...
# tmp = s.split(sep=sp)
# print(len(tmp) - tmp.count(''))