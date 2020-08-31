import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n<=1:
        print("0")
    elif a[0]==0:
        print("-1")
    else:
        x=a[0]
        s=a[0]
        j=1
        f=-1
        for i in range(1,n):
            if i==n-1:
                f=j
                break
                
            x=max(x,i+a[i])
            s-=1
            if s==0:
                j+=1
                if i>=x:
                    f=-1
                    break
                s=x-i
        print(f)
                
                
                
