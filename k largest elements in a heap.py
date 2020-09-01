#code
import heapq
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    heapq.heapify(a)
    print(*(heapq.nlargest(k,a)))
