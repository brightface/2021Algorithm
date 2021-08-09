#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

int main() {
	queue<int> q;
	int n=0;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	
	//시작
	while (1) {
		if (q.size() >= 2) {
			q.pop(); //2 이상
		}
		else break; //1이하
		int tmp = q.front();
		q.pop();
		q.push(tmp);
	}
	cout << q.front();
}