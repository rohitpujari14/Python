total = 0


while True:
   
    num = float(input("Enter a number (enter 0 to stop): "))
    
 
    if num == 0:
        break  
    
    # Add the entered number to the total
    total += num

# Print the total sum
print("The total sum of all the numbers entered is:", total)