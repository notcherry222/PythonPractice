# 집합 set
# 중복 안 됨. 순서 없음

java = {"재석","태호"}
python = set(["재석","명수"])

print(java & python) #합집합
print(java | python) #합집합
print(java.difference(python)) #차집합 = java-python

python.add("태호")
java.remove("태호")

##자료구조의 변경 - set, list ,tuple
menu = {"커피", "우유", "주스"}
menu = set(menu)
menu = list(menu)
menu = tuple(menu)

#1명은 치킨, 3명은 커피 쿠폰을 받음.
# 조건 : 20명이 참여. 아이디는 1~20.
# 무작위로 추첨하되 중복 불가. random모듈의 suffle과 sample을 사용.
# 예제: --당첨자 발표--
# 치킨 : 1 커피 : [2, 3, 4]
# --축하--

from random import *

id = [i for i in range(1, 21)]
shuffle(id)
winner= sample(id, 4)
print("--당첨자 발표--\n치킨 : "+ str(winner[0])+"\n커피 : "+str(winner[1:])+"\n--축하--") //str