def solution(answers):
    # 수포자들의 찍기 패턴
    P1 = [1, 2, 3, 4, 5]
    P2 = [2, 1, 2, 3, 2, 4, 2, 5]
    P3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자의 정답 개수를 저장할 변수 초기화
    count = [0, 0, 0]

    # 정답과 수포자의 패턴을 비교해서 정답 개수 계산
    for i in range(len(answers)):
        if answers[i] == P1[i % len(P1)]:
            count[0] += 1
        if answers[i] == P2[i % len(P2)]:
            count[1] += 1
        if answers[i] == P3[i % len(P3)]:
            count[2] += 1

    # 가장 많은 정답 개수
    max_count = max(count)

    # 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return
    return [i + 1 for i, c in enumerate(count) if c == max_count]
