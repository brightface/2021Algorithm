// 20210809최대공약수최소공배수.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//
#include <iostream>
using namespace std;


int gcd(int a, int b) {
	if (b == 0) return a;
	else {
		gcd(b, a%b);
	}
}
int lcd(int a, int b) {
	return (a*b) / gcd(a, b);
}

int main()
{
	int a, b;
	cin >> a >> b;
	cout << gcd(a, b) << endl;
	cout<< lcd(a, b);
    
}
