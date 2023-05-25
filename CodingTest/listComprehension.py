# 3원소가 8개인 리스트
a1 = [3]*8
a2 = [3 for i in range(8)]

#0~7 리스트
b1 = [*range(8)]
b2 = [i for i in range(8)]

print( "a1 = ", a1,"a2 = ", a2,"b1 = ", b1,"b2 = ", b2)

#10~17
c = [i + 10 for i in range(8)]
print("c = ", c)

#0~7 제곱
d = [i ** 2 for i in range(8)]
print("d = ", d)

#다차원 리스트 만들기(e1같은 방식은 지양!)
e1 = [[1]*4]*3
e2 = [[1]*4 for _ in range(3)]
e3 = [[1 for _ in range(4)] for _ in range(3)]
print("e1 = ", e1,"e2 = ", e2,"e3 = ", e3)