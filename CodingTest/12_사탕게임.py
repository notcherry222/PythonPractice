#n*n 크기의 보드에 색이 다른 사탕이 채워져 있다.
# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 있고, 한 번 인접한 사탕의 위치를 바꿀 수 있다.
# 인접한 같은 색의 사탕을 먹을 수 있을 때 최대 개수를 구하라.

n = int(input())
board = [list(input()) for _ in range(n)]
ans =1
def search():
    global ans
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j-1] == board[i][j] :
                cnt +=1
                ans = max(ans,cnt)
            else : cnt =1

    for j in range(n):
        cnt = 1
        for i in range(1,n):
            if board[i-1][j] == board[i][j]:
                cnt+=1
                ans = max(ans,cnt)
            else : cnt=1

for i in range(n) :
    for j in range(n):
        if j+1<n:
            board[i][j], board[i][j+1] == board[i][j+1], board[i][j]
            search()
            board[i][j], board[i][j + 1] == board[i][j + 1], board[i][j] #원상복구

        if i+1<n:
            board[i][j], board[i+1][j] == board[i+1][j], board[i][j]
            search()
            board[i][j], board[i+1][j] == board[i+1][j], board[i][j]

print(ans)