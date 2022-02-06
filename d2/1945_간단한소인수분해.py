# 간단한 소인수분해  2022-02-06

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = [2, 3, 5, 7, 11]
    dict = {}
    i = 0

    while i <= len(nums)-1:
        if N % nums[i] == 0:
            N = N // nums[i]
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        elif nums[i] in  dict:
            i += 1
        else:
            dict[nums[i]] = 0
            i += 1
    
    result = ' '.join(map(str, list(dict.values())))
    print(f'#{test_case} {result}')