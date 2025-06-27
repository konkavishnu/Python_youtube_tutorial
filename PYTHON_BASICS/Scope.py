name = 'vishnu'  # --> global scope
count = 1  # --> global scope


def greeting(firstname):  # --> note here the value passed below the function block is taken as parameter
    print("Welcome " + str(firstname))
    color = "blue"  # --> local scope
    print(name)  # -->  global scope
    print(color)


greeting("Harsha")  # --> python takes the parameter passed to the function as priority.


def another2():
    def greet(name):
        global count   # --> to assign a new value to the global variable globally in the entire code, we need to define it with the keyword 'global'
        count = count+1   # --> python will now call the variable with global keyword here and use it ,else it will make a copy of
        # the global variable and use it as local variable
        print(count)
        print("Welcome " + str(name))
    greet("Harsha")


def another():
    color_1 = "blue"

    def greet(name):
        count = 2   # --> python will create a copy of the global variable as local variable here and use it
        print(count)
        print("Welcome " + str(name))

    def inside():
        nonlocal color_1  # --> we should use 'nonlocal' keyword to access/manipulate a variable available within the -
        # scope of its main function where it is nested
        color_1 = "red"
        print(color_1)

    inside()
    greet("Harsha")  # --> python takes the parameter passed to the function as priority.


another()
another2()







