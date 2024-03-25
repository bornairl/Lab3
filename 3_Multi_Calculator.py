#Sergio Maceda
#multi command calculator
#

print("Calculator")

sum = 0

while True:
    #1 Input
    x1 = input("Enter x1: ")
    x2 = input("Enter x2: ")
    op = input("Enter operator: ")

    #2 Process
    if op == "+":
        sum = int(x1) + int(x2)
    elif op == "-":
        sum = int(x1) - int(x2)
    elif op == "*":
        sum = int(x1) * int(x2)
    elif op == "/":
        sum = int(x1) / int(x2)
    for x in range(int(x1),int(x2)+1):
        sum += x

    #3. Output
    print(f"Sum: {sum}")
    res = input("Continue? (Yes/No) :")
    if res == "No":
        print("Exit")
        break;


    
