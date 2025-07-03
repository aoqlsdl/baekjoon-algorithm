#include <iostream>
#include <deque>
using namespace std;

/**
 * 의사 코드
 * 1. N이 1이 될 때까지 while문을 실행시킨다
 * 2. 반복문 내에서
 * 2-1. vector의 첫 번째 요소를 삭제하고
 * 2-2. 자동으로 첫 번째 요소가 되는 요소를 요소 맨 뒤로 뺀다.
 * 3. 반복문이 종료되면 남은 요소를 출력한다.
 */
int main() {
	// 입력
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	deque<int> cards;
	int N;

	cin >> N;

	for (int i = 0; i < N; i++) cards.push_back(i + 1);

	// 실행
	while (cards.size() > 1) {
		cards.pop_front(); // 제일 위 카드 버리기
		cards.push_back(cards.front()); // 그 다음 카드 맨 뒤로
		cards.pop_front();
	}

	cout << cards.front(); // 마지막 남은 카드 출력
	return 0;
}