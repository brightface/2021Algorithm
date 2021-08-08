import sys

sys.stdin = open("input.txt")

#dp[i] 는 i의 숫자가 주어지면 1이나 2나 3으로 자르는 더해서 나타낼수 있는 경우의수

#dp에서의 반복문은 dp 테이블을 채우기 위한 행위

def D(num):
    if num == 1:
        dp[num]=1
        return dp[num]
    elif num==2:
        dp[num]=2
        return dp[num]
    elif num==3:
        dp[num]=4
        return dp[num]
    else:
        dp[num] = D(num-1)+D(num-2)+D(num-3)
        return dp[num]

testCases = int(input())
while(testCases):
    testCases -= 1
    n = int(input())
    dp = [0]*(n+1)
    D(n)
    print(dp[n])