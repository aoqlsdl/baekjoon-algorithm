#include <string>
#include <vector>

using namespace std;

int isZero(int m) {
    if (m == 0) {
        return 1;
    } else {
        return 0;
    }
}

string solution(string code) {
    string answer = "";
    int mode = 0;
    
    for (int idx=0; idx < code.size(); idx++) {
        if (isZero(mode)) {
            if (code[idx] == '1') {
                mode = 1;
            } else if (idx % 2 == 0) {
                answer += code[idx];
            }
        } else {
            if (code[idx] == '1') {
                mode = 0;
            } else if (idx % 2 != 0) {
                answer += code[idx];
            }
        }
    }
    
    if (answer.size() == 0) {
        answer = "EMPTY";
    }
    return answer;
}