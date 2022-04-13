# [D2] 1976. 시각 덧셈  2022-04-13

T = int(input())
for tc in range(1, T + 1):
    H1, M1, H2, M2, = map(int, input().split())
    RM = M1 + M2
    if RM >= 60:
        H1 += 1
        RM -= 60
    RH = H1 + H2
    if RH > 12:
        RH -= 12

    print(f'#{tc}', RH, RM)
