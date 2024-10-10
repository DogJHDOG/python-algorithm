import sys
sys.setrecursionlimit(10 ** 6)

M, N = map(int, input().split())

arr = [[0 for j in range(N)] for i in range(M)]
dp = [[-1 for j in range(N)] for i in range(M)]  # 방문 체크 및 경로 수를 기록할 DP 배열
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 입력 받기
for i in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        arr[i][j] = data[j]

# DFS로 경로 수 찾기
def DFS(x, y):
    # 마지막 목적지에 도착한 경우
    if x == N - 1 and y == M - 1:
        return 1

    # 이미 계산된 경로가 있는 경우 캐시된 값 반환
    if dp[y][x] != -1:
        return dp[y][x]

    # 경로 수 초기화
    dp[y][x] = 0

    # 네 방향으로 이동
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        # 범위 밖인 경우 무시
        if tx < 0 or tx >= N or ty < 0 or ty >= M:
            continue

        # 내리막길로만 이동 가능
        if arr[ty][tx] < arr[y][x]:
            dp[y][x] += DFS(tx, ty)

    return dp[y][x]

# 시작점에서 DFS 호출
result = DFS(0, 0)
print(result)
