def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n],x))
# strings를 x로 받아서 x의 n번째의 인덱스값을 기준으로 정렬시 원래의 값인 x(strings)를 기준으로 정렬하여 반환