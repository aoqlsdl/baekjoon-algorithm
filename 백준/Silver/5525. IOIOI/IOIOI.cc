#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	// 입력
	int n, m; string str;
	cin >> n >> m >> str;

	// 문제 풀이
	int cnt = 0;
	for (int i = 0; i < m; i++) {
		
		int k = 0; // IOI의 개수
		if (str[i] == 'O') continue;

		while (str[i + 1] == 'O' && str[i + 2] == 'I') {
			k++;

			if (k == n) {
				cnt++;
				k--;
			}
			i += 2;
		}
	}

	cout << cnt;

	return 0;
}