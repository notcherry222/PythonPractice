import sys

input = sys.stdin.readline
meeting=[]

for _ in range(int(input())):
    start, end = map(int, input().split())
    meeting.append((end, start))

meeting.sort()
t = 0
ans = 0


for end, start in meeting :
    if t <= start :
        ans += 1
        t = end

print(ans)
