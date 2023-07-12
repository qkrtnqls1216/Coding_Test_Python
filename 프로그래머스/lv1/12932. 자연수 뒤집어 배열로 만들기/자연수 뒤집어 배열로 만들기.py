def solution(n):
    str_1 = str(n)[::-1] # 정수를 문자열로 바꾸고 슬라이싱을 사용하여 [start:stop:step]으로 start,stop생략하고 -1을 하면 문자열을 역순으로 바꿈 => 여긴 아직까지 문자열을 뒤집기만 한 상태
    arr_1 = [int(i) for i in str_1] # 뒤집은 문자열을 반복하면서 문자열을 정수로 바꾸고 배열형태로 다시 저장 => 리스트컴프리헨션
    return arr_1