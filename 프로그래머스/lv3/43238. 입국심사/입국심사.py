def solution(n, times):
    answer = 0 # 시간의 최솟값 출력을 위한 변수 초기화
    min_time = 0; # 최소시간
    max_time = max(times)*n # 최대시간
    
    while min_time<=max_time: # 최소시간이 최대시간보다 작거나 같을 때까지 반복
        mid = (min_time+max_time)//2 # 중간시간 구하기
        people_count = 0 # 중간시간동안 처리가능한 사람 수 
        for t in times:
            people_count += mid // t
        if people_count >= n: # 처리가능한 사람의 수가 입국심사를 기다리는 사람보다 많은 경우
            max_time = mid-1
            answer = mid
        else:
            min_time = mid+1
    return answer