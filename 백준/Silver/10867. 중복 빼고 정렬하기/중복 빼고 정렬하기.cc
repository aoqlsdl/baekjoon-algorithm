#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	// 입력
	int N;
	cin >> N;

	set<int> s;
    int x;

	// 실행
    for (int i = 0; i < N; ++i) {
        cin >> x;
        s.insert(x);  // 자동 정렬 + 중복 제거
    }

    // set -> vector 변환
    vector<int> res(s.begin(), s.end());

	for (int i = 0; i < res.size(); i++) {
		cout << res[i] << ' ';
	}
    return 0;
}