class A:
    def __init__(self, a, b, c):
        self.__a = a  # private member
        self._b = b   # protected member
        self.c = c    # public member

    def display(self):
        print("Values in class A:")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)


class B(A):
    def display(self):
        print("Values in class B:")
        try:
            # Trying to access private member 'a' from the base class
            print("a:", self.__a)
        except Exception as e:
            print("Exception occurred:", e)
            print("Cannot access private member 'a'")
        print("b:", self._b)
        print("c:", self.c)


# Creating an object of class B and testing the display method
obj = B(1, 2, 3)
obj.display()
