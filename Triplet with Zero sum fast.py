def findTriplets(a, n):
    a.sort()
    for i in range(n-3):
        f=i+1
        l=n-1
        while f<l:
            x=a[i]+a[f]+a[l]
            if x==0:
                return 1
            elif x<0:
                f+=1
            else:
                l-=1
    return 0
