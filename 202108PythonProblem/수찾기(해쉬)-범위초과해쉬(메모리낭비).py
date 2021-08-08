import sys
sys.stdin = open("input.txt")

check = [0]*(100010)
n = int(input())
ntmp = list(map(float,input().split()))
#print(tmp)
for i in range(len(ntmp)):
    check[ntmp[i]] = 1.0

m = int(input())
mtmp = list(map(float,input().split()))
for j in range(len(mtmp)):
    if check[mtmp[j]] == 1.0:
        print(1)
    else:
        print(0)