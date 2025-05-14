import sys

# 입력 빠르게 받기
input = sys.stdin.readline

n = int(input())
members = []

for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))  # i: 입력 순서 저장

# 나이로 정렬, 같은 나이는 입력 순서(i)로 정렬
members.sort(key=lambda x: (x[0], x[1]))

for age, _, name in members:
    print(age, name)
