num1, num2 = 0, 1

print("Fibonacci series of 10 numbers:")

# Loop to generate and display the Fibonacci series of the first 10 numbers
for _ in range(10):
    print(num1, end=" ")
    # Calculate the next number in the sequence by adding the previous two numbers
    num1, num2 = num2, num1 + num2

print()