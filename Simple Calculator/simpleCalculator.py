
print("Welcome to Andrews calculator! ")

def runTheProgram():
    
    x = int(input("Enter 1 to add, 2 to subtract, 3 to multiply, or 4 for division"))
    if x == 1:
        addition()
    if x==2:
        subtraction()
    if x==3:
        mul()
    if x==4:
        div()


def addition():
    print("You have chosen to do addition")
    print("Make sure to add a space between numbers EX: 22 23 23")
    nums = input("Enter numbers and I will add them for you: ")
    
    num_list = nums.split()
    numsum = 0

    for usernum in num_list:
        numsum += int(usernum)
    print("The result of your addition is: ", numsum)

def subtraction():
    print("You have chosen to do subtraction")
    print("Make sure to add a space between numbers EX: 22 23 23")
    nums = input("Enter numbers and I will subtract them for you: ")
    
    num_list = nums.split()
    numsum = 0

    for usernum in num_list:
        numsum -= int(usernum)
    print("The result of your subtraction is: ", numsum)

def mul():
    print("You have chosen to multiply")
    print("Enter Two numbers and they will be multiplied")

    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))

    print("The result is: ", num1*num2)

def div():
    print("You have chosen to divide")
    print("Enter Two numbers and they will be divided")

    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))

    print("The result is: ", num1/num2)      

runTheProgram()