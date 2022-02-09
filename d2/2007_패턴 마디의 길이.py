# 2022-02-09

T = int(input())
for tc in range(1, T+1):
    txt = input()
    for i in range(1, len(txt)):
        if txt[0:i] == txt[i:i*2]:
            print(i)
            break