
# Help functions:

def addition(number_list: list):
    '''
    Args: number_list: list

    Function to sum up the total value in a passed list.

    returns sum_of_list
    '''
    sum_of_list = 0
    for n in number_list:
        sum_of_list += n
    
    return sum_of_list

def subtraion(number_list: list):
    '''
    Args: number_list: list

    Function to subtract values from index 0.
    Startvalue - rest of the lists values

    returns sub_of_list
    '''
    sub_of_list = number_list[0]
    for n in number_list[1:]:
        sub_of_list -= n
        
    return sub_of_list

def multiplication(number_list: list):
    '''
    Args: number_list: list

    Function to multiply values in the list.
    number_list[0] * number_list[1] * ..... [n]

    returns multiplied_list
    '''
    
    muliplied_list = 1
    for n in number_list:
        muliplied_list *= n
    
    return muliplied_list 

def divison(number_list: list):
    '''
    Args: number_list: list

    Function to divide each element in list by 2
    [2,4,8] => [1,2,4]

    returns div_list
    '''
    div_list = []
    for n in number_list:
        div = n / 2 
        div_list.append(div)
    return div_list


def list_values():
    '''
    Args: None
    Function to take input from user, add to new created list.
    Loop through and add values from input - from user
    
    return number_list
    '''
    
    number_list = []
    numbers_to_add_count = int(input("Enter how many number you want to add: "))
    for _ in range(numbers_to_add_count):
        val = float(input("Enter value to be added to the list: "))
        number_list.append(val)
    print(f"The values you choose: \n \
          {number_list}")
    return number_list
    

print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation: ")
while True:
    userChoice = int(input("""\n"(1) Add numbers in list"
"(2) Subtract numbers in list"
"(3) Multiply numbers in list"
"(4) Divide numbers in list by 2:"
"(999) EXIT:"
\n"""))


    valid_numbers = [1, 2, 3, 4]

    if userChoice in valid_numbers:
        numbers = list_values()
        match userChoice:

            case 1:
                total = addition(numbers)
                print(f"The addition of {numbers} is {total} ")

            case 2:
                total = subtraion(numbers)
                print(f"The subtraction of {numbers} is {total} ")

            case 3:
                total = multiplication(numbers)
                print(f"The multiplication of {numbers} is {total} ")

            case 4:
                total = divison(numbers)
                print(f"The division of {numbers} by 2 is {total} ")
                
    elif userChoice == 999:
        print("Thank for using the calculator!")
        break
    
    else:
        print("Invaild menu choice")



