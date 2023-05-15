import sys

n = int(sys.stdin.readline())
divisors = list(map(int, sys.stdin.readline().split()))

ans = min(divisors) * max(divisors) if len(divisors) > 1 else divisors[0] * divisors[0]
print(ans)