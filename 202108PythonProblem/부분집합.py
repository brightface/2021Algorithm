n = int(input())
check = [0] * (n + 2)
def f(index): #n은 들어갈 인덱스
    if index == n+1:
        for i in range(1,n+1):
            if check[i] == 1:
                print(i , end=' ')
        print()

    else:
        check[index] = 1 #넣었으니까 1한다
        f(index+1)
        check[index] = 0 #넣은후 다시 빼야하니 0 한다.
        f(index+1)

if __name__ == "__main__":
    f(1)


    