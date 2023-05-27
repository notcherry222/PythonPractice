#물은 왼쪽에서 정수만큼 떨어진 거리에서 샘
# 항승이는 물을 막을 건데, 테이프 길이는 L이며
# 좌우 0.5만큼 간격을 주고 테이프는 자를 수 없으며 겹쳐 붙일 수 있음
#테이프 최소 개수 구하는 프로그램
#입력 : 첫째줄에는 물새는 곳 개수 N과 테이프 길이 L이 주어짐
#둘째줄은 물이 새는 곳

#4 2
#1 2 100 101           #2

coord = [False]*1001
N, L= map(int, input().split())
for i in map(int, input().split()) :
    coord[i] = True     #막아야하는 구멍은 트루

ans = 0
x =0
while x<=1000 :
    if coord[x] :
        ans+=1
        x+=L  #테이프 길이만큼 뛰어넘기
    else: x+=1

print(ans)

