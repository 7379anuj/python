i=1
n=int(input("Enter the table o:"))
def table(i):
    if i>10:
        return
    else:
        print(i*i)
        table(i+1)
table(i)