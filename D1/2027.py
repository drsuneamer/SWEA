# 대각선 출력하기 2022-01-26

result = ['+', '+', '+', '+', '+']

for i in range(len(result)):
    result[i] = '#'
    print(''.join(result))
    result = ['+', '+', '+', '+', '+']
