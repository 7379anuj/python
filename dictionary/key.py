#program for print key in dictionary
mydict={
    "name":"anuj",
    "grade":"9",
    "roll number":"5",
    "school":"M.M.S"
}
for key,value in mydict.items():
    print(key,":",value)
#program for print length of dict
dict={
    'name':'anuj',
    'grade':'9'
}
print(len(dict))
#program for print type
dict={
    'name':'anuj',
    'grade':'9'
}
print(type(dict))
#program for print item in dict
dict={
    'name':'anuj',
    'grade':'9'
}
for item in dict:
    print(item)


mydict ={
    'name':'Arun',
    'age':'15',
    'address':{
        'prement':'Rishikesh',
        'current':'Delhi',
    },
    'vechile':['car','track','bike','cycle']

}
print(mydict["address"]["current"])
print(mydict["vechile"][2])
mydict["age"]=19
print(mydict["age"])
