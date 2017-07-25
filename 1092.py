def LCS(s1,s2):
    dp= [[0]*(len(s1)+5) for i in range(len(s2)+5)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])

    ans=''
    i,j=len(s1),len(s2)
    while i!=0 and j!=0:
        if dp[i][j]==dp[i-1][j]:
            i-=1
        elif dp[i][j]==dp[i][j-1]:
            j-=1
        else:
            ans+=s1[i-1]
            i-=1
            j-=1
    return ans
s1=raw_input()
s2=s1[::-1]
print len(s1)-len(LCS(s1,s2))
