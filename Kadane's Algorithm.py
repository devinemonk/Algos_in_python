#code
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    m=0
    p=-11111111111
    for i in a:
        p=max(p,i)
        s=s+i
        if s<0:
            s=0
        m=max(m,s)
    if p<0:
        m=p
    print(m)
