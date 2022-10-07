# 9655 - 돌 게임
# 메모리 30840KB, 시간 68ms

'''
"완벽"하게 게임을 했다는 것은?
  - 한 번 가져갈 때 가져갈 수 있는 최대한으로 가져간다는 뜻으로 이해
'''

import sys

n = int(sys.stdin.readline())
cnt = 0

if n >= 3:
    cnt = n // 3
    n = n % 3
cnt += n

print('CY' if cnt % 2 == 0 else 'SK')