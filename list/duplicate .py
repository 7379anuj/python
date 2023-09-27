#program for duplicate in list

l1=[2,4,2,5,4,7,1]
l2=[]
for i in l1:
    if i not in   l2:
        l2.append(i)
    else:
        print(i)

#program for duplicate in list
l1=[1,7,1,7,2,5,3]
my_dict=dict()
count=[]

for i in l1:
    my_dict[i]=0
for item in l1:
    for key,value in my_dict.items():
        if item==key:
            my_dict[key]=value+1
        j=0
for key,value in my_dict.items():
    if value>1:
        print(key)