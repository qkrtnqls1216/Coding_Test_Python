def solution(s):
    answer = len(s)

    for unit in range(1, len(s) // 2 + 1):
        word = ""
        comp = s[:unit]
        count = 1

        for i in range(unit, len(s), unit):
            current = s[i:i + unit]

            if comp == current:
                count += 1
            else:
                if count > 1:
                    word += str(count)
                word += comp
                comp = current
                count = 1

        if count > 1:
            word += str(count)
        word += comp

        answer = min(answer, len(word))

    return answer