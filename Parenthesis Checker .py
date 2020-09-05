#code
for _ in range(int(input())):
    d={}
    d['}']='{'
    d[')']='('
    d[']']='['
    a=[]
    f=0
    s=input()
    for i in s:
        if i in ['{','(','[']:
            a.append(i)
        else:
            if a:
                if d[i]==a[-1]:
                    a.pop()
                else:
                    f=1
                    break
            else:
                f=1
                break
    if f==1 or len(a)>=1:
        print("not balanced")
    else:
        print("balanced")
