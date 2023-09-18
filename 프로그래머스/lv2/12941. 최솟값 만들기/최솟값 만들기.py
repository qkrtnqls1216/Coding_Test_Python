def solution(A, B):
    answer = 0
    A.sort()  # A배열을 오름차순으로 정렬
    B.sort(reverse=True)  # B배열을 내림차순으로 정렬

    for i in range(len(A)): # A의 길이 만큼 반복 (A와B의 길이는 동일)
        answer += A[i] * B[i]

    return answer