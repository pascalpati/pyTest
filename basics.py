#
#
# Python basics exercise code
#
# Have fun!

f = 2

# Class with basic methods
class myFirstClass():
    def method_1(self):
        print("This is method_1 of 1st class")

    def method_2(self, inputString):
        print("This is method_2 of 1st class " + inputString)

# Another class inheriting from myFirstClass
class mySecondClass(myFirstClass):
    def method_1(self):
        print("This is method_1 of 2nd class")

    def method_2(self):
        myFirstClass.method_2(self, "with string from 2nd class")
        print("This is method_2 of the 2nd class")

# Defining a func with no arguments
def func_1():
    print ("func_1" + " " + str(f))

# Defining a function accepting an argument
def cube(x):
    return x * x * x

# Defining a function accepting multiple arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# Define a func with usual if logic
def is_greater_1(x, y):

    if (x > y):
        return  x
    elif (x == y):
        return "Equal!"
    else:
        return y

# Define a func with python style if logic
def is_greater_2(x, y):
    if (x == y):
        return "Equal!"
    else:
        return x if (x > y) else y

# Define a func which contains a while loop
def func_whileLoop(x):
    while (x < 5):
        print(x)
        x += 1

# Define a func which contains a for loop
def func_forLoop(x, y):
    for r in range(x, y):
        print(r)

    sample_array = [6, 7, 8, 9, 10]
    for r in sample_array:
        print(r)
        if (8 == r):
            break

# main() function
def main():
    print(func_1)
    global f
    f = "string"
    print(str(0) + " " + f)
    print("Hello World!")


    # Print a global value
    print (f)

    # Function accepting a single argument
    print(cube(3))

    # Function accepting multiple arguments
    print(multi_add(1, 2, 3, 4, 5, 6))

    # Comparison function (Comparing the usual way)
    print(is_greater_1(1,1))

    # Comparison function (Comparing pythin way)
    print(is_greater_2(3,2))

    # Function to print input up to 5 times (while loop)
    func_whileLoop(0)

    # Function to print the numbers in the given range
    func_forLoop(0, 5)

    # Calling functions belong to a class
    firstClass = myFirstClass()
    firstClass.method_1()
    firstClass.method_2("with this input string!")

    # Calling overridden functions from 2nd class
    secondClass = mySecondClass()
    secondClass.method_1()
    secondClass.method_2()

# main() function
if __name__ == '__main__':
    main()





