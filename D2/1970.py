# [D2] 1970. 쉬운 거스름돈  2022-04-13

T = int(input())
for tc in range(1, T + 1):
    M = int(input())    # 주어진 금액
    i = 0

    Money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    Result = [0, 0, 0, 0, 0, 0, 0, 0]
    while M > 9:
        if M >= Money[i]:
            Result[i] += 1
            M -= Money[i]
        else:
            i += 1
    print(f'#{tc}')
    for r in Result:
        print(r, end=" ")
    print()