# 2022-01-24

T = int(input())
for test_case in range(1, T + 1):
    lst = map(int, input().split())
    max_n = 0
    for i in lst:
        if i > max_n:
            max_n = i
    print(f'#{test_case} {max_n}')

''' 입력
3 
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   
'''