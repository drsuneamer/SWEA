# 2022-01-23

T = int(input())
result = 0

while T > 0:
    i = T % 10
    result += i
    T = T // 10

print(result)

# 입력 : 6789