import sys
sys.stdin = open("input.txt")
# arr = []
# n = int(sys.stdin.readline().rstrip())
# for i in range(n):
#     x = list(map(int, sys.stdin.readline().rstrip().split()))
#     arr.append(x)
# print(arr)

n = int(input())
arr = []
arr.append([0]*(n+2))
for i in range(n):
    t = list(map(int,input().split()))
    t.insert(0,0)
    t.append(0)
    arr.append(t)
arr.append([0]*(n+2))
print(arr)
dp = [[0] * (n+2) for _ in range(n+2)]
#print(dp)

for i in range(1,n+1):
    curY = i
    for j in range(1, n+1):
        curX = j
        #상하좌우
        if arr[curY+1][curX] > arr[curY][curX] and dp[curY+1][curX] >= dp[curY][curX]:
            dp[curY][curX] = dp[curY+1][curX] + 1
        if arr[curY-1][curX] > arr[curY][curX] and dp[curY-1][curX] >= dp[curY][curX]:
            dp[curY][curX] = dp[curY-1][curX] + 1
        if arr[curY][curX-1] > arr[curY][curX] and dp[curY][curX-1] >= dp[curY][curX]:
            dp[curY][curX] = dp[curY][curX-1] + 1
        if arr[curY][curX+1] > arr[curY][curX] and dp[curY][curX+1] >= dp[curY][curX]:
            dp[curY][curX] = dp[curY][curX+1] + 1
print(dp)
answer = -1
for i in dp:
    tmp = max(i)
    if tmp > answer:
        answer = tmp
print(answer+1)
#

