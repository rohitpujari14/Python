def compare_number(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

number = float(input("Enter a number: "))

result = compare_number(number)
print("Result:", result)