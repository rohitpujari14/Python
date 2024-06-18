def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Prime numbers from 3 to 30:")
for num in range(3, 31):
    if is_prime(num):
        print(num, end=" ")