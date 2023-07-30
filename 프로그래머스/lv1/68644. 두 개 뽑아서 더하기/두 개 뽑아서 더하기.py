from itertools import combinations

def solution(numbers):
    answer = set()  # set을 사용하여 중복제거
    for num1, num2 in combinations(numbers, 2):
        answer.add(num1 + num2)
    
    return sorted(list(answer))  # answer을 리스트로 변환 후 정렬하여 반환