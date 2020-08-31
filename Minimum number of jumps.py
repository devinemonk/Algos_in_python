import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=[math.inf for i in range(n)]
    d[0]=0
    for i in range(n):
        for j in range(i+1,i+a[i]+1):
            if j<n:
                d[j]=min(d[j],d[i]+1)
    if d[-1]==math.inf:
        d[-1]=-1
    print(d[-1])
