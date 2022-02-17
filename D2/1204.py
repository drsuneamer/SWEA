 
# [S/W 문제해결 기본] 1일차 - 최빈수 구하기   2022-02-06

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 개수 세기 위한 dictionary
    cnt = {}

    for n in nums:
        if n not in cnt:
            cnt[n] = 1
        else:
            cnt[n] +=1

    # 개수 dictionary 안에서 가장 큰 값을 가진 key (최빈수) 추출하여 list로
    result = [k for k, v in cnt.items() if max(cnt.values()) == v]

    # 문제에서 최빈수가 여러 개일 경우 가장 큰 값을 출력하라고 하였기에 추출된 값 중 가장 큰 값 출력
    print(f'#{test_case} {max(result)}')