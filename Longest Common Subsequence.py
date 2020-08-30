#code
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=input()
    b=input()
    dp=[]
    for i in range(n+1):
        dp.append([])
        for j in range(m+1):
            dp[i].append(0)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    print(dp[-1][-1])
