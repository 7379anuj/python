#Program for calculater user input
operater=input("Enter operater:")
if operater=='+':
    num1=int(input("Enter the first no:"))
    num2=int(input("Enter the seecond no:"))
    print(num1+num2)
elif operater=='-':
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second no:"))
    print(num1-num2)
elif operater=='*':
    num1=int(input("Enter the first no:"))
    num2=int(input("Enter first no:"))
    print(num1*num2)
elif operater=='*':
    num1=float(input("Enter the first no:"))
    num2=float(input("Enter first no:"))
    print(num1*num2)
elif operater=='**':
    num1=int(input("enter first no:"))
    num2=int(input("enter second no:"))
    print(num1**num2)
elif operater=='/':
    num1=int(input("enter first no:"))
    num2=int(input("enter second no:"))
    print(num1/num2)
elif operater=='//':
    num1=int(input("enter first no:"))
    num2=int(input("enter second no:"))
    print(num1//num2)
elif operater=='^2':
    num1=int(input("enter first no:"))
   # num2=int(input("enter second no:"))
    print(num1*num1)

elif operater=='^3':
    num1=int(input("enter first no:"))
   # num2=int(input("enter second no:"))
    print(num1*num1*num1)
elif operater=='%':
    num1=int(input("enter value:"))
    num2=int(input("enter total value:"))
    print((num1/num2)*100)
    