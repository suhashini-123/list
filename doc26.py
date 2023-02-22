a=[4,5,5,5,3,8]
i=0
while i<len(a)-1:
    k=a.count(a[i])
    if k==3:
        count=count+a[i]
    i=i+1
print(count)