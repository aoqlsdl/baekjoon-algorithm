#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

/** 의사 코드
 * 1. n, m을 int로, 자연수는 리스트로 저장한다. *이때 자연수 리스트를 sorting한다.
 * 2. 출력할 set인 res, for문 내에서 사용할 리스트 arr를 각각 생성한다.
 * 3. m번 만큼 for문을 실행한다.
 * 4. for문 내에서 또 다른 for문을 실행하는데, 이때는 처음에 입력받은 자연수 리스트에 접근한다.
 * 4-1. for문 내의 depth < m이면 arr[depth] = 자연수 값으로 세팅한 후 재귀함수를 호출한다.
 * (이때 재귀함수 parameter: depth, m, arr 이정도?)
 * 4-2. for문 내의 arr의 길이 == m이면 arr를 res에 append하고 return한다.
*/

int n, m;
vector<int> numbers;
set<vector<int> > res;

void dfs(int depth, vector<int>& arr) {
    if (depth == m) {
        res.insert(arr); // 중복 제거를 위한 set
        return;
    }

    for (int i = 0; i < n; ++i) {
        if (depth == 0 || arr[depth - 1] <= numbers[i]) { // 비내림차순 조건
            arr[depth] = numbers[i];
            dfs(depth + 1, arr);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    numbers.resize(n);

    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    sort(numbers.begin(), numbers.end());

    vector<int> arr(m);
    dfs(0, arr);

    for (set< vector<int> >::iterator it = res.begin(); it != res.end(); ++it) {
        for (size_t i = 0; i < it->size(); ++i) {
            cout << (*it)[i] << " ";
        }
        cout << '\n';
    }

    return 0;
}