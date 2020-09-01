#code
import heapq
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s1=0
    s2=0
    c=0
    heapq.heapify(a)
    while a:
        if c%2==0:
            s1=s1*10+heapq.heappop(a)
        else:
            s2=s2*10+heapq.heappop(a)
        c+=1
    #print(s1)
    #print(s2)
    print(s1+s2)
