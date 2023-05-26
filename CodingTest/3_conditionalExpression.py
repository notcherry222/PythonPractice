a = [i for i in range(1,9)]

for i in a :
    even_or_odd = '짝' if i%2 == 0 else '홀'
    print(i,even_or_odd)

#리스트 컴프리헨션과 삼항 연산자를 같이 사용해서 리스트 초기화
b = [1 if j%2 else 0 for j in a]
print(b)