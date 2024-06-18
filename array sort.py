numbers = []

for i in range(6):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)


numbers.sort()

print("The sorted numbers are:", numbers)