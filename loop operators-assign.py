# 1. break statement.
for i in range(1, 7):
    if i == 5:
        break
print(i)

# 2. pass satement.
for i in range(1, 7):
    if i == 5:
        pass  
    else:
        print(i)

# 3. continue statement.
for i in range(1, 7):
    if i == 5:
        continue  
    print(i)

# 4. for with else statement.
for i in range(1, 7):
    print(i)
else:
    print("Loop is completed!")

# 5. while with else statement.
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop is completed!")