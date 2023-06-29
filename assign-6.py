    # 1)Create a function named ds with parameters roll_no and name.
def ds(roll_no, name):

    # 2)Add those parameters in the following data structures:
    my_list = [roll_no, name]
    my_tuple = (roll_no, name)
    my_set = {roll_no, name}
    my_dict = {'roll_no': roll_no, 'name': name}

    # Print the initial values
    print("Initial values:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Change values during runtime
    roll_no = 100  # Change roll_no
    name = "Yash"  # Change name

    # Update the values in the data structures
    my_list[0] = roll_no
    my_list[1] = name

    # Tuples are immutable, so you can't directly change the values
    # To change the values, you would need to create a new tuple
    my_tuple = (roll_no, name)

    my_set.remove(roll_no)
    my_set.add(100)  # Add new roll_no value

    my_dict['roll_no'] = roll_no
    my_dict['name'] = name

    # Print the updated values
    print("\nUpdated values:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Delete the data structures
    del my_list
    del my_tuple
    del my_set
    del my_dict

# Example usage of the ds function
ds(100, "Yash")
