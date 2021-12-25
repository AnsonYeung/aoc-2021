#include <vector>
#include <iostream>
#include <tuple>
#include <algorithm>
using namespace std;

int main() {
    string s;
    vector<int> xcomp;
    vector<int> ycomp;
    vector<int> zcomp;
    vector<tuple<bool, int, int, int, int, int, int>> steps;
    while (getline(cin, s)) {
        // cout << "received: \"" << s << "\"\n";
        bool val = false;
        if (s.substr(0, 2) == "on") {
            val = true;
        }
        int x1, x2, y1, y2, z1, z2;
        sscanf(s.substr(s.find(' ') + 1).c_str(), "x=%d..%d,y=%d..%d,z=%d..%d", &x1, &x2, &y1, &y2, &z1, &z2);
        // cout << "parsed: " << val << ' ' << x1 << ' ' << x2 << ' ' << y1 << ' ' << y2 << ' ' << z1 << ' ' << z2 << '\n';
        xcomp.push_back(x1);
        xcomp.push_back(x2 + 1);
        ycomp.push_back(y1);
        ycomp.push_back(y2 + 1);
        zcomp.push_back(z1);
        zcomp.push_back(z2 + 1);
        steps.push_back(make_tuple(val, x1, x2 + 1, y1, y2 + 1, z1, z2 + 1));
    }

    sort(xcomp.begin(), xcomp.end());
    sort(ycomp.begin(), ycomp.end());
    sort(zcomp.begin(), zcomp.end());

    cout << xcomp.size() << ' ' << ycomp.size() << ' ' << zcomp.size() << '\n';
    vector<vector<vector<bool>>> res{xcomp.size(), {ycomp.size(), vector<bool>(zcomp.size(), false)}};

    auto bsearch = [] (const vector<int> &sortedVec, const int &val) {
        return lower_bound(sortedVec.begin(), sortedVec.end(), val) - sortedVec.begin();
    };

    for (const auto &[val, x1, x2, y1, y2, z1, z2]: steps) {
        int x1i = bsearch(xcomp, x1);
        int x2i = bsearch(xcomp, x2);
        int y1i = bsearch(ycomp, y1);
        int y2i = bsearch(ycomp, y2);
        int z1i = bsearch(zcomp, z1);
        int z2i = bsearch(zcomp, z2);
        for (int i = x1i; i < x2i; ++i) {
            for (int j = y1i; j < y2i; ++j) {
                for (int k = z1i; k < z2i; ++k) {
                    res[i][j][k] = val;
                }
            }
        }
    }

    long long result = 0;
    for (int i = 0; i < res.size(); ++i) {
        for (int j = 0; j < res[i].size(); ++j) {
            for (int k = 0; k < res[i][j].size(); ++k) {
                if (res[i][j][k]) {
                    result += (long long)(xcomp[i + 1] - xcomp[i]) * (ycomp[j + 1] - ycomp[j]) * (zcomp[k + 1] - zcomp[k]);
                }
            }
        }
    }

    cout << result << '\n';

    return 0;
}
