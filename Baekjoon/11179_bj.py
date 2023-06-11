import sys

N = int(sys.stdin.readline())

N = list((bin(N)[2:]))
N.reverse()
N = int('0b' + ''.join(N), 2)

print(N)