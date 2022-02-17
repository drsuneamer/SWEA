# 초심자의 회문 검사   2022-02-06

T = int(input())
for test_case in range(1, T+1):
	txt = input()
	result = 1 if txt == txt[::-1] else 0
    
	print(f'#{test_case} {result}')