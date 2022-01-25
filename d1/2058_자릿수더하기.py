# 자릿수 더하기   01 / 23 / 2022

T = int(input())
result = 0

while T > 0:
    i = T % 10
    result += i
    T = T // 10

print(result)

# 입력 : 6789