def solution(n, k):
    total = n * 12000 + k * 2000
    discount = n // 10 * 2000
    answer = total - discount
    return answer