# 2022 / 01 / 26

T = int(input())

result = 1
for num in range(T+1):
    if num == 0:
        print (1, end = ' ')
    else:
        result *= 2
        print (result, end = ' ')