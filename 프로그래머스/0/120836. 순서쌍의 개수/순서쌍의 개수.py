def solution(n):
    count = 0
    for i in range(1, n//2+1):
        if n%i==0:
            count += 1
    answer = count + 1
    return answer