# 알파벳을 숫자로 변환  01 / 25 / 2022

alph = input()

crit = {'A':1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

for i in alph:
    a = ('crit[i], end = ''')

# 왠지 안되는 풀이
'''
alph = input()

for i in range(len(alph)):
    print(i+1, end = ' ')
'''