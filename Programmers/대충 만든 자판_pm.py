def solution(keymap, targets):
    answer = []
    dictionary = dict.fromkeys(range(65, 91), 0)
    
    for key in keymap:
        key = list(key)
        for k in key:
            if (dictionary[ord(k)] == 0):
                dictionary[ord(k)] = key.index(k)+1
            else:
                dictionary[ord(k)] = min(key.index(k)+1, dictionary[ord(k)])

    for target in targets:
        target = list(target)
        cnt, tmp = 0, 0
        for t in target:
            if dictionary[ord(t)] == 0:
                answer.append(-1); break
            else: 
                cnt += dictionary[ord(t)]; tmp += 1
        if len(target) == tmp: answer.append(cnt)
    
    return answer