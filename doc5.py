a=[1,2,2,5,8,4,4,8]
b=[ ]
i=0
count=0
while i<len(a):
    if a[i]not in b:
        b.append(a[i])
        count=count+1
    i=i+1
print("count","=",count)
        