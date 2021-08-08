#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int solution(vector<int> priorities, int location) {
	int answer = 0;
	queue<pair<int, int>> p;
	priority_queue<int> pq;
	for (int i = 0; i < priorities.size(); i++) {
		p.push(make_pair(i, priorities[i]));
		pq.push(priorities[i]);
	}
	while (!p.empty()) {
		if (p.front().second != pq.top()) {
			pair<int, int> tmp = p.front();
			p.pop();
			p.push(tmp);
		}
		else {
			if (p.front().first == location) return ++answer;
			else {
				answer++;
				p.pop();
				pq.pop();
			}
		}
	}
	return answer;

}

int main() {
	int testCases;
	cin >> testCases;
	
	while (testCases--) {
		int cnt;
		vector<int> priorities;
		int location;
		cin >> cnt>>location;
		for (int i = 0; i < cnt; i++) {
			int tmp;
			cin >> tmp;
			priorities.push_back(tmp);
		}
		
		cout<<solution(priorities, location)<<endl;
		
		priorities.clear();
		vector<int>().swap(priorities);
	}
}