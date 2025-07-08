#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

/**
 * 의사코드
 * 1. k번 만큼 입력을 받고, 값을 확인한다.
 * 1-1. 값이 0이라면 vector 맨 끝에 있는 원소를 vector에서 제거한다
 * 1-1. 값이 0이 아니라면 vector 맨 뒤에 해당 값을 추가한다.
 * 2. vector 내부의 수를 모두 더한다.
 */
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	// 입력
	int k;
	vector<int> nums;

	cin >> k;

	// 실행
	for(int i = 0; i < k; i++) {
		int n;
		cin >> n;

		if (n == 0) {
			nums.pop_back();
		} else {
			nums.push_back(n);
		}
	}

	int res = accumulate(nums.begin(), nums.end(), 0);
	cout << res;
	
	return 0;
}