i=1
n=int(input("Enter the table o:"))
def table(i):
    if i>10:
        return
    else:
        print(n*i)
        table(i+1)
table(i)