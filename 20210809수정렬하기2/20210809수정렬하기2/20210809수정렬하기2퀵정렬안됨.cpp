#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int n=0;
	cin >> n;
	vector<int> arr;
	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		arr.push_back(tmp);
	}
	sort(arr.begin(), arr.end());
	for (int m : arr) {
		cout << m << endl;
	}
}
