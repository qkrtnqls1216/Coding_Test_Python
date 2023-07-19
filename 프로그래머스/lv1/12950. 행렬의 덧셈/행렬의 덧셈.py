def solution(arr1, arr2):
    answer=[] 
    for i in range(len(arr1)): # 배열의 행만큼 반복
        sum_1 = []
        for j in range(len(arr1[0])): # 배열의 열만큼 반복
            sum_1.append(arr1[i][j]+arr2[i][j]) # arr1과 arr2와 동일한 열에 있는 값을 더한 후 sum_1에 추가
        answer.append(sum_1) # 추가한 값을 answer 배열에 추가
    return answer