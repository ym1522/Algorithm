# 2822 - 점수 계산
# 메모리: 30840KB, 시간: 72ms

import sys
scores = []

# socres 리스트에 점수 저장
for i in range(1, 9):
    scores.append(int(sys.stdin.readline()))

# tmp에 scores 복사하고 상위 5개 점수만 남김
tmp = scores.copy()
tmp.sort(reverse=True)
tmp = tmp[:5]

# order에 몇 번째 점수인지 저장
order = []
for t in tmp:
    order.append(scores.index(t)+1)
order.sort()

print(sum(tmp))
print(*order)