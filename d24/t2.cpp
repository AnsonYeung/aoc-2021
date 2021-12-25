#include <bits/stdc++.h>
using namespace std;
#define int long long

vector<string> inputs;
set<tuple<int, int, int, int, int>> notOk;
int mn = 100000000000LL;

int dfs(int ln, int r0, int r1, int r2, int r3) {
    if (notOk.find(make_tuple(ln, r0, r1, r2, r3)) != notOk.end()) {
        return -1;
    }
    map<char, int> regs {{'x', r0}, {'y', r1}, {'z', r2}, {'w', r3}};
    for (int i = ln; i < inputs.size(); ++i) {
        string inst = inputs[i].substr(0, inputs[i].find(' '));
        if (inst == "inp") {
            for (int j = 1; j <= 9; ++j) {
                regs[inputs[i][4]] = j;
                int result = dfs(i + 1, regs['x'], regs['y'], regs['z'], regs['w']);
                if (result != -1) {
                    cout << j << '\n';
                    return result;
                }
            }
            notOk.insert(make_tuple(ln, r0, r1, r2, r3));
            return -1;
        } else {
            char op1 = inputs[i][4];
            int op2 = inputs[i][6] >= 'a' ? regs[inputs[i][6]] : atoi(inputs[i].c_str() + 6);
            if (inst == "add") {
                regs[op1] += op2;
            } else if (inst == "mul") {
                regs[op1] *= op2;
            } else if (inst == "div") {
                regs[op1] /= op2;
            } else if (inst == "mod") {
                regs[op1] %= op2;
            } else if (inst == "eql") {
                regs[op1] = regs[op1] == op2 ? 1 : 0;
            }
        }
    }
    if (regs['z'] < mn) {
        mn = regs['z'];
        cout << "omg! " << mn << '\n';
    }
    if (regs['z'] != 0) {
        notOk.insert(make_tuple(ln, r0, r1, r2, r3));
        return -1;
    }
    return 0;
}

int32_t main() {
    string s;
    while (getline(cin, s)) {
        inputs.push_back(s);
    }

    dfs(0, 0, 0, 0, 0);

    return 0;
}
