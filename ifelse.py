x = input("Enter first value : ")
y = input("Enter second value : ")
x = int(x)
y = int(y)
res = x+y
great = x
print("Sum : ", res)
if y>x:
    great = y
elif x>y:
    great = x
else:
    print("Values are equal")
print("The greatest value is : ", great)