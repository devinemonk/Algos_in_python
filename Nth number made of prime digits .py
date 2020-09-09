a=[2,3,5,7]
q=[2,3,5,7]
for i in range(25):
    for j in range(len(a)):
        q.append(q[i]*10+a[j])


for i in range(int(input())):
    print(q[int(input())-1])
