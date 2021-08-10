#include <iostream>
using namespace std;
int fiboarr[50] = { 0,1, };
int fibo(int N)
{
    if (N == 0 || N == 1)
        return fiboarr[N];
    else if (fiboarr[N] == 0) //dp의 핵심. 0이면 갱신이 안되었다는 뜻. 함수를 돌려 갱신하자.
        fiboarr[N] = fibo(N - 1) + fibo(N - 2);
    return fiboarr[N];
}
int main() {
    int T;
    cin >> T;
    int tmp;
    for (int i = 0; i < T; i++)
    {
        cin >> tmp;
        if (tmp == 0)
            cout << "1 0" << '\n';
        else
            cout << fibo(tmp - 1) << ' ' << fibo(tmp) << '\n';
    }
}