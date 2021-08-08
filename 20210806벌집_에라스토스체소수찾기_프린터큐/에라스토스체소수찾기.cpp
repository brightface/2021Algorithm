#include <iostream>
#include <math.h>
using namespace std;
bool check[1020];

int main() {
    int cnt;
    cin >> cnt;
    int answer = 0;

    for (int j = 2; j <= 1010; j++) {
        for (int i = j*2; i <= 1010; i += j) {
            if (check[i] == false) {
                check[i] = true;
            }
            
        }
    }
    check[1] = true;
    for (int i = 0; i < cnt; i++) {
        int tmp;
        cin >> tmp;
        if (check[tmp] == false) {
            answer++;
        }
    }
    cout << answer;
    return 0;
}