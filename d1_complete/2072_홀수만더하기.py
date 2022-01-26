# 2022-01-20

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    total = 0
    for i in numbers:
        if i % 2:
            total += i
    print(f'#{test_case} {total}')


''' 입력
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   
'''