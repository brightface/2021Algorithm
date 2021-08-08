#include <iostream>
#include <math.h>
using namespace std;
bool check[1000010];

int main() {
    int n, m;
    cin >> n >> m;


    for (int j = 2; j <= m; j++) {
        for (int i = j * 2; i <= m; i += j) {
            if (check[i] == false) {
                check[i] = true;
            }

        }
    }
    check[1] = true;
    for (int i = n; i <= m; i++) {
        if (check[i] == false) {
            cout << i << " ";
        }
    }
    return 0;
}