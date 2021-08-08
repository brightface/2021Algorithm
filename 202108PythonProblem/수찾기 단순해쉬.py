import sys
sys.stdin = open("input.txt")

#멀리서 봐야한다. 단순하려면
n = int(input())
ntmp = list(map(int,input().split()))
#print(tmp)

m = int(input())
mtmp = list(map(int,input().split()))
#시간초과 코드 . 해쉬가 아닌가보네
# for i in range(m):
#     if mtmp[i] in ntmp:
#         print(1)
#     else:
#         print(0)

#해쉬
d= dict()
for i in ntmp:
    d[i] = 1
#print(d)

for i in mtmp:
    if i in d:
        print(1)
    else:
        print(0)
