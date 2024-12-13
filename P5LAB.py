# Eric Corbett 
# Date: 11/17/2024
#P5LAB
#This program simulates a self-checkout where a customer is provided change based on the amount they owe and the amount they pay. The change is broken down into dollars, quarters, dimes, nickels, and pennies.

import random

# Function to disperse change
def disperse_change(change):
    # Initialize variables for coin denominations
    dollars = int(change // 1)
    change = round(change % 1, 2)  

    quarters = int(change // 0.25)
    change = round(change % 0.25, 2)

    dimes = int(change // 0.10)
    change = round(change % 0.10, 2)  

    nickels = int(change // 0.05)
    change = round(change % 0.05, 2)  

    pennies = int(change // 0.01)
    change = round(change % 0.01, 2)  
    
    # Display the result
    print("Your change is:")
    print(f"{dollars} Dollar(s)")
    print(f"{quarters} Quarter(s)")
    print(f"{dimes} Dime(s)")
    print(f"{nickels} Nickel(s)")
    print(f"{pennies} Penny(ies)")

# Main function
def main():
    # Generate a  price owed 
    owed = round(random.uniform(0.01, 100.00), 2)
    
    # Prompt the user for the amount of money they will give to the machine
    print(f"The total owed is: ${owed}")
    paid = float(input("Enter the amount of cash you will give to the self-checkout machine: $"))
    
    # Check if the customer provided enough money
    if paid < owed:
        print("Insufficient funds. Please enter a higher amount.")
    else:
        # Calculate the change owed
        change = round(paid - owed, 2)
        print(f"Change owed: ${change}")
        
        # Call the function to disperse the change
        disperse_change(change)

# Calling the main function to run the program
if __name__ == "__main__":
    main()
