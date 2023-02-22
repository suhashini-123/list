# a=int(input("enter the num"))
# i=0
# while i<a:
#     tens=a%10000
#     ones=a%1000
#     hundreds=a%100
#     tens=a%10
#     ones=a%1
#     i=i+1
# print(a-tens,"+",tens-ones,"+",hundreds-tens,"+",tens-ones)

# a=int(input("enter the num"))
# i=1
# while i<=a:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",i*j)
#         j=j+1
#     i=i+1  

# i=1
# while i<=10:
#     i=i+1
#     if i==6:
#         continue
#     print(i*i) 

# a=["red","maroon","yellow","olive"]
# b=[]
# i=0
# while i<=len(a)-1:
#     c=a[i]
#     d=[]
#     j=0
#     while j<len(c):
#         d.append(c[j])
#         j=j+1
#     b.append(d)
#     i=i+1
# print(b)

# a=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83] 
# i=0
# b=[]
# while i<len(a):
#     c=[a[i],a[i+1],a[i+2]]
#     b.append(c)
#     i=i+3
# print(b)

# a=[10,20],[30,40],[50,60],[30,20,80]
# b=[[61],[12,14,15],[12,13,19,20],[12]]
# i=0
# c=[]
# while i<len(a):
#     d=a[i]+b[i]
#     c.append(d)
#     i=i+1
# print(c)             
        
        
# a=[["g","f","g"],["i","s"],["b","e","s","t"]]
# i=0
# b=""
# while i<len(a):
#     c=a[i]
#     j=0
#     while j<len(c):
#         k=c[j]
#         b=b+k
#         j=j+1
#     i=i+1
# print(b)  

# a=[29,34,5,8,1,30]
# i=0
# m1=0
# m2=0
# m3=0
# while i<len(a):
#     if a[i]>m1:
#         m1=a[i]
#     i=i+1
#     j=0
#     while j<len(a):
#         if a[j]<m1 and a[j]>m2:
#             m2=a[j]
#         j=j+1
#     k=0
#     while k<len(a):
#         if a[k]<m2 and a[k]>m3:
#             m3=a[k]
#         k=k+1
# print(m1)
# print(m2)
# print(m3) 

# a=[1,5,23,7,4]
# i=0
# max=0
# min=a[0]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     elif a[i]<min:
#         min=a[i]
#     i+=1
# print(max)
# print(min)

# a=[1,1,2,3,4,4,5,1]
# i=0
# b=[]
# while i<len(a)-1:
#     count=1
#     if a[i]==a[i+1]:
#         count=1
#         d=[count,a[i]]
#         b.append(d)
#     else:
#         b.append(a[i])
#     i=i+1
# b.append(a[-1])
# print(b)

# l=[1,2,3]
# for i in range(len(l)):
#     for j in range(len(l)):
#         for k in range(len(l)):
#             if (i!=j and j!=k and i!=k):
#                 print(l[i],l[j],l[k])
               
    
            
            
                                    
            
              

        
        
    
        
        