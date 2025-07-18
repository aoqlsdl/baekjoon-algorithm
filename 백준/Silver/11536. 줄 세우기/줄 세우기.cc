#include <iostream>
#include <vector>
using namespace std;

int n, stat = 2;
vector <string> s;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
    s.resize(n);
	for(int i = 0; i < n; i++) cin >> s[i];

	for(int i = 1; i < n; i++) {
		if(s[i - 1] < s[i]) {
			if(stat == -1) stat = 0;
			else if(stat == 2) stat = 1;
		}
		else {
			if (stat == 1) stat = 0;
			else if (stat == 2) stat = -1;
		}
	}
	
	if (stat == -1) cout << "DECREASING";
	else if (stat == 0) cout << "NEITHER";
	else cout << "INCREASING";
}