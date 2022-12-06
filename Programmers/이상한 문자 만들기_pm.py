# lv1 - 이상한 문자 만들기

def solution(s):
    answer = ''
    tmp = list(s.split(' '))  # 공백 기준으로 split
    
    for t in tmp:
        for i, tt in enumerate(t):
            if i % 2 == 0: answer += tt.upper() # 단어에서 해당 문자의 자릿수가 짝수면 대문자를 answer에 더함
            else: answer += tt.lower()
        answer += ' '  # 한 단어가 끝날 때마다 띄어쓰기
        
    return answer[:-1]  # 마지막에 더해진 띄어쓰기는 제거