#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<string> inputs;
set<tuple<ll, ll, ll, ll, ll>> notOk;
ll mn = 100000000000LL;

ll dfs(ll ln, ll r0, ll r1, ll r2, ll r3) {
    if (notOk.find(make_tuple(ln, r0, r1, r2, r3)) != notOk.end()) {
        return -1;
    }
    map<char, ll> regs {{'x', r0}, {'y', r1}, {'z', r2}, {'w', r3}};
    for (ll i = ln; i < inputs.size(); ++i) {
        string inst = inputs[i].substr(0, inputs[i].find(' '));
        if (inst == "inp") {
            for (ll j = 9; j > 0; --j) {
                regs[inputs[i][4]] = j;
                ll result = dfs(i + 1, regs['x'], regs['y'], regs['z'], regs['w']);
                if (result != -1) {
                    cout << ln << ' ' << r0 << ' ' << r1 << ' ' << r2 << ' ' << r3 << '\n';
                    cout << j << '\n';
                    return result;
                }
            }
            notOk.insert(make_tuple(ln, r0, r1, r2, r3));
            return -1;
        } else {
            char op1 = inputs[i][4];
            ll op2 = inputs[i][6] >= 'a' ? regs[inputs[i][6]] : atoi(inputs[i].c_str() + 6);
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

int main() {
    string s;
    while (getline(cin, s)) {
        inputs.push_back(s);
    }

    dfs(0, 0, 0, 0, 0);

    return 0;
}
