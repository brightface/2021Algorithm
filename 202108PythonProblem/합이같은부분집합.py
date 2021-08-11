n = int(input())
flag = False
total = 0

def f(idx, sum):
    global flag
    if sum > (total/2): #아예 안나오는 경우
        return
    if flag == True:
        return
    if idx == n+1:
        if sum == (total-sum):
            flag = True
    else:
        # if idx<6:
        f(idx+1, sum+arr[idx])
        f(idx+1, sum)


if __name__== "__main__":
    arr = list(map(int,input().split(' ')))
    arr.append(0)
    print(arr)
    total = sum(arr)
    f(1,0)
    if flag:
        print("YES")
    else:
        print("NO")