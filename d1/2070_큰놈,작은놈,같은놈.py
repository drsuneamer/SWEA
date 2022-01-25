# 큰 놈, 작은 놈, 같은 놈   01 / 22 / 2022

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a > b:
        result = '>'
    elif a == b:
        result  = '='
    else:
        result = '<'
    print(f'#{test_case} {result}')

'''입력
3
3 8 
7 7 
369 123     
'''