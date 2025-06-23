import calculator
import sys
print("This is my first Calculator project in Python")
print("---------Calculator-------")
while(True):
    print("What is the operation you want to do")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    
    s = str((input("Choose: ")))
    if(s == '5'):
        print("Exiting...")
        sys.exit()
    elif s in ('1','2','3','4'):
        try:
            x,y = float(input("Enter first value: ")),float(input("Enter second value: "))
        except ValueError:
            print("Invalid Input")
            continue
        try:
            if(s == '1'):
                ans = calculator.add(x,y)
            elif(s == '2'):
                ans = calculator.sub(x,y)
            elif(s == '3'):
                ans = calculator.mul(x,y)
            elif(s == '4'):
                ans = calculator.div(x,y)
            print(f"Ans->: {ans}")
        except ZeroDivisionError:
            print("Cant be divided by zero")
            continue
        
    else:
        print("Invalid Number!!!!!")

