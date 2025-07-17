#include <iostream>
using namespace std;

int main() {
	int N;
	// int 이용시 오류발생
	long long pn[91];
	
	cin >> N;

	pn[0] = 0;
	pn[1] = 1;
	pn[2] = 1;
	for (int i = 3; i <= N; i++) {
		pn[i] = pn[i - 1] + pn[i - 2];
	}

	cout << pn[N];

	return 0;
}