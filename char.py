def identify_and_display(char):
    if char.isdigit():
        print("You entered an integer:", char)
    elif char.isalpha():
        print("You entered a string:", char)
    else:
        print("You entered a special character or symbol:", char)

char_input = input("Enter a character: ") 
identify_and_display(char_input)