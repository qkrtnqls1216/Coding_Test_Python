def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command  # i, j, k 값 저장
        sub_array = array[i-1:j]  # i번째부터 j번째까지의 부분 배열을 자르기
        sub_array.sort()  # 부분 배열을 오름차순으로 정렬
        answer.append(sub_array[k-1])  # 정렬된 부분 배열에서 k번째 숫자를 answer 배열에 추가
    return answer