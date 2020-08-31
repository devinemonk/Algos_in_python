for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    if s%2!=0:
        print("NO")
    else:
        dp=[]
        s=s//2
        for i in range(n+1):
            dp.append([])
            for j in range(s+1):
                dp[i].append(False)
        for i in range(n+1):
            dp[i][0]=True
        for i in range(1,n+1):
            for j in range(1,s+1):
                if j<a[i-1]:
                    dp[i][j]=dp[i-1][j]
                if j>=a[i-1]:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-a[i-1]]
        if dp[-1][-1]==True:
            print("YES")
        else:
            print("NO")
            
