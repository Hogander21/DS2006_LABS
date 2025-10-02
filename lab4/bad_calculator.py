print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation: ")
userChoice = input("(1) Add two numbers \n(2) Subtract two numbers\n(3) Multiply two numbers\n(4) Divide two numbers: \n")


firstNumber = input("Type the first number: ") 
secondNumber = input("Type the second number: ")

match str(userChoice): # Dosent take the str - use int

    case 1:
        total = firstNumber + secondNumber
        print(f"The addition of {firstNumber} + {secondNumber} is {total} ")
    case 2:
        total = firstNumber - secondNumber
        print(f"The subtraction of {firstNumber} + {secondNumber} is {total} ")
    case 3:
        total = firstNumber * secondNumber
        print(f"The multiplication of {firstNumber} + {secondNumber} is {total} ")
    case 4:
        total = firstNumber / secondNumber
        print(f"The division of {firstNumber} + {secondNumber} is {total} ")
    case _:
        print("Invaild menu choice")
'''
Problems with this code:
1: The first problem is the type of input in "firstNumber" and "secondNumber", 
this input will return a str and will not work. It should take the inputs as floats
to cover all of the type of inputs possible.

2: 
The firstNumber variable is wrong from the beginning and named firsNumber, this 
will make the code throw an NameError. The correct name is firstNumber

3: 
The match statement should take an int to be able to match to the different cases.
Now it takes str and would be able to match.

4: 
In the print statements show an '+' in all of the statements, this should be changed to 
the right operator like this: 
Addition: +
Subtration: -
Multiplication: *
Division: /

5: 
The next problem is the division operator in case 4, the total calcuation, right now it does 
floordivison and it should be normal divison as "//" istead of "/"

'''
