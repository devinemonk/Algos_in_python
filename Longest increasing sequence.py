#code
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l=[1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if a[j]<a[i]:
                l[i]=max(l[i],l[j]+1)
    print(max(l))
