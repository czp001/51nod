from heapq import *
n=input()
cnt,hd=1,[]
for i in range(n):
    hd.append(map(int,raw_input().split()))
hd.sort()
heap=[]
heappush(heap,hd[0][1])
for i in range(1,n):
    x=heap[0]
    if hd[i][0]<x:
        cnt+=1
        heappush(heap,hd[i][1])
    else:
        heappop(heap)
        heappush(heap,hd[i][1])
print(cnt)
