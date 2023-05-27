import sys

input = sys.stdin.readline #여러 줄로 입력 받음

s = set() #세트는 중복 없음. 순서 없음.
for i in range(int(input())) :
    name, status = input().split()

    if status == 'enter' :
        s.add(name)
    else :
        if name in s :
            s.remove(name)

for name in sorted(s, reverse=True) :
    print(name)

ppl = dict()

