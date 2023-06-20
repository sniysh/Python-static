# input from the user of 5 numbers
ls=[]
for i in range(5):
    num = int(input("Enter a number:"))
    ls.append(num)
print(num)

#Calculate the sum of all the elements in the list
sum_of_numbers = sum(ls)
print("Sum of all the numbers:", sum_of_numbers)
print(sum_of_numbers)

# Find the smallest number
smallest=min(ls)
print("Smallest number is:",smallest)
print(smallest)

# Find the largest number
largest=max(ls)
print("Largest number is:",largest)
print(largest)

# Display in ascending order
ascending_order = sorted(ls)
print("List in ascending order:", ascending_order)
print(ascending_order)

# Display in decending order
decending_order = sorted(ls,reverse=True)
print("List is decending order:",decending_order)
print(decending_order)

# Convert list into tuple
numbers_tuple = tuple(ls)
print("List converted to tuple:", numbers_tuple)
print(numbers_tuple)

# Delete the list
del ls
print("List is deleted")