s=input()
flag=0
for i in range(2,37):
    try:
        if int(s,i)%(i-1)==0:
            flag=1
            print(i)
            break
    except ValueError:
        continue
if flag==0:print('No Solution')
