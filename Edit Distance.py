
for _ in range(int(input())):
    n,m=map(int,input().split())
    a,b=map(str,input().split())
    
    dp=[]
    for i in range(n+1):
        dp.append([])
        for j in range(m+1):
            dp[i].append(0)
    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
    print(dp[-1][-1])
