#include <iostream>
#include <string.h>
#include <stdio.h>
#include <vector>

using namespace std;
typedef long long LL;

LL Solve(LL a, LL b)
{
    vector<LL> v;
    for(LL i = 0; ;i++)
    {
        LL t = 2 * i * i + 2 * i + 1;
        if(t > b) break;
        v.push_back(t);
    }

    int cnt = 0;
    for(LL i = 1; i < v.size(); i++)
    {
        LL t = 2 * i * i + 2 * i + 1;
        LL x = v[i];
        if(t == x && t >= a)
            cnt++;
        if(x > 1)
        {
            for(int j = i; j < v.size(); j += x)
                while(v[j] % x == 0)
                    v[j] /= x;
            for(int j = x - i - 1; j < v.size(); j += x)
                while(v[j] % x == 0)
                    v[j] /= x;
        }
    }
    return cnt;
}

int main()
{
    LL a, b;
    while(cin >> a >> b)
        cout << Solve(a, b) << endl;
    return 0;
}
