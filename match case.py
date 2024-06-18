def add():
    print("Adding item...")

def modify():
    print("Modifying item...")

def delete():
    print("Deleting item...")

number = int(input("Enter a number (1 for add, 2 for modify, 3 for delete): "))

match number:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("Invalid input. Please enter 1, 2, or 3.")