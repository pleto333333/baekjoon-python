import sys

# 입력 수 N
N = int(sys.stdin.readline())

# 점들을 리스트에 저장
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 정렬: x좌표 기준, 같으면 y좌표 기준
points.sort(key=lambda p: (p[0], p[1]))

# 출력
for x, y in points:
    print(x, y)
