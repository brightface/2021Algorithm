#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int k;
	cin >> k;

	
	int ans = 1;
	for (int i = 1; i <= k; i++) {
		int m = ((i * i) - i) * 3 + 1;
		if (ans < m ) {
			ans = i;
			break;
		}
	}
	cout << ans;

}