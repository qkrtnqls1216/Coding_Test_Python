def solution(phone_number):
    return "*"*(len(phone_number) - 4) + phone_number[-4:]
    # 1. phone_number의 길이에서 고정할 값인 4를 뺀만큼 * 생성
    # 2 .phone_number에서 나타내려고하는 4개의 숫자를 슬라이싱한다.
    # 1번과 2번을 결합한다.