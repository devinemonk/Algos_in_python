#
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    p=int(input())
    a.sort()
    print(a[p-1])
