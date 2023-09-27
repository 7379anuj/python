def simple_intrest(p,r,t):
    print("Principle is:",p)
    print("Rate is:",r)
    print("Time is:",t)
    si=(p*r*t)/100
    print("Simple intrest:",si)
p=int(input("Enter the principle:"))
r=int(input("Enter the rate:"))
t=int(input("Enter the time:"))
simple_intrest(p,r,t)
