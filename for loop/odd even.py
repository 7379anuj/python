# program for find odd even user input
n1=int(input("Enter the first number:"))
n2=int(input("Enter the last number:"))
def number(n1,n2):
    for i in range(n1,n2+1):
        if i%2==0:
            print("Even number is:",i)
        else:
            print("Odd number is:",i)
number(n1,n2)