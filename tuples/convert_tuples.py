#convert list into tuples
l1=['Ram','Sham','3','4']
tup=tuple(l1)
print(tup)

# #program  for add item in tuples 
tup=("ram",'sham','3','5')
l2=list(tup)
l2.append("39")
tup=tuple(l2)
print(tup)

#program for remove item in tuples
tup=("ram",'sham','3','5')
l2=list(tup)
l2.remove('sham')
tup=tuple(l2)
print(tup)
