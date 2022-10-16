# 1251 - 단어 나누기
# 메모리: , 시간:

'''
사전 순으로 제일 앞선 단어 s1 찾기 (s1 뒤에 두 글자 이상 있어야 함)-> s1이 첫 번째 단어
s1 이후에 있는 단어만 봤을 때 사전 순 제일 앞단어 찾기 (s2 뒤에 한 글자 이상 있어야 함)-> s2
제일 앞선 단어가 두 번 연속으로 나온다면??
'''

import sys

word = list(sys.stdin.readline().rstrip())
tmp = []
res=[]

for w in word[:-2]:
    if w == min(word[:-2]):
        index = word[:-2].index(w)+1
        tmp.append(word[:index])
        word = word[len(word[:index]):]
        break
for w in word[:-1]:
    if w == min(word[:-1]):
        index = word[:-1].index(w)+1
        tmp.append(word[:index])
        word = word[len(word[:index]):]
        break
tmp.append(word)
for t in tmp:
    t.reverse()
    res.append(t)
for r in res:
    print(*r, end='', sep='')