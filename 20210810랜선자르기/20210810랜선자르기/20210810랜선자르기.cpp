// 20210810랜선자르기.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int k, n;
    cin >> k >> n;
    vector<int> arr;
    int sum = 0;
    int tmp;
    for (int i = 0; i < k; i++) {
        cin >> tmp;
        arr.push_back(tmp);
        sum += arr[i];
    }
    int ans = sum / n;
    int flag = 1;
    while (flag) {
        int cnt = 0;
        for (int i = 0; i < arr.size(); i++) {
            //int temp = 0;
            cnt += arr[i] / ans; 
        }
        if (cnt == n) { flag = 0; }
        else {
            ans--;
        }
    }
    cout << ans;
}
