a = float(input())
operation = input()
b = float(input())
if operation == '/' and b == 0:
    print("Forbidden")
else:
    if operation == '+':
        print(a+b)
    elif operation == '-':
        print(a-b)
    elif operation == '*':
        print(a*b)
    elif operation == '/':
        print(a/b)
    elif operation == '^':
        print(a**b)
    else:
        print("Your calculator isn't smart enough for this")


