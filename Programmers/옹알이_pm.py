# lv0 - 옹알이

def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    
    for tmp in possible:
        for i, baby in enumerate(babbling):
            if tmp in baby: 
                babbling[i] = baby.replace(tmp, '*')        # 옹알이 가능한 문자열이 존재하면 *로 대체
    
    for i, baby in enumerate(babbling):
        babbling[i] = baby.replace('*', '')                 # 위에서 대체했던 * 제거
    
    answer = babbling.count('')                             # 아무 값도 없는 원소이면 옹알이 가능이므로 count
    return answer

'''
레벨 0 치고는 조금 까다로웠던 것 같다.. 나만 그랬다면 머쓱
처음에는 옹알이 가능한 문자열이 있으면 *로 안바꾸고 바로 제거해버렸는데
'wyeoo'의 경우 'ye'를 제거하면 'woo'가 남아서 이것도 가능으로 count 해버림
'''