from itertools import groupby # 반복가능한 객체(itertools)의 연속된 원소들을 그룹화하기 -> 그룹화 결과 key값으로 반환

def solution(arr): 
    answer =  [k for k, _ in groupby(arr)] 
    # 배열 반복
    # _ 는 그룹화한 원소들의 순회가능한 값인 key값
    # groupby로 연속된 원소들을 같은 그룹으로 묶기
    return answer