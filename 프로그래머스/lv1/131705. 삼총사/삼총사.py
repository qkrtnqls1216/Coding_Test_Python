from itertools import combinations
#  itertools 모듈에서 제공하는 함수 combinations
# combinations:  주어진 길이의 조합을 생성하는 함수
def solution(number):
    count = 0  # 삼총사를 만드는 방법

    # 학생 3명의 조합
    for comb in combinations(number, 3):
        # 조합에 포함된 학생들의 정수 번호 더하기
        if sum(comb) == 0: # 조합의 합이 0인 경우
            count += 1

    return count
