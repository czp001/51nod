n=input()
do={}
d={}
for i in range(n):
    s=raw_input()
    do[s]=1
    ss=''.join(sorted(list(s)))
    if ss in d:d[ss]+=1
    else:d[ss]=1
q=input()
for i in range(q):
    s=raw_input()
    if s in do:tot=-1
    else:tot=0
    ss=''.join(sorted(list(s)))
    if ss in d:print d[ss]+tot
    else:print tot
