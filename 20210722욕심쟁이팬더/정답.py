import sys
sys.stdin = open("input.txt")

n = int(input())
arr = []
arr.append([-1]*(n+2))
for i in range(n):
    t = list(map(int,input().split()))
    t.insert(0,-1)
    t.append(-1)
    arr.append(t)
arr.append([-1]*(n+2))
#print(arr)
dp = [[-1] * (n+2) for _ in range(n+2)]
#print(dp)
#상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]
# def dfs(y,x):
#     if dp[y][x] != -1:
#         return dp[y][x]
#     else:
#         for i in range(4):
#             ny,nx = y+dy[i], x+dx[i]
#             if arr[ny][nx] > arr[y][x]:
#                 dp[y][x] = max(dfs(ny,nx), dp[y][x])
#         dp[y][x] += 1
#         return dp[y][x]
# def dfs(y,x):
#     if dp[y][x] == -1:
#         dp[y][x] = 0
#         for i in range(4):
#             ny,nx = y+dy[i], x+dx[i]
#             if arr[ny][nx] > arr[y][x]:
#                 dp[y][x] = max(dfs(ny,nx), dp[y][x])
#         dp[y][x] += 1
#     return dp[y][x]
def dfs(i, j):
    if dp[i][j] < 0:
        dp[i][j] = 0
        for d in range(4):
            x, y = i+dx[d], j+dy[d]
            
            if 0<=x<n and 0<=y<n and arr[i][j] < arr[x][y]:
                dp[i][j] = max(dp[i][j], dfs(x, y))
        dp[i][j] += 1
    return dp[i][j]

answer = 0
for i in range(1,n+1):
    for j in range(1, n+1):
        answer = max(dfs(i,j),answer)

print(answer)
#

