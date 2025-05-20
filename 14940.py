from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
dist = [[-1]*m for _ in range(n)]

# 목표 지점 위치 찾기
target = None
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 0:
            dist[i][j] = 0  # 갈 수 없는 곳은 거리도 0
        if row[j] == 2:
            target = (i, j)
    grid.append(row)

# BFS 시작
q = deque()
q.append(target)
dist[target[0]][target[1]] = 0  # 시작점 거리 0

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

# 출력
for row in dist:
    print(' '.join(map(str, row)))
