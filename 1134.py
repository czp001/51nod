def find(a,length,n):
    left=0;right=length
    while(left<=right):
        mid=int((right+left)/2)
        if a[mid]<n:
            left=mid+1
        else:
            right=mid-1
    return left

def func(s):
    le=[]
    le.append(s[0])
    for i in s:
        if le[-1]<i:
            le.append(i)
        else:   
            left=find(le, len(le), i)

            le[left]=i
    print(len(le))
    
leng=int(input())
s=[]
for i in range(leng):
    s.append(int(input()))
func(s)
