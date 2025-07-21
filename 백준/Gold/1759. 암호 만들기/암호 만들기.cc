#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


/** 
 * 의사코드
 * 1. 문자를 리스트로 받아 알파벳 순으로 정렬한다.
 * 2. 재귀함수를 실행한다. 이때, params는 깊이(글자수), 문자, 배열로 구성
 * 2-1. 깊이 == L이면, 모음이 1개 이상이고 자음이 2개 이상인지 확인한 다음, 암호를 출력하고 재귀에서 빠져나온다.
 * 2-2. 깊이 != L이면 재귀함수에 (depth + 1)과 다음 문자를 전달한다.
 * 2-3. 재귀 함수 내에서는 리스트를 c번 순회한다.
 */

int L, C;
vector<char> words;

int cntVowel(string wo) {
	int cnt = 0;

	for (auto w : wo) {
		if (w == 'a' || w == 'e' || w == 'i' || w == 'o' || w == 'u') cnt++;
	}
	
	return cnt;
}

void recursive(int depth, int start, string temp) {
	if (depth == L) {
		int numVo = cntVowel(temp);
		
		if (numVo >= 1 && L - numVo >= 2) {
			cout << temp << "\n"; 
			return;
		}
	}

	for (int i = start; i < C; i++) {
		recursive(depth + 1, i + 1, temp + words[i]);
	}
}

int main() {
	// 입력
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> L >> C;
	
	char ch;
	for (int i = 0; i < C; i++) {
		cin >> ch;
		words.push_back(ch);
	};
	sort(words.begin(), words.end()); // 오름차순으로 정렬

	// 실행
	recursive(0, 0, "");

	return 0;
}