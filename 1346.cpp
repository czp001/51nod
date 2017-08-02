#include<cstdio>
#include<cstring>
#include<cctype>
#include<algorithm>
using namespace std;
#define rep(i,s,t) for(int i=s;i<=t;i++)
#define dwn(i,s,t) for(int i=s;i>=t;i--)
#define clr(x,c) memset(x,c,sizeof(x))
int read(){
    int x=0;char c=getchar();
    while(!isdigit(c)) c=getchar();
    while(isdigit(c)) x=x*10+c-'0',c=getchar();
    return x;
}
const int nmax=105;
const int maxn=131173;
int f[nmax][maxn],g[maxn][nmax];
int main(){
    rep(i,2,131172) {
        f[1][i]=read();
        if(i<=100) g[1][i]=f[1][i];
    }
    rep(i,2,131172){
        g[i][1]=read();
        if(i<=100) f[i][1]=g[i][1];
    }
    rep(i,2,100) rep(j,2,131172) f[i][j]=f[i][j-1]^f[i-1][j];
    rep(i,2,131172) rep(j,2,100) g[i][j]=g[i][j-1]^g[i-1][j];
    int t=read(),n,m;
    while(t--){
        n=read(),m=read();
        printf("%d\n",f[n][m+131072]^g[n+131072][m]);
    }
    return 0;
}
