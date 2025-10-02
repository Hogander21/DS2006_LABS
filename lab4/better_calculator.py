
# Help functions:

def addition(x: float, y: float):
    '''
    Args: x: float, y: float

    Function to add x and y together as addition.

    returns x + y
    '''
    return x + y

def subtraion(x: float, y: float):
    '''
    Args: x: float, y: float

    Function to add x and y together.

    returns x - y
    '''
    return x - y

def multiplication(x: float, y: float):
    '''
    Args: x: float, y: float

    Function to multiply x and y together.

    returns x * y
    '''
    return x * y

def divison(x: float, y: float):
    '''
    Args: x: float, y: float 

    Function to divide x and y.

    returns x // y
    '''
    return x // y
    
def floor_divison(x: float, y: float):
    '''
    Args: x: float, y: float

    Function to floor divide x and y.

    returns x / y
    '''
    return x / y

def exponentiation(x: float, y: float):
    '''
    Args: x: float, y: float

    Function to exponate x with y

    returns x ** y
    '''
    return x**y

def modulus(x: float, y: float):
    '''
    Args: x: float, y: float

    Function operate modulus operator

    returns x % y 
    '''
    return x % y


print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation: ")
userChoice = int(input("""(1) Add two numbers",
"(2) Subtract two numbers",
"(3) Multiply two numbers",
"(4) Divide two numbers:",
"(5) Floor Divide two numbers:",
"(6) Exponentiation two numbers:",
"(7) Modulus two numbers:\n"""))



valid_numbers = [1,2,3,4,5,6,7]

if userChoice in valid_numbers:
    firstNumber = float(input("Type the first number: "))
    secondNumber = float(input("Type the second number: "))

    match userChoice:

        case 1:
            total = addition(firstNumber, secondNumber)
            print(f"The addition of {firstNumber} + {secondNumber} is {total} ")

        case 2:
            total = subtraion(firstNumber, secondNumber)
            print(f"The subtraction of {firstNumber} - {secondNumber} is {total} ")

        case 3:
            total = multiplication(firstNumber, secondNumber)
            print(f"The multiplication of {firstNumber} * {secondNumber} is {total} ")

        case 4:
            total = divison(firstNumber, secondNumber)
            print(f"The division of {firstNumber} // {secondNumber} is {total} ")

        case 5:
            total = floor_divison(firstNumber, secondNumber)
            print(f"The division of {firstNumber} / {secondNumber} is {total} ")

        case 6:
            total = exponentiation(firstNumber, secondNumber)
            print(f"The division of {firstNumber} ** {secondNumber} is {total} ")

        case 7:
            total = modulus(firstNumber, secondNumber)
            print(f"The division of {firstNumber} % {secondNumber} is {total} ")
else:
    print("Invaild menu choice")

