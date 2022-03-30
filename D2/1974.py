# [D2] 1974. 스도쿠 검증  2022-03-22

T = int(input())
for tc in range(1, T + 1):
    S = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    # 가로
    h = [0] * 10
    for i in range(9):
        for j in range(9):
            h[S[i][j]] += 1
            if 2 in h:
                ans = 0
        h = [0] * 10

    # 세로
    v = [0] * 10
    for j in range(9):
        for i in range(9):
            v[S[i][j]] += 1
            if 2 in v:
                ans = 0
        v = [0] * 10

    # 사각형
    q = [0] * 10
    for i in range(3):
        for j in range(3):
            q[S[i][j]] += 1
            if 2 in q:
                ans = 0
    q = [0] * 10

    for i in range(3):
        for j in range(3, 6):
            q[S[i][j]] += 1
            if 2 in q:
                ans = 0
    q = [0] * 10

    for i in range(3):
        for j in range(6, 9):
            q[S[i][j]] += 1
            if 2 in q:
                ans = 0
    q = [0] * 10

    for i in range(3, 6):
        for j in range(3):
            q[S[i][j]] += 1
            if 2 in q:
                ans = 0
    q = [0] * 10

    for i in range(3, 6):
        for j in range(3, 6):
            q[S[i][j]] += 1
            if 2 in q:
                ans = 0
    q = [0] * 10

    for i in range(3, 6):
        for j in range(6, 9):
            q[S[i][j]] += 1
            if 2 in q:
                ans = 0
    q = [0] * 10

    for i in range(6, 9):
        for j in range(3):
            q[S[i][j]] += 1
            if 2 in q:
                ans = 0
    q = [0] * 10

    for i in range(6, 9):
        for j in range(3, 6):
            q[S[i][j]] += 1
            if 2 in q:
                ans = 0
    q = [0] * 10

    for i in range(6, 9):
        for j in range(6, 9):
            q[S[i][j]] += 1
            if 2 in q:
                ans = 0
    q = [0] * 10

    print(f'#{tc} {ans}')