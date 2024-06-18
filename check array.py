numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)


new_number = float(input("Enter a new number to check: "))

if new_number in numbers:
    position = numbers.index(new_number) + 1  
    print(f"The number {new_number} exists in the array at position {position}.")
else:
    print(f"The number {new_number} does not exist in the array.")