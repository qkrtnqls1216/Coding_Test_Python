def solution(absolutes, signs):
    result = 0  # 결과값 저장할 변수
    for i in range(len(absolutes)): # absolutes길이만큼 반복
        if signs[i] == True:  
        # signs 리스트의 해당 인덱스 요소가 True인 경우
            result += absolutes[i] 
        else:
        # signs 리스트의 해당 인덱스 요소가 False인 경우    
            result -= absolutes[i]
    return result

# 문제풀이
# absolutes [4,7,12] signs [true,false,true]인 경우
# signs[0] = True -> result = 4
# signs[1] = False -> result = -3
# signs[2] = True -> result = 9
# 반환값 9