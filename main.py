operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "=": lambda x, y: x == y
}

def cal():
    a = int(input("Enter the first number: "))
    operation = input("Choose operation (=, +, -, *, /): ")
    b = int(input("Enter the second number: "))

    if operation == "/" and b == 0:
        print("Division by zero. Try again")
        return cal()
    elif (operation != "=") and (operation != "+") \
            and (operation != "-") and (operation != "*") and (operation != "/"):
        print("Incorrect operator. Try again")
        return cal()
    elif 0 <= len(operation) > 1:
        print("Incorrect operator. Try again")
        return cal()
    else:
        return print("Result:", operations[operation](a, b))

cal()