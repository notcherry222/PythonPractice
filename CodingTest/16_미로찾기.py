import sys
N, M = int(input(sys.stdin.realine()).split())
def bfs(si, sj, ei, ej) :
    q = []
    v = [[0]*  M for _ in range(N)]

    q.append((si,sj))
    v[si][sj] = 1
    while q :
        ci, cj = q.pop(0)
        if(ci,cj) == (ei,ej) : #정답 처리가 필요한 경우 여기에서,,
            return v[ei][ej]

    #4방향 범위 내, 조건 맞으면 : arr ==1, v == 0
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)) :
            ni, nj = ci+di, cj+dj
            if 0<ni<N and 0<=nj<M and arr[ni][nj]==1 :
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1
arr = [list(map(int, input())) for _ in range(N)]
ans = bfs(0,0,N-1,M-1)
print(ans)