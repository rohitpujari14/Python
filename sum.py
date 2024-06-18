def sum_of_values_from_user():
    try:
        values = input("Enter values separated by spaces: ").split()
        values = [int(val) for val in values] 
        total_sum = sum(values)
        print("Sum of the provided values:", total_sum)
    except ValueError:
        print("Please enter valid numeric values.")

sum_of_values_from_user()