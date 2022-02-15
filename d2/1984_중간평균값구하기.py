# 중간 평균값 구하기 2022-02-15

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    cnt = 0
    for i in nums:
        cnt += 1

    for i in range(cnt-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    total = 0
    for i in range(1, cnt-1):
        total += nums[i]

    print(f'#{tc} {total // (cnt-2)}')
