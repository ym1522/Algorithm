# 7785 - 회사에 있는 사람
# 메모리: 44448KB, 시간: 216ms
import sys

# ---------- 오답 ----------
# 근무 시간을 채워야 퇴근할 수 있다고 생각해 큐를 이용해 풀이
# but '아무때나 퇴근 가능'
from collections import deque
company = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    name, state = (sys.stdin.readline().split())
    if state == 'enter': company.append(name)
    elif state == 'leave': company.popleft()
list(company).sort(reverse=True)
print(*company, sep='\n')


# ---------- 정답 ----------
company = {}
n = int(sys.stdin.readline())

for _ in range(n):
    name, state = (sys.stdin.readline().split())
    if state == 'enter': company[name] = 0          # 회사에 있으면 0
    elif state == 'leave': company[name] = 1        # 퇴근했으면 1로 바뀜

tmp = []
for key, value in company.items():                  # 0인 경우만 tmp에 저장
    if value == 0: tmp.append(key)
    
tmp = sorted(tmp.keys(), reverse=True)
print(*tmp, sep='\n')


'''
<더 간결한 풀이>
  - 출입 했으면 딕셔너리에 저장하고
  - 퇴근 했으면 딕셔너리에서 삭제 !! 
'''