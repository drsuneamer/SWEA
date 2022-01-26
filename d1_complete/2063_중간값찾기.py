# 2022-01-26

T = int(input())
lst = list(map(int, input().split()))
lst.sort()

cnt = 0
for i in lst:
    cnt += 1
num = cnt // 2

print(lst[num])