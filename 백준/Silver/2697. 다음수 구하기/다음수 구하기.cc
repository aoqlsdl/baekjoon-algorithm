#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int t; 
	cin >> t;
	while (t--) {
		string s; cin >> s;
		if (next_permutation(s.begin(), s.end())) cout << s << '\n'; // 바로 다음 순열을 출력하는 STL
		else cout << "BIGGEST\n"; // 다음 순열이 없으면 BIGGEST
	}
}