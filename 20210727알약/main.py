import sys
sys.stdin = open("input.txt")

while(True):
    n = int(input())
    if n == 0:
        break
    else:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for w in range(n+1):
            for h in range(n+1):
                if w < h :
                    continue
                elif w == 0 :
                    dp[w][h] = 1
                else:
                    dp[w][h] = dp[w][h-1] + dp[w-1][h]
        mx = -1
        for i in dp:
            if mx <max(i):
                mx = max(i)
        print(mx)
