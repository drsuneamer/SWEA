# [D4] 5247. 연산  2022-04-05

def bfs(n, m):
    q = [0] * 1000001
    v = [0] * 1000001
    front = -1
    rear = 0
    q[rear] = n
    v[n] = 0

    while front < rear:
        front += 1
        i = q[front]
        if i == m:
            return v[i]
        else:
            for k in [i + 1, i - 1, i * 2, i - 10]:
                if 0 < k <= 1000000 and v[k] == 0:
                    rear += 1
                    q[rear] = k
                    v[k] = v[i] + 1



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    a = bfs(N, M)
    print(f'#{tc} {a}')