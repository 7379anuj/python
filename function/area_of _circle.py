#program for area of circle user input
def circle(raduse):
    return 3.14*raduse*raduse
area=circle(int(input("Enter the raduse:")))
print("Area of circle is:",area)

#program for area of rectangle user input
def rectangle(length,breadth):
    return length*breadth
area=rectangle(int(input("Enter the length of rectangle:")),int(input("Enter the breadth of rectangle:")))
print("Area of rectangle is:",area)

#program for area of square user input
def square(side):
    return side*side
area=square(int(input("Enter the side of square:")))
print("Area of rectangle is:",area)