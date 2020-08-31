#code
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    h=a[0]
    p=[0]
    for i in range(1,n):
        if a[i]>h:
            h=a[i]
            p.append(0)
        else:
            p.append(h-a[i])
    x=a[-1]
    q=[0]
    for i in range(1,n):
        if a[-i-1]>x:
            x=a[-i-1]
            q.append(0)
        else:
            q.append(x-a[-i-1])
    s=0
    for i in range(n):
        s+=min(p[i],q[-i-1])
    print(s)
    
