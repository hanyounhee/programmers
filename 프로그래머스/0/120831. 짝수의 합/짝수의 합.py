def solution(n):
    count = 1
    sum1 = 0
    while n >= count:
        if count % 2 == 0:
            sum1 += count
        count += 1
    answer = sum1
    return answer