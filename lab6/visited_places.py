
def append_list(visited_list: list):
    city = input("Enter city you want to add: ")
    visited_list = visited_list.append(city)
    return visited_list

def view_list(visited_list: list):
    print(visited_list)
    
def sort_list(visited_list: list):
    visited_list = sorted(visited_list)
    print(f"{visited_list}")
    return visited_list
    
def number_citys(visited_list: list):
    num_citys = len(visited_list)
    print(num_citys)
    return num_citys

def remove_city(visited_list: list):
    removed = str(input("Enter city to remove: "))
    visited_list = visited_list.remove(removed)
    return visited_list

def clear_list(visited_list: list):
    return visited_list.clear()

def save_list_file(visited_list: list):
    filename = input("Enter name of file: ")
    
    with open({filename} + '.txt', 'w') as file:
        n = 1
        for i in visited_list:
            file.write(f"{n} | city visited: {i} | \n")
            n += 1
            
def dashboard_menu():
    print("*"*50, "\n","*"*18, "My Travel List", "*"*18,"\n","*"*50, sep = "")
    for i in menu_options:
        print(i)
    print("*"*50)
    
menu_options = [
    
    "(1) Add new city",
    "(2) View your list",
    "(3) Sort the list",
    "(4) Show city count",
    "(5) Remove a city",
    "(6) Remove all cities",
    "(7) Save to file",
    "(999) Quit",
]

visited_list = []
run = False
while run is False:

    dashboard_menu()
    choice = int(input("Enter action in the menu above: "))
    if choice == 1:
        append_list(visited_list)
    elif choice == 2:
        view_list(visited_list)
    elif choice == 3:
        sort_list(visited_list)
    elif choice == 4:
        number_citys(visited_list)
    elif choice == 5:
        remove_city(visited_list)
    elif choice == 6:
        clear_list(visited_list)
    elif choice == 7:
        save_list_file(visited_list)
    elif choice == 999:
        break
    else:
        print("Invalid input... Try again.")
    
