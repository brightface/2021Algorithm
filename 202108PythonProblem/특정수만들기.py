n ,ans = map(int,input().split())
arr = list(map(int,input().split(' ')))
arr.append(0)
cnt = 0

def dfs(index, sum):
    global cnt
    if index >= n:
        if sum == ans:
            cnt +=1
    else:
        dfs(index+1, sum +arr[index])
        dfs(index+1, sum)
        dfs(index+1, sum -arr[index])
if __name__ == "__main__":
    dfs(0,0)
    print(cnt)
