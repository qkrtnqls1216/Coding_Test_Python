def solution(s, n):
    answer = ''
    for char in s: # s의 길이 만큼 반복
        if 'A' <= char <= 'Z': # 'A'~'Z'사이일 경우
            new = chr((ord(char) - ord ('A') + n) % 26 + ord('A'))
        elif 'a' <= char <= 'z': # 'a'~'z'사이일 경우
            new = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        else:
            new = char
        answer += new
    return answer

# ord 함수는 문자를 ASCII 코드 값으로 변환
# chr()은 정수 형태의 ASCII 코드 값을 해당하는 문자로 변환하는 Python의 내장 함수