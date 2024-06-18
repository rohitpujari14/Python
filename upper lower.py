
char = input("Enter a character: ")
if char.isupper():
    print("The entered character is an uppercase letter.")
elif char.islower():
    print("The entered character is a lowercase letter.")
elif not char.isalpha():
    print("The entered character is not an alphabet.")