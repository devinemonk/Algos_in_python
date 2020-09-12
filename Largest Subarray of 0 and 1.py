def maxLen(arr, N):
    for i in range(N):
        if arr[i]==0:
            arr[i]=-1
    d={}
    m=0
    s=0
    for i in range(N):
        s+=arr[i]
        if arr[i]==0 and m==0:
            m=1
        if s==0:
            m=i+1
        if s in d:
            m=max(m,i-d[s])
        else:
            d[s]=i
    return m
