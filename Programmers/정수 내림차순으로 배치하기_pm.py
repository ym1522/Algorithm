# lv1 - 정수 내림차순으로 배치하기

def solution(n):
    answer = 0
    
    n = sorted(str(n), reverse=True)
    answer = int(''.join(n))
    
    return answer