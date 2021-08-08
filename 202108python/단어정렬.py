import sys
sys.stdin = open("input.txt")

n = int(input())
l = []
for i in range(n):
    l.append(input())
l = list(set(l))
l.sort(key = len)
#print(l)
# 시간초과

# for i in range(1,len(l)):
#     if len(l[i-1]) == len(l[i]):
#         k = i
#         while(len(l[i]) == len(l[i-1])):
#             if l[i-1] > l[i]:
#                 if l[i-1] > l[i]:
#                     l[i - 1], l[i] = l[i], l[i-1]
#                     i -= 1
#             else:
#                 break
# for i in range(len(l)):
#     print(l[i])

# voca_list = []
# for i in range(int(input())):  # 테스트케이스 수 입력
#     voca_list.append(input())  # 입력하는 단어를 리스트로 저장
#
# set_voca_list = list(set(voca_list))  # 리스트의 중복 제거
sort_voca_list = []

for j in l:
    sort_voca_list.append((len(j), j))  # 단어의 길이와 단어를 같이 리스트화 시켜 저장

sort_voca_list.sort()  # sort()는 len(j), j 에서 앞을 먼저 정렬후에 앞의 조건이 일치하면 뒤를 정렬한다.

for len_voca, voca in sort_voca_list:  # 리스트를 순환시켜 순서대로 출력
    print(voca)