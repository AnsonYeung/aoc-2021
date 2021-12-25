#include <bits/stdc++.h>
using namespace std;

int main() {
    fstream infile("input.txt");
    while (infile) {
        string s;
        infile >> s;
        if (infile) {
            cout << s << endl;
        }
    }
    return 0;
}
