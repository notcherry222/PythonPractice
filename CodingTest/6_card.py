from collections import deque

de = deque()

for i in range(1, int(input("숫자를 입력하세요"))+1) :
    de.append(i)

while len(de)>1 :
    de.popleft()  #맨 위에 것 pop
    de.append(de.popleft())

print(de.pop())