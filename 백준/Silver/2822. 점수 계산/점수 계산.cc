#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 내림차순 정렬
bool compare(pair<int, int> a, pair<int, int> b){
	return a.second > b.second;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	// 입력
	vector<pair<int, int> > score; 
	vector<int> selected;
	for(int i = 0; i < 8; i++) {
		int sco;
		cin >> sco;
		score.push_back(make_pair(i + 1, sco)); // {문제번호 : 점수}
	}

	// 실행
	int total = 0;
	sort(score.begin(), score.end(), compare);

	for (int i = 0; i < 5; i++) {
		total += score[i].second;
		selected.push_back(score[i].first);
	}

	sort(selected.begin(), selected.end());

	cout << total << "\n";
	for (int i = 0; i < 5; i++) cout << selected[i] << " ";
	return 0;
}