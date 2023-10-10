squares=lambda x:x*x
num=int(input("Enter the first no:"))
num=int(input("Enter the last no:"))
for num in range(1,num+1):
    print(squares(num))