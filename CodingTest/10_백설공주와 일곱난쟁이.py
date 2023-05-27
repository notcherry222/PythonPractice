#9명중 진짜 7명 찾기
# 모자합이 100인 7명

from itertools import combinations

for i in combinations([int(input()) for _ in range(9)],7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break