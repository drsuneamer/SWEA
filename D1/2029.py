# 몫과 나머지 출력하기  2022-01-26

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())

    A = a // b
    B = a % b
    print(f'#{test_case} {A} {B}')