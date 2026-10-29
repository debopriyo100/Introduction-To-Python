a = float(input("Enter the first Number: "))
b = float(input("Enter the second Number: "))

op = input("operator (+ - * / ** % //): ")

if op == "+":
    print = a+b
elif op == "-":
    print = a-b
elif op == "*":
    print = a*b
elif op == "/":
    if b == 0: print ("Any Number Divided by Zero Is Undifined")
    else: print = a/b
elif op == "**":
    print = a**b
elif op == "%":
    print = a%b
elif op == "//":
    print = a//b

else: print("Unknown Operator")