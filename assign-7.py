f=open("f.txt","a+t")
f.writelines(["\nrollno","\nname","\n","class"])
f.seek(0)
print(f.read())
print(f.readlines())
print(f.readline())

try:
    a=10
    b=0
    print(a/b)

except ZeroDivisionError:
    print("This is  arithmetic class")

except ArithmeticError:
    print("This is  arithmetic class")

except Exception:
    print("This is exception class")

finally:
    print("This is finally block")

print("This is outside the try-except block")