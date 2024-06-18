def validate_string_length(input_str, min_length=3, max_length=5):
 
    if min_length <= len(input_str) <= max_length:
        return True
    else:
        return False

input_string = input("Enter a string: ")
if validate_string_length(input_string):
    print("The string length is valid.")
else:
    print("The string length is not within the specified range.")