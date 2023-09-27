l=[3,5,7,5,8,1,9,99,89]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
        
print("list in ascending order",l)