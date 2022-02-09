# 숫자를 정렬하자 2022-02-10

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(N-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print(f'#{tc}', end = ' ')
    for i in nums:
        print(i, end = ' ')
    print()