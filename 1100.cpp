#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e4 + 100;
struct st
{
    int x, y, pos;
}a[maxn];
bool cmp(st a, st b) {
    return a.x < b.x;
}
double xielv(st a, st b) {
    return (a.y-b.y)*1.0/(a.x-b.x);
}
int main() {
    int n, x, y;    
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d%d", &x, &y);
        a[i] = (st) {x, y, i+1};
    }
    sort(a, a+n, cmp);
    double maxxl = -1e9;
    int index = -1;
    for(int i=1; i<n; i++) {
        if(maxxl < xielv(a[i], a[i-1])) {
            maxxl = xielv(a[i], a[i-1]);
            index = i;
        }
    }
    if(a[index].x < a[index-1].x) printf("%d %d\n", a[index].pos, a[index-1].pos);
    else printf("%d %d\n", a[index-1].pos, a[index].pos);
    return 0;
}
