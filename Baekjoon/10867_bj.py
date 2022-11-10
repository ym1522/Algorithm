# 10867 - 중복 빼고 정렬하기
# 메모리: 40596KB, 시간: 112ms
import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num = list(set(num))
num.sort()
print(*num, sep=' ')

'''
sort하고 set하면 틀림
왜 ??: set은 순서가 없기 때문에 !
'''