#code
import math
total=256
count=[0]*(total+1)

def develope(s):
    n=len(s)
    for i in s:
        count[ord(i)]+=1
    for i in range(1,257):
        count[i]+=count[i-1]


def update(x):
    for i in range(ord(x),257):
        count[i]-=1


def find(s):
    z=list(s)
    if len(z)!=len(set(z)):
        return 0
    l=len(s)
    f=math.factorial(l)
    rank=1
    develope(s)
    for i in range(l):
        f=f//(l-i)
        rank+=count[ord(s[i])-1]*f
        update(s[i])
    return rank%1000003



for i in range(int(input())):
    n=input()
    print(find(n))
    
