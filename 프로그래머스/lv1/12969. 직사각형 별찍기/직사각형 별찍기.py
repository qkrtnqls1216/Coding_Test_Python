def solution(n,m):
    for i in range(m): # 세로길이 반복
        print('*' * n) # 가로에 *
        
a, b = map(int, input().strip().split(' ')) # 입력받아 공백으로 구분된 문자열을 정수로 변환        
solution(a,b)
