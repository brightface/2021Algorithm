import sys
sys.stdin = open("input.txt")

A = list(input())
B = list(input())
A_len = len(A)
B_len = len(B)
A.insert(0,0)
B.insert(0,0)
max_len = max(A_len,B_len)
#현재 문자열을 비교하는 과정: 이전의 과정이 LCS[i-1][j], LCS[i][j-1]
LCS = [[0] * (max_len+1) for _ in range(max_len+1)]

for i in range(0,A_len+1):
    for j in range(0,B_len+1):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
print(LCS)
mx = -1
for i in LCS:
    if mx < max(i):
        mx = max(i)
print(mx)
