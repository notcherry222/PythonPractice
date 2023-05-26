# 1번부터 N번까지 원을 그리며 앉아 있음.
# 양의 정수 K(<=N)번째 사람을 순서대로 제거.
# (N, K) 입력시 순열 출력 코드 EX) (7, 3) -> <3, 6, 2, 7, 5, 1, 4>

N, K = map(int, input("N K 를 입력하시오 : ").split())

ppl = [i for i in range(1, N+1)]
ans = []
pt = 0

for _ in range(N):
    pt = pt+K-1
    pt %= len(ppl)
    ans.append(ppl.pop(pt))

print(f"<{','.join(map(str, ans))}>")   #f-string