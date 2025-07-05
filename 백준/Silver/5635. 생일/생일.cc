#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

/**
 * 의사 코드
 * 0-1. map 자료형에 {이름: vector[연, 월, 일]} 형태로 저장한다.
 * 0-2. 가장 나이 적은/많은 사람 이름과 나이 변수를 각각 생성한다.
 * 1. for문을 돌면서 가장 나이 적은/많은 사람과 비교하고, 값을 갱신한다.
 * 1-1. 가장 먼저 연도를 비교하고,
 * 1-2. 연도가 같다면 월 -> 일 순서로 비교한다.
 */

// bool isFaster(int old, int chk) {
// 	if (int old < chk) {
// 		return false;
// 	}

// 	return true;
// }

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	// 입력
	int n; cin >> n;

    map<string, vector<int> > stu;

    for (int i = 0; i < n; ++i) {
        string name;
        int dd, mm, yy;
        cin >> name >> dd >> mm >> yy;

		stu[name].push_back(yy); stu[name].push_back(mm); stu[name].push_back(dd);
    }

	int old_y = 2011; int old_m = 0; int old_d = 0;
	int yng_y = 1989; int yng_m = 0; int yng_d = 0;
	
	string old_n = ""; string yng_n = "";

	for (auto s : stu) {
		if (s.second[0] < old_y
			|| (s.second[0] == old_y && s.second[1] < old_m )
			|| (s.second[0] == old_y && s.second[1] == old_m && s.second[2] < old_d)) {
			old_n = s.first;
			old_y = s.second[0]; old_m = s.second[1]; old_d = s.second[2];

			continue;
		}

		if (s.second[0] > yng_y
			|| (s.second[0] == yng_y && s.second[1] > yng_m)
			|| (s.second[0] == yng_y && s.second[1] == yng_m && s.second[2] > yng_d)) {
				yng_n = s.first;
				yng_y = s.second[0]; yng_m = s.second[1]; yng_d = s.second[2];
			}
	}

	cout << yng_n << '\n' << old_n << '\n';
	
	return 0;
}