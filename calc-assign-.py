name=input("Enter your name:")
print("Enter two numbers:")
n1=float(input("Enter n1 :"))
n2=float(input("Enter n2 :"))
print("\nPlease select an operation!")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulo (%)")
print("6. Exponentiation (**)") 
print("7. Floor Division (//)")
operation = input("\nEnter the corresponding number:")
res = None
if operation == '1':
    res = n1 + n2
    operator = "+"
elif operation == '2':
    res = n1 - n2
    operator = "-"
elif operation == '3':
    res = n1 * n2
    operator = "*"
elif operation == '4':
    res = n1 / n2
    operator = "/"
elif operation == '5':
    res = n1 % n2
    operator = "%"
elif operation == '6':
    res = n1 ** n2
    operator = "**"
elif operation == '7':
    res = n1 // n2
    operator = "//"
else:
    print("Invalid operation!")
    exit()
    print("Name is:",name)
print(f"\n{n1} {operator} {n2} = {res}")