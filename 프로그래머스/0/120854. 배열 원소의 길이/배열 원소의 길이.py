def solution(strlist):
    count = 0
    answer = []
    for s in strlist:
        for t in s:
            count +=1
        
        answer.append(count)
        count = 0

    return answer