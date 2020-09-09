#code
for _ in range(int(input())):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    for i in range(1,n):
        if a[i]%2==0:
            c+=1
        a[i]+=a[i-1]
    #print(a)
    #print(c)
    for i in range(n):
        if a[i]%2==0:
                c+=1
        for j in range(1,i):
            if (a[i]-a[j-1])%2==0:
                #print(i,j)
                c+=1
            
    print(c)
