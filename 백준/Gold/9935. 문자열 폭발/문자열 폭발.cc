#include <iostream>
#include <string>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string s, b, t = "";

	cin >> s;
	cin >> b;

	for (int i = 0; i < s.size(); i++) { // s의 크기 만큼 반복
		t += s[i];

		if (t.back() == b.back()) { // t의 맨 뒤와 폭발문자열의 맨 뒤가 같다면
			bool ch = true;

			if (t.size() < b.size()) continue;

			for (int j = 0; j < b.size(); j++) { // 폭발문자열 길이만큼 반복
				if (t[t.size() - b.size() + j] != b[j]) {
					ch = false;
					break;
				}
			}
			if (ch) { // 폭발 문자열이 존재한다면
				for (int j = 0; j < b.size(); j++) t.pop_back();
			}
		}
	}

	if (t.empty()) {
		cout << "FRULA";
	} else {
		cout << t;
	}
	
	return 0;
}