def toggle_case(char):

    if char.isupper():

        return char.lower()

    elif char.islower():

        return char.upper()
    else:

        return char


char_input = input("Enter a character: ")

result = toggle_case(char_input)
print("Toggle of", char_input, "is", result)