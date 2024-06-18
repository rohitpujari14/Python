def toggle_case_string(input_string):
    toggled_string = input_string.swapcase()
    return toggled_string

string_input = input("Enter a string: ")

result = toggle_case_string(string_input)
print("Toggled string:", result)