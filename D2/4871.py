# [D2] 4871. 그래프 경로  2022-04-03

def dfs(start, end):
    stack = []
    visited = [0] * (V+1)

    # 시작점 push 하고 시작
    stack.append(start)
    visited[start] = 1

    # stack 안에 값이 남아 있는 동안
    while stack:
        now = stack.pop()
        visited[now] = 1    # 방문 기록
        for new in range(1, V+1):
            # 연결되어있고 아직 방문하지 않았으면
            if visited[new] != 1 and arr[now][new]:
                # stack에 추가
                stack.append(new)

    # 도착 지점을 방문했으면 1
    if visited[end] == 1:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
    S, G = map(int, input().split())

    print(f'#{tc} {dfs(S, G)}')