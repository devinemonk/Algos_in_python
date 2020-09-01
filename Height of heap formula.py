#code
import math
for  _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    n=math.floor(math.log(n,2))
    print(n)
