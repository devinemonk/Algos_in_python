#code
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    s=int(input())
    dp=[]
    for i in range(n+1):
        dp.append([])
        for j in range(s+1):
            dp[i].append(0)
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(s+1):
            if j<a[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-a[i-1]]
    print(dp[-1][-1])
